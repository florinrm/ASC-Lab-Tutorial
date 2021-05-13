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

    float *x, *y;

    cudaMallocManaged(&x, num_bytes);
    cudaMallocManaged(&y, num_bytes);

    if (!x || !y) {
		fprintf(stderr, "[HOST & DEVICE] cudaMallocManaged failed\n");
		return 1;
	}

    // se initializeaza x si y
    for (int i = 0; i < num_elements; i++) {
        x[i] = 4;
        y[i] = 2;
    }

    // stabilim dimensiunea unui bloc (adica numarul de threads dintr-un bloc)
    const size_t block_size = 256;
    
    // numarul de blocuri
    size_t blocks_no = num_elements / block_size;
 
    // daca avem un bloc care nu are dimensiunea 256, incrementam numarul de blocuri
    if (num_elements % block_size != 0) {
        ++blocks_no;
    }

    vector_add<<<blocks_no, block_size>>>(x, y, num_elements);
    
    // asteptam ca thread-urile de pe GPU sa-si termine treaba - echivalent cu pthread_join
    cudaDeviceSynchronize();


    for (int i = 0; i < 10; ++i) {
        printf("Result %d: %1.1f + %1.1f = %1.3f\n", i, x[i] - y[i], 
                y[i], x[i]);
    }

    // eliberam memoria pe device
    cudaFree(x);
    cudaFree(y);
  
    return 0;
}