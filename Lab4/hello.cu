#include <stdio.h>
 
__global__ void kernel_example(int value) {
    printf("[GPU] Hello from the GPU!\n");
    printf("[GPU] The value is %d\n", value);
    printf("[GPU] blockDim = %d, blockId = %d, threadIdx = %d\n", blockDim.x, blockIdx.x, threadIdx.x);
}
 
int main(void) {
    int nDevices;
    printf("[HOST] Hello from the host!\n");
    
    cudaGetDeviceCount(&nDevices);
    printf("[HOST] You have %d CUDA-capable GPU(s)\n", nDevices);
    
    // 4 blocuri, fiecare bloc cu 4 threads
    kernel_example<<<4,4>>>(25);
    cudaDeviceSynchronize();
    
    return 0;
}