"""Problem 1: Combinations (n choose k)"""

n = 4
k = 2

def calc(n, k):
    result = []
    
    def backtrack(index, path):
        if len(path) == k:
            result.append(path[:])
            return
        
        for i in range(index, n + 1):
            path.append(i)
            backtrack(i + 1, path)
            path.pop()
        
    backtrack(1,[])
    return result

res = calc(n,k)
print(res)