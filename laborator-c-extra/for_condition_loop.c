#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <sys/time.h>

#define N               100000000
#define SECOND_MICROS   1000000.f

int main(int argc, char** argv) {
    struct timeval start1, end1, start2, end2;

    printf("Condition in if\n");
    
    gettimeofday(&start1, NULL);
    for (long i = 0; i < N; i++) {
        if (i >= N / 2) {

        }
    }
    gettimeofday(&end1, NULL);

    printf("Condition in for\n");

    gettimeofday(&start2, NULL);
    for (long i = N / 2; i < N; i++) {
    }
    gettimeofday(&end2, NULL);

    printf("Condition in if: %f\n", ((end1.tv_sec - start1.tv_sec) * SECOND_MICROS 
        + end1.tv_usec - start1.tv_usec) / SECOND_MICROS);
    printf("Condition in for: %f\n", ((end2.tv_sec - start2.tv_sec) * SECOND_MICROS 
        + end2.tv_usec - start2.tv_usec) / SECOND_MICROS);

    return 0;
}