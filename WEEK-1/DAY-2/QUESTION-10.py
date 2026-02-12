"""
Question 10 — Strings (Basics)

Write a program to:
Count vowels and consonants in a string

Example:

Input: "hello world"
Output:
Vowels = 3
Consonants = 7
"""

s = input("enter any value: ")
b = s.split()
c = ''.join(b)
vowels = 0
consonants = 0
VOWELS =  ['A','E','I','O','U','a','e','i','o','u']
for char in c:
    if char in VOWELS:
        vowels += 1
    else:
        consonants += 1
        
print("Vowels: ",vowels)
print("Consonats: ",consonants)