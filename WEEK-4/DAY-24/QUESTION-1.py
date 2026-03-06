"""Problem 1 — Implement Bubble Sort
Problem
Write a function to sort an array using Bubble Sort.

Example
Input
arr = [5, 1, 4, 2, 8]

Output
[1, 2, 4, 5, 8]"""

arr = [5, 1, 4, 2, 8]

for i in range(0 ,len(arr) - 1):
    for j in range(0, len(arr) - 1):
        if arr[j] > arr[j + 1]:
            arr[j] , arr[j + 1] = arr[j + 1] , arr[j]
        
print(arr)