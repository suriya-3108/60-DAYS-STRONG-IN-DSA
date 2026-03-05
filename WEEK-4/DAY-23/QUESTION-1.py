"""Question 1: First Occurrence of an Element (Binary Search Variation)
Problem
Given a sorted array (ascending order) and a target element, return the index of the first occurrence of the target.
If not found → return -1.

Example 1
Input: arr = [1,2,2,2,3,4,5]
Target = 2
Output: 1"""

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
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


arr = [1,2,2,2,3,4,5]
target = 2
res = binary_search(arr, target)
print(res)