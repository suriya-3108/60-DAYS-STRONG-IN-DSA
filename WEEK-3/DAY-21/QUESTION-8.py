"""Problem 8 (Combination Problems – Subset Sum)
Given nums = [2,3,5] and target = 8, return all combinations of numbers (each number used at most once) that sum to the target.
Example:

Input: [2,3,5], target = 8
Output: [[3,5], [2,3,3]]  (if repetitions allowed) OR [[3,5]] if each used once"""

def calculate(nums, target):
    result = []
    
    def backtrack(index, path, total):
        if total == target:
            result.append(path[:])
            return
        
        if total > target:
            return 
        
        for i in range(index, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path, total + nums[i])
            path.pop()
            
    backtrack(0, [], 0)
    return result

nums = [2,3,5]
target = 8
res = calculate(nums, target)
print(res)