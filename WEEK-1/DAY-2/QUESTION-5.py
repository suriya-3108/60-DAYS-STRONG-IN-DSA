"""
Question 5 — Lists

Write a program to:
Remove duplicate elements from a list (keep original order).

Example:

Input: [1, 2, 2, 3, 1, 4]
Output: [1, 2, 3, 4]

Constraint:
❌ don't use set() shortcut
✅ use loop + logic
"""

num1 = [1,2,2,3,1,4]
num2 = []

for n in num1:
    if n not in num2:
        num2.append(n)
        
print("The Duplicate removed List: ",num2)