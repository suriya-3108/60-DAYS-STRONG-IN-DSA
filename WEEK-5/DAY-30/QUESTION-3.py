"""Problem 2: Daily Temperatures (Stack Pattern)

You are given temperatures for each day.
For every day, find how many days you must wait until a warmer temperature.
If no warmer temperature exists → 0.

Example
Input:
[73,74,75,71,69,72,76,73]

Output:
[1,1,4,2,1,1,0,0]"""

def solution(arr):
    stack = []
    result = [0] * len(arr)
    
    for i in range(len(arr)):
        while stack and arr[i] > arr[stack[-1]]:
            prev_day = stack.pop()
            result[prev_day] = i - prev_day
        stack.append(i)
        
    return result

arr = [73,74,75,71,69,72,76,73]
print(solution(arr))