#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <sys/time.h>

#define N               600
#define SECOND_MICROS   1000000.f

int main(int argc, char** argv) {
    int a[N][N], b[N][N], c[N][N], d[N][N];
    struct timeval start1, end1, start2, end2;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            a[i][j] = 1;
            b[i][j] = 2;
            c[i][j] = 0;
            d[i][j] = 0;
        }
    }
    
    printf("Basic multiplication\n");
    
    gettimeofday(&start1, NULL);
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            for (int k = 0; k < N; k++) {
                c[i][j] += a[i][k] * b[k][j];
            }
        }
    }
    gettimeofday(&end1, NULL);

    printf("i-k-j loop reorder\n");

    gettimeofday(&start2, NULL);
    // TODO
    gettimeofday(&end2, NULL);

    printf("Checking...\n");
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            for (int k = 0; k < N; k++) {
                if (c[i][j] != d[i][j]) {
                    printf("[%d][%d] diff: %d VS %d\n", i, j, c[i][j], d[i][j]);
                    printf("Mai invata programare, boss\n");
                    exit(EXIT_FAILURE);
                }
            }
        }
    }
    printf("Bravo boss!\n");

    printf("Basic multiplication time (N = %d): %f\n", N, ((end1.tv_sec - start1.tv_sec) * SECOND_MICROS 
        + end1.tv_usec - start1.tv_usec) / SECOND_MICROS);
    printf("i-k-j loop reorder time (N = %d): %f\n", N, ((end2.tv_sec - start2.tv_sec) * SECOND_MICROS 
        + end2.tv_usec - start2.tv_usec) / SECOND_MICROS);
    
    return 0;
}