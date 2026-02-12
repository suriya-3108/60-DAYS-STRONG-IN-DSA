"""
Question 11 — Strings

Write a program to:
Check whether a string is a palindrome

Example:

Input: "madam"
Output: Palindrome

Input: "hello"
Output: Not Palindrome
"""

s = input('enter any string values: ')
low = s.lower()

if low == low[::-1]:
    print("palindrome")
else:
    print("not a palindrome")