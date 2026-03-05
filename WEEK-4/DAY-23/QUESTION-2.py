"""BINARY SEARCH - LAST OCCURENCE"""

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    result = -1
    
    while (left <= right):
        middle = (left + right) // 2
        
        if arr[middle] == target:
            result = middle
            left = middle + 1
        
        elif arr[middle] < target:
            left = middle + 1
            
        elif arr[middle] > target:
            right = middle - 1
    
    return result

arr = [1,2,2,2,3,4,5]
target = 2
res = binary_search(arr, target)
print(res)