"""
Question 9 (Counter – Frequency Counting)

Write a Python program to:
Take a string as input
Count the frequency of each character using Counter from collections
Print the frequency dictionary

Example:

Input:
banana

Output:
Counter({'a': 3, 'n': 2, 'b': 1})

Rules:
Use collections.Counter
Don't write manual counting
Write full code
"""

from collections import Counter

s = 'banana'

count = Counter(s)

print(count)