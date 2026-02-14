"""
Question 2 (List Comprehension with Condition)

Write a Python program to:
Create a list of squares of all even numbers from 1 to 20 using list comprehension

Print the list

Example:
Output:
[4, 16, 36, 64, 100, 144, 196, 256, 324, 400]

Rules:
Use list comprehension
Include condition inside comprehension (if)
"""

square_num = [ x ** 2 for x in range(1,21) if x % 2 == 0] 
print(square_num)