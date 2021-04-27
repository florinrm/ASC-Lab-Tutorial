#include <math.h>
#include <stdio.h>
#include <stdlib.h>

// functie kernel prin care adunam doi arrays
__global__ void vector_add(float *x, float *y, int n) {
    // calculam indexul - echivalent cu for-ul

    // threadId.x - id-ul unui thread blocul actual
	// blockDim.x - dimensiunea blocului actual
	// blockIdx.x - id-ul blocului actual


    int i = threadIdx.x + blockDim.x * blockIdx.x;

    if (i < n) {
        x[i] = x[i] + y[i];
    }
}

int main(void)
{
    const int num_elements = 1 << 16;
    const int num_bytes = num_elements * sizeof(float);

    float *host_array_x = 0, *host_array_y = 0; // arrays pentru host (CPU)
    float *device_array_x = 0, *device_array_y = 0; // arrays pentru device (GPU)

    // alocam memorie pentru host
    host_array_x = (float *) malloc(num_bytes);
    host_array_y = (float *) malloc(num_bytes);

    // alocam memorie pentru device
    cudaMalloc((void **) &device_array_x, num_bytes);
    cudaMalloc((void **) &device_array_y, num_bytes);

    // verificam daca alocarea a fost cu succes
    if (host_array_x == 0 || host_array_y == 0 || device_array_x == 0 || device_array_y == 0) {
        printf("[HOST] Couldn't allocate memory\n");
        return 0;
    }

    // se initializeaza x si y
    for (int i = 0; i < num_elements; i++) {
        host_array_x[i] = 4;
        host_array_y[i] = 2;
    }

    // facem transferul host -> device (CPU -> GPU)
    cudaMemcpy(device_array_x, host_array_x, num_bytes, cudaMemcpyHostToDevice);
    cudaMemcpy(device_array_y, host_array_y, num_bytes, cudaMemcpyHostToDevice);

    // stabilim dimensiunea unui bloc (adica numarul de threads dintr-un bloc)
    const size_t block_size = 256;
    
    // numarul de blocuri
    size_t blocks_no = num_elements / block_size;
 
    // daca avem un bloc care nu are dimensiunea 256, incrementam numarul de blocuri
    if (num_elements % block_size != 0) {
        ++blocks_no;
    }

    vector_add<<<blocks_no, block_size>>>(device_array_x, device_array_y, num_elements);
    
    // asteptam ca thread-urile de pe GPU sa-si termine treaba - echivalent cu pthread_join
    // ca apoi sa facem transferul GPU -> CPU
    cudaDeviceSynchronize();

    // transferul GPU -> CPU (device -> host)
    cudaMemcpy(host_array_x, device_array_x, num_bytes, cudaMemcpyDeviceToHost);
    cudaMemcpy(host_array_y, device_array_y, num_bytes, cudaMemcpyDeviceToHost);

    for (int i = 0; i < 10; ++i) {
        printf("Result %d: %1.1f + %1.1f = %1.3f\n", i, host_array_x[i] - host_array_y[i], 
                host_array_y[i], host_array_x[i]);
    }

    // eliberam memoria pe host
    free(host_array_x);
    free(host_array_y);

    // eliberam memoria pe device
    cudaFree(device_array_x);
    cudaFree(device_array_y);
  
    return 0;
}