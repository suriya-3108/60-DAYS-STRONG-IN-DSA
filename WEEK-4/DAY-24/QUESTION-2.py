"""Next Question (Day 24 — Question 2)
Now let's solve Selection Sort.
Problem
Sort the array using Selection Sort.

Input
arr = [64, 25, 12, 22, 11]

Expected Output
[11, 12, 22, 25, 64]"""

arr = [64, 25, 12, 22, 11]

for pos in range(len(arr)):
    min = pos
    for i in range(pos + 1, len(arr)):
        if arr[i] < arr[min]:
            min = i
    arr[min], arr[pos] = arr[pos], arr[min]
    
print(arr)