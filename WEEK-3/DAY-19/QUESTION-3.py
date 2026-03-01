"""BACKTRACKING - COMBINATION OF SIZE K"""

nums = [1,2,3]

def combination(nums, k):
    result = []
    
    def backtrack(index, path):
        if len(path) == k:
            result.append(path[:])
            return
        
        for i in range(index , len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
    
    backtrack(0, [])
    return result

res = combination(nums,2)
print(res)