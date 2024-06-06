#include <stdio.h>


int mult (int x, int y) {
    int i = 0,
        j = 0;
    LOOP:
    if (i < y) {
        j = j + x;
        i++;
        goto LOOP;
    }
    return j;
}

int fact (int x) {
    int i = 1, 
        j = 1;
    LOOP:
    if (i <= x) {
        j = mult(i, j);
        i++;
        goto LOOP;
    }
    return j;
}

int main (void) {
    int x = 5;
    printf("%d\n", fact(x));
}
