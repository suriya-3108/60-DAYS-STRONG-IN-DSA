"""
Question 8 (Filter Dictionary Based on Value)

Write a Python program to:
Take a dictionary:
scores = {'Alice': 85, 'Bob': 42, 'Charlie': 90, 'David': 65}
Create a new dictionary containing only those items where the value is greater than 50

Print the new dictionary

Example:
Output:
{'Alice': 85, 'Charlie': 90, 'David': 65}

Rules:
Use dictionary comprehension
Include condition inside comprehension
"""

scores = {'Alice': 85, 'Bob': 42, 'Charlie': 90, 'David': 65}

result = {keys : values for keys,values in scores.items() if values > 50}

print(result)