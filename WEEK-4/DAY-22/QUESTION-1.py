"""Problem 1 — Linear Search (Basic)
Question:
Given a list of integers and a target number,
return the index of the target if it exists.
If it does not exist, return -1.

Example:
Input:
arr = [10, 25, 30, 45, 50]
target = 30

Output:
2"""

def linear_search(arr,target):
    
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    
    return -1


arr = [10, 25, 30, 45, 50]
target = 30
res  = linear_search(arr,target)
print(res)