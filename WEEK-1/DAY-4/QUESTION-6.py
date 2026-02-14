"""
Question 6 (Dictionary Comprehension with Condition)

Write a Python program to:
Take numbers from 1 to 10
Create a dictionary where:
Key = number
Value = square of the number
Include only even numbers in the dictionary

Print the dictionary
Example:

Output:
{2: 4, 4: 16, 6: 36, 8: 64, 10: 100}

Rules:
Use dictionary comprehension
Include condition inside comprehension (if)
"""

dictionary = {i : i *i for i in range(1,11) if i % 2 == 0}
print(dictionary)