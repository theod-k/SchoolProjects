In this implementation, the important things are as follows:
First I create some global variables to store error information. These are as follows:
invalidAddresses to store the addresses provided by free calls to invalid addresses.
malloc_store to store information whenever a malloc is called.
ms as an array of malloc_store to store each individual malloc call. This is then referenced later in free and in the destructor to check for errors.

I also created indexes corresponding to these global variables so the program wouldn't iterate into an empty array.

From there the changes to malloc are as follows:
Before the print, I initialize the malloc's details into ms such as the size, address, free (to store whether the malloc has been properly freed), the canary, and the freeCanary (to later store the canary when free is called).

The changes to free are as follows:
Inside of free I have created a variable freeValid to help store the following: 
If the free has been made more than once to the same address
If the free has been made to an invalid address
If the free has been done correctly
This ensures that real_free will only be called when free has been used properly, and it won't be called if freeValid has been set otherwise.

From there I iterate through ms to check if the free call made corresponds to any of the cases that the homework asks for and assign freeValid accordingly.

If in the for loop the address is found, the free value of that malloc call is set to 1.
If that malloc call has already been set to 1, then the value of free is incremented by 1 to track it as a duplicate free call.
In the case that the for loop finished and freeValid is still uninitialized, then that means that the free call has been made to an invalid address and invalidAddresses is updated accordingly.
In the case that everything is normal, the freeCanary is updated and real_free is called.

Finally in the destructor:
I first iterate through ms to check for the following:
If all mallocs have been freed.
If there are any duplicate frees called on a single malloc.
If the canary is preserved.
If any of these meet their respective triggers (aka there is a malloc with free=0, or a malloc with a free>1, or a malloc where freeCanary doesn't equal canary) then a corresponding error message will be printed.

Finally I go through invalidAddresses to see if there were any invalid free calls made and print them if such a thing has happened.