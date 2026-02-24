"""Question 6 (Medium — Mixed Arrays & Strings)

Problem: First Unique Character in a String
Given a string s, find the index of the first non-repeating character.
If it doesn't exist, return -1.

Example 1:
s = "leetcode"
# Output: 0"""

s = "aabb"

freq = {}

for char in s:
    freq[char] = freq.get(char, 0) + 1

for char in s:
    if freq[char] == 1:
        res = s.find(char)
        print(res)
        break
else:
    print("-1")