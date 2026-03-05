"""BINARY SEARCH - COUNT OCCURENCES"""

# First Occurence
def first_occurence(arr,target):
    left = 0
    right = len(arr) - 1
    result = -1
    
    while (left <= right):
        middle = (left + right) // 2
        
        if arr[middle] == target:
            result = middle
            right = middle - 1
        
        elif arr[middle] < target:
            left = middle + 1
            
        elif arr[middle] > target:
            right = middle - 1
            
    return result

# Second Occurence
def last_occurence(arr,target):
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

# Count Occurence
def count_occurence(arr,target):
    first = first_occurence(arr,target)
    
    if first == -1:
        return 0
    
    last = last_occurence(arr,target)
    
    return last - first + 1

arr = [1,2,2,2,3,4,5]

target = 2

res = count_occurence(arr,target)

print(res)