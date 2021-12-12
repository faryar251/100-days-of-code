#   Day 01 of 100 Days Of Code
#   Q - Given an array of integers, and a number ‘sum’, find the number of pairs of integers in the array whose sum is equal to ‘sum’

#   ref - https://www.geeksforgeeks.org/count-pairs-with-given-sum/?ref=lbp

#   Time Complexity - O(n)

def countpair_sum(ar, sum):
    freq = {}  # empty dictionary to monitor the frequency of numbers 
    count = 0

    for i in range(0, len(ar)):
        # check the occurance of the pair before the current iteration
        # if duplicate exists, then the current number ar[i] will be paired with all the duplicate pairs that occured before this iteration
        if sum - ar[i] in freq:
            count += freq[sum-ar[i]]

        # check if the current no already exists in the dictionary or not
        # if it already exists, then increment 
        if ar[i] in freq: 
            freq[ar[i]] +=1
        # if it doesn't exists and this is the first occurance, then add '1' as the value
        else:
            freq[ar[i]] = 1

    return count


## Driver function to test the code
ar = [-1, 5, 3, 1, 0, 9, 1, 7, 8, -2, 2]
sum = 6
print(f"Total number of sum pairs for {sum} in this array is {countpair_sum(ar, sum)}")