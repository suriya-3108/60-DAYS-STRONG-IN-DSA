"""
Question 1 — Two Sum (Sorted Array)

Given a sorted array of integers and a target value,
return the indices (0-based) of the two numbers such that they add up to the target.

You must:
Use two pointer technique
Use O(1) extra space
Time complexity should be O(n)

Example 1:
Input:
arr = [1, 2, 3, 4, 6]
target = 6

Output:
[1, 3]

Explanation:
2 + 4 = 6
"""

def find_sum(target,arr):
    left = 0

    right = len(arr) - 1
    
    
    while (left < right):
        target_total = arr[left] + arr[right]
    
        if target_total == target:
            return [left , right]
        elif target_total < target:
            left += 1
        elif target_total > target:
            right -= 1
    return [-1,-1]

arr = [1, 2, 3, 4, 6]
target = 6

res = find_sum(target,arr)
print(res)
