"""Problem 1 — Rotate Array (Without Extra Array)
Given an array and a number k, rotate the array to the right by k steps.

Example:
Input:
arr = [1,2,3,4,5,6,7]
k = 3

Output:
[5,6,7,1,2,3,4]"""

arr = [1,2,3,4,5,6,7]

k = 3

for n in range(k):
    last = arr[-1]
    for i in range(len(arr)-1, -1, -1):
        arr[i] = arr[i - 1]
    arr[0] = last

print(arr)
    