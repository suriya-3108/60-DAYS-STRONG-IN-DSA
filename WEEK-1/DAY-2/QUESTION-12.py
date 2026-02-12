"""
Question 12 — Strings (Slicing)

Write a program to:
Print the first half and second half of a string

Example:

Input: "Python"
Output:
First half: Pyt
Second half: hon
"""

s = input("enter any string value: ")
a = len(s)
d = a // 2

print('First half: ',s[:d])
print('Second half: ',s[d:])