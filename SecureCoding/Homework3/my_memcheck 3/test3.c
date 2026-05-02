#include <stdio.h>
#include <stdlib.h>
#include <stdio.h>
// This program is leaking heap space thru main:ptr and foo:ptr2 .
void foo()
{
  void *ptr = malloc(16);
  void *ptr2 = malloc(32);
  free(ptr);
}
int main()
{
  void *ptr = malloc(16);
  foo();
}
