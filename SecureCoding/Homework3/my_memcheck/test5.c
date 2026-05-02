#include <stdio.h>
#include <stdlib.h>
#include <stdio.h>
// This program is leaking thru main:ptr, foo:ptr2, and has an invalid free(0)
void foo()
{
  void *ptr = malloc(16);
  void *ptr2 = malloc(32);
  free(ptr);
  free(0);
}
int main()
{
  void *ptr = malloc(16);
  foo();
}
