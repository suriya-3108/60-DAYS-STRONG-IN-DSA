"""
Day 8 Extra Problem 6
Remove All Occurrences of a Given Element (In-place)
📌 Problem:
Given an array of integers and a number val, remove all occurrences of val from the array in-place and return the new array length.

Input:
arr = [3, 2, 2, 3, 4]
val = 2

Output:
[3, 3, 4]
"""

arr = [3, 2, 2, 3, 4]

val = 2

index = 0

for i in range(len(arr)):
    if arr[i] != val:
        arr[index] = arr[i]
        index += 1

print(arr[:index])
