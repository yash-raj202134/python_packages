'''Description :
This python file contains all sorting alogorithms such as quicksort,mergesort, bubblesort,insertion sort
selection sort 

Developed by : Yash Raj
'''

# Bubble Sort 
def bubbleSort(array:list,n:int):
    '''A function to perform the sorting of the passed list using bubblesort technique '''
    issorted=0  # temporary variable to track already sorted array or list
    for i in range (0,n):
        issorted=1
        for j in range (0,n-i-1):
            if array[j] > array[j+1]: # comparing the element with the next consecutive element
                array[j],array[j+1] = array[j+1],array[j] # swapping
                issorted=0 
        
        if issorted : 
            return
        
# Insertion sort
def insertionSort(Arr:list, n:int):
    '''A function to perform the sorting of the passed list using insertionsort technique '''
    for i in range(1, n):
        key = Arr[i]
        j = i-1

        while Arr[j] > key and j >= 0:
            Arr[j+1] = Arr[j]
            j -= 1

        Arr[j+1] = key
        
# Selection sort
def selectionSort(arr:list,n:int):
    '''A function to perform the sorting of the passed list using selectionsort technique '''
    for i in range(0,n-1):
        index_of_min=i
        for j in range(i+1,n):
            
            if  arr[j] < arr[index_of_min] :
                index_of_min = j
        
        arr[i],arr[index_of_min] = arr[index_of_min],arr[i]

# Merge sort
def merge(arr:list,left:int,right:int):
    '''A utility function that simply merges 2 passed sorted array or a list''' 
    i=j=k=0  # starting indices
    while i < len(left) and j < len(right):  
        if left[i] <= right[j] :  # comparing left and the right array elements
            arr[k]=left[i]   # assigning the shortest element to our original array
            i+=1   
        else:
            arr[k]=right[j] 
            j+=1
        k+=1  
    
    # checking for the left out element in left array just in case
    while i < len(left): 
        arr[k]=left[i]
        i+=1
        k+=1
    # checking for the left out element in right array 
    while j < len(right): 
        arr[k]=right[j]
        j+=1
        k+=1
        
def mergeSort(arr:list):
    '''MergeSort function to implement merge sort technique ''' 
    
    # exit condition
    if len(arr)<=1: # already sorted 
        return   # return nothing
    # calculating mid of the array passed
    mid = int(len(arr)/2) 
    Left = arr[:mid]  # creating Left array (from start till the mid value)  
    Right = arr[mid:] # creating Right array(from mid value till the end)
    mergeSort(Left) # recursive call for left array 
    mergeSort(Right)  # recursive call for right array
    merge(arr,Left,Right)  # finally merge 

# Quicksort
def partition(arr:list, low:int, high:int):
    '''A partition function to perform the partition process in the 
    passed array or a list'''
    # choosing the first element as the pivot in a list.
    pivot = arr[low]
    i, j = low + 1, high

    # compare each element with pivot
    while i <= j:
        if arr[j] < pivot and arr[i] > pivot:
            arr[j], arr[i] = arr[i], arr[j]   # swap

        if not arr[i] > pivot:
            i += 1

        if not arr[j] < pivot:
            j -= 1

    arr[low], arr[j] = arr[j], arr[low]  # swapping the pivot element with j

    return j  # returning the index of pivot element after setting it


def quickSort(array:list, low:int, high:int):
    '''A quick sort function to perform quicksort in the 
    passed array or a list'''

    if low < high:
        # Find the pivot element such that
        # element smaller than pivot are on the left
        # and the element greater than pivot are on the right
        # fetches the index of pivot element
        partition_index = partition(array, low, high)

        # Recursive call to sort the left subarray of the pivot.
        quickSort(array, low, partition_index-1)
        # Recursive call to sort the Right subarray of the pivot.
        quickSort(array, partition_index+1, high)
        