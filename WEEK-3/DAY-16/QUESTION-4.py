"""Longest Subarray with Sum = K
Problem Statement
Given an array of integers and a number K, find the length of the longest subarray whose sum equals K.

Sample Input
arr = [1, 2, 3, 4, 5]
K = 9
Sample Output
3"""

arr = [1, 2, 3, 4, 5]
K = 9

left = 0

right = 0

length = 0

total = 0

for right in range(len(arr)):
    total += arr[right]

    if total > K:
        total -= arr[left]
        
    if total == K:
            left += 1
            length = right - left + 1

print(length)    