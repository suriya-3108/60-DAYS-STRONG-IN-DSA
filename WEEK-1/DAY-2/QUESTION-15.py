"""
Question 15 — Strings (Challenge / Day 2)

Write a program to:
Remove duplicate characters from a string

Example:

Input: "programming"
Output: "progamin"

Keep first occurrence, remove later duplicates.
"""

s = input("enter any string values: ")
res = ''

for char in s:
    if char not in res:
        res += char
        
print(res)