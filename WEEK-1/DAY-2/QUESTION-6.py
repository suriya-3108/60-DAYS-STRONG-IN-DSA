"""
Question 6 — Lists (Slightly Higher Level)

Write a program to:
Rotate a list to the right by 1 position

Example:

Input: [1, 2, 3, 4]
Output: [4, 1, 2, 3]

Rules:
❌ no slicing shortcut
❌ no built-in rotate functions
✅ use logic + loops
"""

num1 = [1,2,3,4]
num2 = num1[-1]

last = [num2]

right = last + num1[0 : (len(num1) - 1)]
print(right)