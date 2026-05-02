#define _GNU_SOURCE
#include <fcntl.h>
#include <stdlib.h>
#include <dlfcn.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>

#define FREE_UNINIT 3
#define FREE_GOOD 0
#define FREE_DUPLICATE 2

char my_memcheck_pool[65536];
void* invalidAddresses[65536];
int invalidAddressesIndex = 0;

struct malloc_store{
    int size;
    void* address;
    int free;
    int canary;
    int freeCanary;
};
struct malloc_store ms[65536];
int msIndex = 0;
    
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

        p = real_malloc(size+4);
	ms[msIndex].size = size;
	ms[msIndex].address = p;
	ms[msIndex].free = 0;
	ms[msIndex].canary = rand();
	ms[msIndex].freeCanary = 0;
	((int*)p)[size] = ms[msIndex].canary;
        fprintf(stderr, "malloc(%d) = %p\n", size, p);
	msIndex++;
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
        //real_free(p);
	int freeValid = FREE_UNINIT;
	int i = 0;
	for(; i < msIndex; ++i){
	    if(ms[i].address == p){
		if(ms[i].free == 0){
		    ms[i].free = 1;
		    freeValid = FREE_GOOD;
		}
		else{
		    freeValid = FREE_DUPLICATE;
		    ms[i].free++;
		}
		break;
	    }
	}
	if (freeValid == FREE_UNINIT){
	    invalidAddresses[invalidAddressesIndex] = p;
	    invalidAddressesIndex++;
	}
	else if (freeValid == FREE_GOOD){
	    int freeCanary = ((int*)p)[ms[i].size];
	    ms[i].freeCanary = freeCanary;
	    real_free(p);
	}
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
    for(int i = 0; i < msIndex; i++){
        if(ms[i].free == 0){
            fprintf(stderr, "Memory never freed at: %p\n", ms[i].address);
        }
	else if(ms[i].free > 1){
	    fprintf(stderr, "Duplicate free called for: %p, %d extra times\n", ms[i].address, ms[i].free-1);
	}
	if(ms[i].canary != ms[i].freeCanary){
	    fprintf(stderr, "Canary overwritten at: %p, Overwritten canary = %x, Expected canary = %x\n", ms[i].address, ms[i].freeCanary, ms[i].canary);
	}
    }
    for(int i = 0; i < invalidAddressesIndex; i++){
	fprintf(stderr, "Invalid free called at: %p\n", invalidAddresses[i]);
    }
    fprintf(stderr,"postmain\n");
}
