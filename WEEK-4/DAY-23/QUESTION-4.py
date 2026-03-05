"""Next Level (Now It Gets Interesting)
Let’s increase difficulty.
Next Question: Lower Bound

Problem:
Return the index of the first element greater than or equal to target.

Example:
arr = [1,2,4,6,8]
target = 5
Output = 3  (because 6 is first >= 5)
If target is bigger than all elements → return len(arr)"""

def binary_search(arr,target):
    
    left = 0
    right = len(arr) - 1
    result = len(arr)
    
    while (left <= right):
        middle = (left + right) // 2
        if arr[middle] >= target:
            result = middle
            right = middle - 1
        else:
            left = middle + 1
    return result

arr = [1,2,4,6,8]
target = 5
res = binary_search(arr,target)
print(res)