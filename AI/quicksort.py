def quicksort(arr, start, end, index):
    if start < end:
        if(index == 2):
            pivotIndex = partitionInt(arr, start, end, index)
        else:
            pivotIndex = partition(arr, start, end, index)
        quicksort(arr, start, pivotIndex-1, index)
        quicksort(arr, pivotIndex+1, end, index)

def partitionInt(arr, start, end, index):
    pivot = int(arr[end][index])
    
    i = start - 1
    
    for j in range(start, end):
        if int(arr[j][index]) > pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i+1], arr[end] = arr[end], arr[i+1]
    return i + 1

def partition(arr, start, end, index):
    pivot = arr[end][index]
    
    i = start - 1
    
    for j in range(start, end):
        if arr[j][index] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i+1], arr[end] = arr[end], arr[i+1]
    return i + 1

contents = []
with open("unsorted.txt", "r") as f:
    lines = f.readlines()

for l in lines:
    l = l.replace(',', '')
    l = l.replace('\n', '')
    contents.append(l.split(' '))

index = input("Enter 1 for last name sorting, 2 for first name sorting, and 3 for grade sorting: ")

quicksort(contents, 0, len(contents)-1, (int)(index)-1)
for i in contents:
    print(i)