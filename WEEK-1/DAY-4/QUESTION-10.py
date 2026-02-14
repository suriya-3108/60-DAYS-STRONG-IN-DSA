"""
Question 10 (defaultdict – Grouping Data)

Write a Python program to:
Take a list of words:
words = ["apple", "banana", "avocado", "berry", "apricot"]

Group the words by their first letter using defaultdict
Print the grouped dictionary

Example:

Output:
{'a': ['apple', 'avocado', 'apricot'], 'b': ['banana', 'berry']}

Rules:
Use collections.defaultdict
Don’t use normal dict + manual key checks
Write full code
"""

from collections import defaultdict

words = ["apple", "banana", "avocado", "berry", "apricot"]

dictionary = defaultdict(list)

for word in words:
    first_letter = word[0]
    dictionary[first_letter].append(word)
    
print(dict(dictionary))