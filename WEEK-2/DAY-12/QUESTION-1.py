"""
Problem 1: Check if Two Strings Are Anagrams
📌 Problem Statement

Given two strings s and t, write a program to check whether they are anagrams of each other.
Two strings are anagrams if:
They have the same length
They contain the same characters with the same frequency

Example
Input:
s = "listen"
t = "silent"

Output:
True
"""

s = input("Enter value - 1:").lower()
t = input("Enter value - 2:").lower()

dict1 = {}
dict2 = {}

for char1 in s:
    dict1[char1] = dict1.get(char1, 0) + 1 

for char2 in t:
    dict2[char2] = dict2.get(char2, 0) + 1 
    
if dict1 == dict2:
    print("True")
else:
    print("False")