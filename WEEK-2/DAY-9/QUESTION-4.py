"""
Question 4: Squared Sorted Array

Given a sorted array of integers (can be negative), return a new array of their squares also sorted.

Example:

Input:  [-4, -1, 0, 3, 10]
Output: [0, 1, 9, 16, 100]
"""

arr = [-4, -1, 0, 3, 10]
n = len(arr)
output = [0] * n 

left = 0
right = n - 1
pos = n - 1 

while left <= right:
    if abs(arr[left]) > abs(arr[right]):
        output[pos] = arr[left] ** 2
        left += 1
    else:
        output[pos] = arr[right] ** 2
        right -= 1
    pos -= 1

print(output)
