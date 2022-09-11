'''Description :
This python file contains all searching alogorithms such as linearSearch, binarySearch
 

Developed by : Yash Raj
'''

def linearSearch(lst:list,key:int):
    '''A function to implement linear search in any list or an array.\n
    The function returns the index of the target element if exists in the list 
    otherwise returns -1 
    '''
    for element in range(len(lst)):
        if lst[element] == key :
            return element
    
    return -1
    

def binarySearch(lst:list,low:int,high:int,key:int):
    '''A function to implement a binary search in a given sorted list using Recursion
    Note : Only sorted array or a list is required.\n
    The function returns the index of the key element if exists in the list otherwise
    returns -1'''
    
    mid=int((high+low)/2)
    if key==lst[mid]:
        return mid
    elif key > lst[mid]:
        if mid==high:
            return -1
        return binarySearch(lst,mid+1,high,key)
    else:
        if mid==0:
            return -1
        return binarySearch(lst,low,mid-1,key)

