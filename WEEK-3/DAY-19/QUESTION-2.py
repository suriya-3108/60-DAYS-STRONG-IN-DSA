"""BACKTRACKING - PERMUTATIONS"""

nums = [1, 2, 3]

def perm(nums):
    result = []
    
    def backtrack(path, nums):
        if not nums:
            result.append(path[:])
            return
        for i in range(len(nums)):
            path.append(nums[i])
            backtrack(path, nums[:i] + nums[i + 1:])
            path.pop()
            
    backtrack([], nums)
    return result    

res = perm(nums)
print(res)