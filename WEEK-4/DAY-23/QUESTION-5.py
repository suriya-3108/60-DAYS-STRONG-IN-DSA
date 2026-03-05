"""Problem: Upper Bound
Definition
Find the first index of an element strictly greater than the target.

Example:
arr = [1, 2, 4, 6, 8]
target = 4"""

def binary_search(arr,target):
    left = 0 
    right = len(arr) - 1
    result = len(arr)
    
    while (left <= right):
        middle = (left + right) // 2
        if arr[middle] > target:
            result = middle
            right = middle - 1
        else: 
            left = middle + 1
    
    return result

arr = [1, 2, 4, 6, 8]
target = 4
res = binary_search(arr,target)
print(res)