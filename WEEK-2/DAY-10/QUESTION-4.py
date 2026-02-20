"""
Problem 4 — Longest Substring Without Repeating Characters
Given:

s = "abcabcbb"
Return length of longest substring without repeating characters.

Expected Output:
3

Explanation:
"abc"
"""

s = "abcabcbb"

left = 0

charset = set()

length = 0

for right in range(len(s)):
    if s[right] in charset:
        charset.remove(s[left])
        left +=1
    
    charset.add(s[right])
    length= max(length , right - left + 1) 
    
print(length)