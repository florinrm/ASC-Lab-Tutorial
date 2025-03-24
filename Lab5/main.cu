
#include <stdlib.h>
#include <vector>
#include <algorithm>
#include <iostream>

#define TILE_WIDTH 16

__global__ void sum_matrices(float *ma, float *mb, float *mc, int height, int width)
{
	int row = blockIdx.y * blockDim.y + threadIdx.y; // linie
    int col = blockIdx.x * blockDim.x + threadIdx.x; // coloana
    
    // se poate si invers, adica row = blockIdx.x * blockDim.x + threadIdx.x;

    if (row < height && col < width) {
	    mc[row * height + col] = ma[row * height + col] + mb[row * height + col];
    }
}

int main() {
	// size
    const size_t n = 1 << 6;
    
    // setam dimensiunea unui bloc pentru linie, respectiv coloana
    const dim3 block_size(TILE_WIDTH, TILE_WIDTH);
    
    // determinam numarul de blocuri pentru linie, respectiv coloana
    const dim3 num_blocks(n / block_size.x, n / block_size.y);
    // nu avem dim2 in CUDA

    // alocam memorie pentru host
    float *host_a = 0, *host_b = 0, *host_c = 0;
	host_a = (float *) malloc(n * n * sizeof(float));
    host_b = (float *) malloc(n * n * sizeof(float));
    host_c = (float *) malloc(n * n * sizeof(float));
    
	for (int i = 0; i < n * n; i++) {
		host_a[i] = 2;
        host_b[i] = 4;
        host_c[i] = 0;
	}

    // alocam memorie pentru device
	float *device_a = 0, *device_b = 0, *device_c = 0;
	cudaMalloc((void**)&device_a, sizeof(float) * n * n);
	cudaMalloc((void**)&device_b, sizeof(float) * n * n);
	cudaMalloc((void**)&device_c, sizeof(float) * n * n);

    // transfer date CPU -> GPU
	cudaMemcpy(device_a, &host_a[0], sizeof(float) * n * n, cudaMemcpyHostToDevice);
    cudaMemcpy(device_b, &host_b[0], sizeof(float) * n * n, cudaMemcpyHostToDevice);
    cudaMemcpy(device_c, &host_c[0], sizeof(float) * n * n, cudaMemcpyHostToDevice);

    // evenimente CUDA, pe care le folosim pentru masurarea timpului de executie
    cudaEvent_t launch_begin, launch_end;

    // creeam evenimentele
	cudaEventCreate(&launch_begin);
	cudaEventCreate(&launch_end);
    
    // lansam in executie evenimentul pentru start
    cudaEventRecord(launch_begin);
    
    // lansam kernel-ul in executie
	sum_matrices<<<num_blocks, block_size>>>(device_a, device_b, device_c, n, n);
    
    // lansam in executie evenimentul pentru stop
    cudaEventRecord(launch_end);

    // in loc sa folosim cudaDeviceSynchronize, folosim cudaEventSynchronize
    // prin care se asteapta terminarea thread-urilor
	cudaEventSynchronize(launch_end);

    float time = 0;
    // determinam timpul de executie
	cudaEventElapsedTime(&time, launch_begin, launch_end);
	
    std::cout << "Time = " << time << std::endl;
    
    cudaMemcpy(host_c, &device_c[0], sizeof(float) * n * n, cudaMemcpyDeviceToHost);
    for (int i = 0; i < 20; i++) {
        std::cout << host_c[i] << " ";
    }
    std::cout << std::endl;

    // distrugem evenimentele
    cudaEventDestroy(launch_begin);
    cudaEventDestroy(launch_end);

	cudaFree(device_a);
	cudaFree(device_b);
    cudaFree(device_c);
    
	free(host_a);
	free(host_b);
	free(host_c);

	return 0;
}
