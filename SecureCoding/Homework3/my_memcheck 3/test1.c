#include <stdlib.h>
#include <stdio.h>
// This program is leaking heap space thru p1 and p3 .
int main() {
    void *p1 = malloc(30);
    void *p2 = malloc(40);
    void *p3 = malloc(50);
    free(p2);
    return 0;
}
