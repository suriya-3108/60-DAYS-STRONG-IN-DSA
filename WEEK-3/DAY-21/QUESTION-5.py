"""Revision Problem 5 (Backtracking – Subsets)
Problem: Generate All Subsets

Given a list of integers nums, return all possible subsets (the power set).
Example:
Input:
nums = [1, 2, 3]

Output:
[
 [],
 [1],
 [2],
 [3],
 [1,2],
 [1,3],
 [2,3],
 [1,2,3]
]
⚠ Rules:
Must use backtracking
No built-in subset functions
Think in include/exclude pattern"""

def calculation(nums):
    result = []
    
    def backtrack(index, path):
        result.append(path[:])
        
        for i in range(index, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
        
    backtrack(0, [])
    return result 

nums = [1, 2, 3]
res = calculation(nums)
print(res)

