#define _GNU_SOURCE
#include <fcntl.h>
#include <stdlib.h>
#include <dlfcn.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>
char my_memcheck_pool[65536];

void* malloc(size_t size)
{
    static int recursively_called = 0;
    static void* (*real_malloc)(size_t) = NULL;
    void *p;
    int f;
    if (!recursively_called)
    {
        recursively_called=1;
        if (!real_malloc)
            real_malloc = dlsym(RTLD_NEXT, "malloc");

        p = real_malloc(size);
        fprintf(stderr, "malloc(%d) = %p\n", size, p);
        recursively_called=0;
    }
    else
    {
        p = real_malloc(size);
    }
    return p;
}
void free(void *p)
{
    static int recursively_called = 0;
    static void (*real_free)(void*) = NULL;
    if (!recursively_called)
    {
        recursively_called=1;
        if (!real_free)
            real_free = dlsym(RTLD_NEXT, "free");
        real_free(p);
        fprintf(stderr, "free(%p)\n", p);
        recursively_called=0;
    }
    else
    {
        real_free(p);
    }
}
void __attribute__ ((constructor)) premain()
{
    fprintf(stderr,"premain\n");
}
void __attribute__ ((destructor)) postmain()
{
    fprintf(stderr,"postmain\n");
}
