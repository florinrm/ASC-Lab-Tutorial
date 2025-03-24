#include <stdio.h>
#include <stdlib.h>

#define SIZE 100

int main(int argc, char **argv) {
    int **matrix = malloc(SIZE * sizeof(int*));
    
    if (matrix == NULL) {
        perror("malloc failed\n");
        exit(EXIT_FAILURE);
    }

    for (int i = 0; i < SIZE; i++) {
        matrix[i] = malloc(SIZE * sizeof(int));

        if (matrix[i] == NULL) {
            perror("malloc failed\n");
            exit(EXIT_FAILURE);
        }
    }

    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            matrix[i][j] = i + j;
        }
    }

    int *vect = malloc(SIZE * SIZE * sizeof(int*));
    
    if (vect == NULL) {
        perror("malloc failed\n");
        exit(EXIT_FAILURE);
    }

    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            vect[i * SIZE + j] = i + j;
        }
    }

    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            if (matrix[i][j] != vect[i * SIZE + j]) {
                perror("not equal\n");
                exit(EXIT_FAILURE);
            }
        }
    }

    return 0;
}