"""Question 4 (Medium — Prefix Sum)

Problem: Count Subarrays with Sum = K
Given an integer array arr and an integer k,
count the number of contiguous subarrays whose sum equals k.

Example 1:
arr = [1, 1, 1]
k = 2
# Output: 2"""

arr = [1, 1, 1]

k = 2

count = 0

for left in range(len(arr)):
    summed = 0
    for right in range(left , len(arr)):
        summed += arr[right]
        if summed == k:
            count += 1
    
print(count)