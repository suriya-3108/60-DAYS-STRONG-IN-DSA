"""Question 3 (Medium — Sliding Window)

Problem: Maximum Sum Subarray of Size K
Given an integer array arr and an integer k,
find the maximum sum of any contiguous subarray of size k.

Example 1:
arr = [2, 1, 5, 1, 3, 2]
k = 3
# Output: 9"""

arr = [2, 1, 5, 1, 3, 2]

k = 3

summed_arr = sum(arr[:k])

maximum = summed_arr

for i in range(k,len(arr)):
    summed_arr = summed_arr - arr[i -k] + arr[i]
    maximum = max(maximum, summed_arr)
    
print(maximum)
    
    
            