"""
Problem 1 — Maximum Sum Subarray of Size K
Given an array of integers and an integer k,
find the maximum sum of any contiguous subarray of size k.

Example:
Input:
arr = [2, 1, 5, 1, 3, 2]
k = 3

Output:
9

Explanation:
Subarrays of size 3:
[2,1,5] = 8
[1,5,1] = 7
[5,1,3] = 9  ← maximum
[1,3,2] = 6
"""

arr = [2, 1, 5, 1, 3, 2]

k = 3

sum_arr = sum(arr[0:k])

max_num = sum_arr

for i in range(k,len(arr)):
    sum_arr = sum_arr - arr[i - k] + arr[i]
    max_num = max(max_num, sum_arr)
    
print(max_num)