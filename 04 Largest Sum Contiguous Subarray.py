# Day 04 of 100 Days Of Code

# Q: Write an efficient program to find the sum of contiguous subarray 
# within a one-dimensional array of numbers that has the largest sum. 

# ref - https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/

# Also called Kadane's Algorithm

def maxArraysum(a, n):

    max_so_far = a[0]
    current_max = 0
    for i in range(0, n):
        current_max = current_max + a[i]

        ## checks if current_max is less than 0, if isn't then it compares with max_so_far
        if current_max < 0:
            current_max = 0
        
        elif max_so_far < current_max:
            max_so_far = current_max

    return max_so_far

## driver function
A = [-1, -4, -2, 4, 5, 1, -1, 3, -4, 5]
n = len(A)
print(f"Largest Maximum Continguous Subarray is {maxArraysum(A, n)}")

# Time Complexity: O(n) 
