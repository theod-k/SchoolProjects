#include <stdlib.h>
#include <stdio.h>
#include <string.h>
// This program has 2 heap overwrite operations.
int main() {
    void *p = malloc(10);
    void *p2 = malloc(20);
//  Overwriting one byte in p here
    strcpy(p,"0123456789"); 
//  Overwriting one byte in p2 here
    strcpy(p2,"01234567890123456789"); 
    free(p);
    return 0;
}
