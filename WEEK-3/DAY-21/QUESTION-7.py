"""Next Step: Combination Problems
Problem 7 (Combination Sum)

Given candidates = [2,3,6,7] and target = 7, return all unique combinations where candidate numbers sum to target.
You can use a candidate multiple times
Numbers in combination should be in non-descending order

Example:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]"""

def calc(nums, target):
    result = []
    
    def backtrack(index, path, total):
        if total == target:
            result.append(path[:])
            return
        if total > target:
            return
        
        for i in range(index, len(nums)):
            path.append(nums[i])
            backtrack(i, path, total + nums[i])
            path.pop()
    
    backtrack(0, [], 0)
    return result

nums = [2,3,6,7]
target = 7
res = calc(nums, target)
print(res)