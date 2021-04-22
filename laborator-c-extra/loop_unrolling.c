#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <sys/time.h>

#define N               100000000
#define SECOND_MICROS   1000000.f

int main(int argc, char** argv) {
    struct timeval start1, end1, start2, end2;

    printf("Normal\n");
    
    gettimeofday(&start1, NULL);
    for (long i = 0; i < N; i++) {
    }
    gettimeofday(&end1, NULL);

    printf("Loop unrolling\n");

    gettimeofday(&start2, NULL);
    for (long i = 0; i < N; i += 10) {
        i++;
        i++;
        i++;
        i++;
        i++;
        i++;
        i++;
        i++;
        i++;
        i++;
    }
    gettimeofday(&end2, NULL);

    printf("Normal: %f\n", ((end1.tv_sec - start1.tv_sec) * SECOND_MICROS 
        + end1.tv_usec - start1.tv_usec) / SECOND_MICROS);
    printf("Loop unrolling: %f\n", ((end2.tv_sec - start2.tv_sec) * SECOND_MICROS 
        + end2.tv_usec - start2.tv_usec) / SECOND_MICROS);

    return 0;
}