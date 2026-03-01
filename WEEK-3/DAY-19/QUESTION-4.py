"""BACKTRACKING - COMBINATIONAL SUM"""

nums = [1,2,3]
target = 3

def combination(nums, target):
    result = []
    
    def backtrack(index, path, total):
        if total == target:
            result.append(path[:])
            return
        if total > target:
            return
        
        for i in range (index, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path, total + nums[i]) 
            path.pop()
    backtrack(0, [], 0)
    return result

res = combination(nums, target)
print(res)