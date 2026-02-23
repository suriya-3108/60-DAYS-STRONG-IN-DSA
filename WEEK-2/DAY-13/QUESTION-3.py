"""Problem 3 — Maximum Sum Subarray of Size k
Given an array of integers and a number k, find the maximum sum of any contiguous subarray of size k.

Example:
arr = [2, 1, 5, 1, 3, 2]
k = 3

Output: 9  # subarray [5,1,3] has the max sum"""

arr = [2, 1, 5, 1, 3, 2]

k = 3

summed_arr = sum(arr[0:k])

summed = summed_arr

for i in range(k,len(arr)):
    summed_arr = summed_arr - arr[i - k] + arr[i]
    summed = max(summed_arr, summed)
    
print(summed)
    