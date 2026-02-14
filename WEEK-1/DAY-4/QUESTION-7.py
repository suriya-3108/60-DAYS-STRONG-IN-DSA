"""
Question 7 (Swap Keys & Values Using Dictionary Comprehension)

Write a Python program to:
Take a dictionary:
original = {'a': 1, 'b': 2, 'c': 3}

Create a new dictionary where keys and values are swapped
Print the new dictionary

Example:
Output:
{1: 'a', 2: 'b', 3: 'c'}

Rules:
Use dictionary comprehension
Don’t use loops outside comprehension
"""

original = {'a': 1, 'b': 2, 'c': 3}

output = {values : keys for keys ,values in original.items()}

print(output)