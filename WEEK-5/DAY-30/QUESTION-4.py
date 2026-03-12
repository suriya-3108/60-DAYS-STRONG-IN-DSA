"""Problem 3: Next Greater Element II (Circular Array)

You are given a circular array.
That means after the last element, the array continues from the beginning.
For each element, find the next greater element.
If none exists → return -1.

Example
Input
nums = [1,2,1]

Output
[2,-1,2]"""

def solution(arr):
    n = len(arr)
    stack = []
    result = [-1] * n
    
    for i in range(2 * n):
        while stack and arr[i % n] > arr[stack[-1]]:
            index = stack.pop()
            result[index] = arr[i % n]
        
        if i < n:
            stack.append(i)
        
    return result


nums = [1,2,1]
print(solution(nums))