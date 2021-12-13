#   Day 02 of 100 Days Of Code

#   Q - Given an array and a number k where k is smaller than the size of the array,
#   we need to find the k’th smallest element in the given array.
#   It is given that all array elements are distinct.

#   ref - https://www.geeksforgeeks.org/kth-smallestlargest-element-unsorted-array/

def findkmin(arr, l, h, k):

    # check whether k doens't exceed the length of the array
    if (k > 0 and k <= h - l + 1): 
        pivot_in = findpivotposition(arr,l,h)  #pivot_in = index of pivot
        # print(f"{arr} -- {pivot}")
        # print(f"{pivot - l} == {k-1}")

        # here it is (pivot - l) because as k gets updated in each recursion as per the new l
        # so pivot index will also be updated each w.r.t the new l
        if (pivot_in - l == k - 1): 
            return arr[pivot_in]

        if (pivot_in - l > k - 1):
            return findkmin(arr, l, pivot_in - 1, k)
        
        # here k is updated each time as per the change in lth element in each recursion
        # hence the new k, e.g., k' = (k - pivot_in + l - 1)
        return findkmin(arr, pivot_in + 1, h, k - pivot_in + l -1) 

# partition algo to find the position or index of the pivot element
def findpivotposition(arr, l, h):
    p = arr[h]
    i = l
    for j in range(l, h):
        if (arr[j] <= p):
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[h] = arr[h], arr[i]
    return i

# driver function
arr = [11,31,9,23,29,15,27,21,1,19,7,13,25,17,3,5]
n = len(arr)
l = 0
k = 9

print(f"The {k}th minimum number in the array is {findkmin(arr,l,n-1,k)}")

# Time Complexity: O(n)
# Space Complexity: O(logn) average