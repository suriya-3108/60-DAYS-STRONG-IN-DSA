"""
Rotate Array Right by k Positions (In-place)
📌 Problem:

Given an array of integers and an integer k, rotate the array to the right by k positions in-place.

Input:
arr = [1, 2, 3, 4, 5]
k = 2

Output:
[4, 5, 1, 2, 3]
"""

arr = list(map(int, input("enter numbers: ").split()))

k = int(input("enter value: "))

for n in range(k):
    last = arr[-1]
    for i in range(len(arr) - 1, -1, -1):
        arr[i] = arr[i - 1]
    arr[0] = last

print(arr)