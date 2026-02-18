"""
Day 8 Extra Problem 3
Left Rotate Array by k Using Reversal Algorithm
📌 Problem:

Given an array of integers and an integer k, rotate the array to the left by k positions in-place.

Input:
arr = [1, 2, 3, 4, 5]
k = 2

Output:
[3, 4, 5, 1, 2]
"""

arr = [1, 2, 3, 4, 5]

k = int(input("enter value: "))

for n in range(k):
    first = arr[0]
    for i in range (0, len(arr) - 1):
        arr[i] = arr[i + 1]
    arr[-1] = first
    
print(arr)
