#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <sys/time.h>

#define N               600
#define SECOND_MICROS   1000000.f
#define MIN(a, b) (((a) < (b)? (a) : (b)))

int main(int argc, char** argv) {
    int *a, *b, *c, *d;
    struct timeval start1, end1, start2, end2;
    int block_size = 100;

    a = malloc(N * N * sizeof(int));
    b = malloc(N * N * sizeof(int));
    c = malloc(N * N * sizeof(int));
    d = malloc(N * N * sizeof(int));

    if (a == NULL || b == NULL || c == NULL || d == NULL) {
        perror("malloc failed\n");
        exit(EXIT_FAILURE);
    }

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            for (int k = 0; k < N; k++) {
                c[i * N + j] += a[i * N + k] * b[k * N + j];
            }
        }
    }
    
    printf("Basic multiplication\n");
    
    gettimeofday(&start1, NULL);
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            for (int k = 0; k < N; k++) {
                c[i * N + j] += a[i * N + k] * b[k * N + j];
            }
        }
    }
    gettimeofday(&end1, NULL);

    printf("Blocked multiplication\n");

    gettimeofday(&start2, NULL);
    // TODO
    gettimeofday(&end2, NULL);

    printf("Checking...\n");
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            for (int k = 0; k < N; k++) {
                if (c[i * N + j] != d[i * N + j]) {
                    printf("[%d][%d] diff: %d VS %d\n", i, j, c[i * N + j], d[i * N + j]);
                    printf("Mai invata programare, boss\n");
                    free(a);
                    free(b);
                    free(c);
                    free(d);
                    exit(EXIT_FAILURE);
                }
            }
        }
    }
    printf("Bravo boss!\n");

    printf("Basic multiplication time (N = %d): %f\n", N, ((end1.tv_sec - start1.tv_sec) * SECOND_MICROS 
        + end1.tv_usec - start1.tv_usec) / SECOND_MICROS);
    printf("Blocked multiplication time (N = %d, block size = %d): %f\n", N, block_size, ((end2.tv_sec - start2.tv_sec) * SECOND_MICROS 
        + end2.tv_usec - start2.tv_usec) / SECOND_MICROS);
    
    free(a);
    free(b);
    free(c);
    free(d);

    return 0;
}