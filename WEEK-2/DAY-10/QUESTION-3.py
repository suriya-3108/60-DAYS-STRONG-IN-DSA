"""
Problem 3 — Smallest Subarray with Sum ≥ Target

Given:
arr = [2, 1, 5, 2, 3, 2]
target = 7

Return the length of the smallest contiguous subarray
whose sum is greater than or equal to target.

Expected Output:
2

Explanation:
[5,2] → sum = 7 → length = 2
"""

arr = [2, 1, 5, 2, 3, 2]

target = 7

left = 0

right = 0

total = 0

min_length = float("inf")

while right < len(arr):
    total += arr[right]
    
    while(total >= target):
        length = right - left + 1
        total = total - arr[left]
        if length < min_length:
            min_length = length
        left += 1
    
    right += 1
        
        
print(min_length)