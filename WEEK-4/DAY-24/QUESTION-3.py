"""Problem 3 — Insertion Sort
Sort the array using Insertion Sort.

Input
arr = [12, 11, 13, 5, 6]

Expected Output
[5, 6, 11, 12, 13]"""

arr = [12, 11, 13, 5, 6]

for i in range(1,len(arr)):
    current = arr[i]
    j = i - 1
    
    while (j >= 0) and (current < arr[j]):
        arr[j + 1] = arr[j]
        j -= 1
    
    arr[j + 1] = current
    
print(arr)