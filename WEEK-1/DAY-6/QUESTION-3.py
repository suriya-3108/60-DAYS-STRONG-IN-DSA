"""
Problem: Check if Two Strings are Anagrams
Two strings are anagrams if they contain the same characters with same frequency.

Example:
Input: "listen", "silent"
Output: True

Input: "hello", "world"
Output: False

Conditions:
Do NOT use sorted()
Use dictionary
Time complexity O(n)
"""

str_1 = input("enter a string values - 1: ")
str_2 = input("enter a string values - 2: ")
dictionary1 = {}
dictionary2 = {}

if len(str_1) == len(str_2):
    for str in str_1:
        dictionary1[str] = dictionary1.get(str, 0) + 1
    
    for chr in str_2:
        dictionary2[chr] = dictionary2.get(chr, 0) + 1
    
    if dictionary1 == dictionary2:
        print("True")
    else:
        print("False")
        
else:
    print("False")