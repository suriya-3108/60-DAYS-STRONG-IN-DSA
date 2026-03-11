"""Final Problem for Day 29 (Very Important)

This problem prepares you for Day 30 – Next Greater Element.
Problem 4 — Baseball Game (Stack Simulation)
You are given operations in a list.

Rules:
Operation	Meaning
number	push score
"+"	sum of last two scores
"D"	double last score
"C"	remove last score
Example

Input
["5","2","C","D","+"]

Process

5 → push → [5]
2 → push → [5,2]
C → remove last → [5]
D → double last → [5,10]
+ → sum last two → [5,10,15]

Final score
5 + 10 + 15 = 30

Output
30"""

def solution(stack):
    arr = []
    for i in range(len(stack)):
        if stack[i].isdigit():
            arr.append(int(stack[i]))
        
        elif stack[i] == 'C':
            arr.pop()
                
        elif stack[i] == 'D':
            arr.append(arr[-1] * 2)
        
        elif stack[i] == '+':
            stack.append(stack[-1] + stack[-2])
    return sum(arr)

stack = ["5","2","C","D","+"]
print(solution(stack))