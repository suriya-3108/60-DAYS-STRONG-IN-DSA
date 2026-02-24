"""Question 1 (Medium — Very Important Pattern)
Problem: Longest Subarray with Sum = K

Given an integer array arr and an integer k,
return the length of the longest subarray whose sum equals k.

Example 1:
Input:
arr = [1, 2, 3, 1, 1, 1, 1]
k = 3

Output:
3"""

arr = [1, 2, 3, 1, 1, 1, 1]

k = 3

length = 0

for left in range(len(arr)):
    curr = 0
    for right in range(left, len(arr)):
        curr += arr[right]
        if curr == k:
            length = max(length, right - left + 1)
                     
print(length)
