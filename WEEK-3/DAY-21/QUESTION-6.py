"""Revision Problem 6 (Backtracking – Permutations)
Problem:
Given nums = [1,2,3], return all permutations.

Output:
[
 [1,2,3],
 [1,3,2],
 [2,1,3],
 [2,3,1],
 [3,1,2],
 [3,2,1]
]"""

def calc(nums):
    result = []
    
    def backtrack(path, nums):
        if not nums:
            result.append(path[:])
            return
        
        for i in range(len(nums)):
            path.append(nums[i])
            backtrack(path, nums[:i] + nums[i + 1:])
            path.pop()
    
    backtrack([],nums)
    return result

nums = [1,2,3]
res = calc(nums)
print(res)