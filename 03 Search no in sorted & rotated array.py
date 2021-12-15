# Day 03 of 100 Days Of Code

# Given a sorted and rotated array A of N distinct 
# elements which is rotated at some point, and given an element key. 
# The task is to find the index of the given element key in the array A.

# ref - https://www.geeksforgeeks.org/search-an-element-in-a-sorted-and-pivoted-array/

## ex, A = [4,5,6,7,8,9,10 1,2,3]

def search(arr, l, h, key):

    ## base case when the key is not found in the array
    if l > h:
        return -1

    m = (l + h) // 2

    if key == arr[m]:
        return m
    
    #Sorted 1st half as in [4,5,6,7,8] or [4,5,6,7,8,9,10,1,2,3]
    if arr[l] < arr[m]:
        # key = 4 to 6 or 4 to 8 
        if key >= arr[l] and key <= arr[m]:
            return search(arr, l, m-1, key)
        #key = 7 to 8 or 9 to 3
        return search(arr, m+1, h, key)

    #Unsorted 1st half as in [9, 10, 1, 2, 3]
    if key >= arr[m] and key <= arr[h]: 
        # key = 2, then 2nd half array search
        return search(arr, m+1, h, key)
    # key = 9 or 10
    return search(arr,l, m-1, key)

# driver function
A = [4,5,6,7,8,9,10,1,2,3]
key = 10
N = len(A)
i = search(A, 0, N-1, key)

if i != -1:
    print('Key found at %d' %i)
else:
    print('Key not found')

# Instead of two or more pass of binary search, the result can be found in one pass of binary search in this approach
# Binary Search requires log n comparisons to find the element.
# Time Complexity: O(log n)

# As no extra space is required.
# Space Complexity: O(1)
