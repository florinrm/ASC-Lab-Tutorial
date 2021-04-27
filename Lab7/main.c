#include <math.h>
#include <stdio.h>
#include <stdlib.h>

void vector_add(float *x, float *y, int n) {
    for (int i = 0; i < n; i++) {
        x[i] = x[i] + y[i];
    }
}

int main(void)
{
    const int num_elements = 1 << 16;
    const int num_bytes = num_elements * sizeof(float);

    float *x, *y;

    x = (float *) malloc(num_bytes);
    y = (float *) malloc(num_bytes);

    // verificam daca alocarea a fost cu succes
    if (x == NULL || y == NULL) {
        printf("Couldn't allocate memory\n");
        return 0;
    }

    // se initializeaza x si y
    for (int i = 0; i < num_elements; i++) {
        x[i] = 4;
        y[i] = 2;
    }

    vector_add(x, y, num_elements);

    for (int i = 0; i < 10; ++i) {
        printf("Result %d: %1.1f + %1.1f = %1.3f\n", i, x[i] - y[i], y[i], x[i]);
    }

    free(x);
    free(y);
    return 0;
}