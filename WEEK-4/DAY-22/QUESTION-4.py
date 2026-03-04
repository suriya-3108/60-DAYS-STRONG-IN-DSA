"""Problem 4 — First Occurrence Using Binary Search
Given a sorted array with duplicates,
return the first occurrence of target.
Example:
arr = [5, 7, 7, 8, 8, 8, 10]
target = 8

Output:
3"""

def binary_search(arr, target):
    
    left = 0
    right = len(arr) -1
    result = -1
    
    while (left <= right):
        
        middle = (left + right) // 2
        if arr[middle] == target:
            result = middle
            right = middle - 1
        
        elif target > arr[middle]:
            left = middle + 1
        
        elif target < arr[middle]:
            right = middle - 1
    return result

arr = [5, 7, 7, 8, 8, 8, 10]
target = 8
res = binary_search(arr, target)
print(res)  