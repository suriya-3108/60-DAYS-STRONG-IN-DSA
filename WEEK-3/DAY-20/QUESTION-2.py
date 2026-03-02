"""Problem 2: Combination Sum"""

candidates = [2,3,6,7]

target = 7

def calc(candidates, target):
    result = []
    
    def backtrack(index, path, total):
        if total == target:
            result.append(path[:])
            return
        
        if total > target:
            return
        
        for i in range(index, len(candidates)):
            path.append(candidates[i])
            backtrack(i, path, total + candidates[i])
            path.pop()
    
    backtrack(0, [], 0)
    return result

res = calc(candidates, target)
print(res)