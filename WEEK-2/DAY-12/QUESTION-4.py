"""
Valid Palindrome Permutation
📌 Problem Statement

Given a string s, determine whether any permutation of the string can form a palindrome.

Return:
True → if it can form a palindrome
False → if it cannot
"""

s = 'aabbcccd'
dict1 = {}
finding = []

for char in s:
    dict1[char] = dict1.get(char, 0) + 1

for char in s:
    if dict1[char] % 2 != 0:
        finding.append(char)

if len(finding) >= 2:
    print("False")
else:
    print("True")        
    