#include <stdio.h>
#include <string.h>

int a1[5];
int a4[8][8];
int main()
{
    // using printf format %p to print the address
    printf("a1 %p\n",&a1[0]);
    printf("a4 %p\n",&a4[0][0]);

    a1[0]=8;
    /*
    Add code below this comment that looks like:

    a1[something] = 8;
    */

    a1[8] = 8;
    a1[15] = 8;

    a1[16] = 8;
    a1[23] = 8;

    a1[24] = 8;
    a1[31] = 8;

    a1[32] = 8;
    a1[39] = 8;

    a1[40] = 8;
    a1[47] = 8;

    a1[48] = 8;
    a1[55] = 8;

    a1[56] = 8;
    a1[63] = 8;

    a1[64] = 8;
    a1[71] = 8;

    
    printf("a1[]=%d,%d,%d,%d,%d\n",a1[0],a1[1],a1[2],a1[3],a1[4]);
    for (int i=0; i<8; i++) {
        for (int j=0; j<8; j++)
            printf("%d,",a4[i][j]);
        printf("\n");
    }
}