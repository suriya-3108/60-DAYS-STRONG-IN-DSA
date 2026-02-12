"""
Question 13 — Strings (Slicing / Characters)

Write a program to:
Swap the first and last character of a string

Example:

Input: "hello"
Output: "oellh"
"""

s = input("enter any string value: ")
o = ''

last = s[-1]
first = s[0]

o = last + s[1:(len(s)-1)] + first

print(o)