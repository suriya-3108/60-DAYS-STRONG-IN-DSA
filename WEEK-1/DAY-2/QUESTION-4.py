"""
Question 4 — Lists

Write a program to:
Reverse a list without using reverse() and without using slicing [::-1].

Example:

Input: 1 2 3 4
Output: [4, 3, 2, 1]
"""

num1 = [1,2,3,4]
num2 = []

for i in range (len(num1) - 1, -1, -1):
    num2.append(num1[i])

print(num2)