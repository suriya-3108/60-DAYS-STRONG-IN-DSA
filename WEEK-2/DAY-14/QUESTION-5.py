"""Question 5 (Medium — Strings / Anagram)

Problem: Check if Two Strings are Anagrams
Given two strings s1 and s2, determine if they are anagrams of each other.
Anagrams: same characters with the same frequency, order does not matter.

Example 1:
s1 = "listen"
s2 = "silent"
# Output: True"""

s1 = "listen"

s2 = "silent"

freq1 = {}

freq2 = {}

for char1 in s1:
    freq1[char1] = freq1.get(char1, 0) + 1

for char2 in s2:
    freq2[char2] = freq2.get(char2, 0) + 1
    
if freq1 == freq2:
    print("True")
else:
    print("False")