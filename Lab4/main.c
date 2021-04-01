#include <stdio.h>
#include <stdlib.h>

#define SIZE 10

struct first_struct {
    int a;
    long b;
    int c;
};

struct second_struct {
    int a;
    int b;
    long c;
};

struct third_struct {
    int a;
    long b;
    int c;
} __attribute__((packed)); 

int main(int argc, char **argv) {
    struct first_struct f1;
    f1.a = 10;
    f1.b = 10;
    f1.c = 10;

    struct second_struct f2;
    f2.a = 10;
    f2.b = 10;
    f2.c = 10;

    struct third_struct f3;
    f3.a = 10;
    f3.b = 10;
    f3.c = 10;

    printf("int size: %ld\n", sizeof(int));
    printf("long size: %ld\n", sizeof(long));

    printf("first_struct size: %ld\n", sizeof(f1));  // 4 + 4 (padding) + 8 + 4 + 4 (padding)
    printf("second_struct size: %ld\n", sizeof(f2)); // 4 + 4 + 8
    printf("third_struct size: %ld\n", sizeof(f3)); // 4 + 4 + 8

    struct second_struct *struct_arr = malloc(SIZE * sizeof(struct second_struct));
    for (int i = 0; i < SIZE; i++) {
        struct_arr[i].a = i;
        struct_arr[i].b = i + 1;
        struct_arr[i].c = i + 2;
    }

    int *arr = (int*) struct_arr;
    for (int i = 0; i < 4 * SIZE; i++) {
        printf("%d ", arr[i]);
    }

    printf("\n");

    return 0;
}