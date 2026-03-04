"""Problem 3 — Binary Search (Basic — Iterative)
From now on: Array is sorted
Question
Given a sorted list of integers and a target number,
return the index of the target using Binary Search.
If not found, return -1.

Example 1
arr = [10, 20, 30, 40, 50, 60]
target = 40

Output:
3"""

def binary_search(arr, target):
    
    left = 0
    right = len(arr) - 1
    
    while (left <= right):
        middle = (left + right) // 2
        if arr[middle] == target:
            return middle
        
        elif target > arr[middle]:
            left = middle + 1
        
        elif target < arr[middle]:
            right = middle - 1
    return -1


arr = [10, 20, 30, 40, 50, 60]
target = 40
res = binary_search(arr, target)
print(res)