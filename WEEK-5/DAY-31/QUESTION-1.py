"""Queue Problem
Number of Recent Calls
Idea:

Store request times in a queue
Remove times older than t − 3000"""

from collections import deque

def solution(number):
    q = deque()
    result = []
    
    for num in number:
        q.append(num)
        
        while q[0] < num - 3000:
            q.popleft()
        
        result.append(len(q))
    
    return result

number = [1, 100, 3001, 3002]
print(solution(number))