"""
Question 3 (List Comprehension with if-else)

Write a Python program to:
Take numbers from 1 to 10
Create a new list where:
Even numbers are squared
Odd numbers are cubed

Print the new list
Example:

Output:
[1, 4, 27, 16, 125, 36, 343, 64, 729, 100]

Rules:
Use list comprehension
Include if-else inside comprehension
"""

new_list = [x ** 2 if x % 2 == 0 else x ** 3 for x in range(1,11)]
print(new_list)