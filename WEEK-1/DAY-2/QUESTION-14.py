"""
Question 14 — Strings (Replacement)

Write a program to:
Replace all vowels in a string with *

Example:

Input: "hello world"
Output: "h*ll* w*rld"
"""

s = 'hello world'
vowels = 'aeiouAEIOU'
result = ''

for char in s:
    if char in vowels:
        result += '*'
    else:
        result += char

print(result)
