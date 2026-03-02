"""Combination Sum II"""

candidates = [10,1,2,7,6,1,5]

target = 8

def calc(candidates, target):
    result = []
    candidates.sort()
    
    def backtrack(index, path, total):
        if total == target:
            result.append(path[:])
            return
        
        if total > target:
            return
        
        for i in range(index, len(candidates)):
            if i > index and candidates[i] == candidates[i - 1]:
                continue
            path.append(candidates[i])
            backtrack(i + 1, path, total + candidates[i])
            path.pop()
    
    backtrack(0, [], 0)
    return result

res = calc(candidates, target)
print(res)