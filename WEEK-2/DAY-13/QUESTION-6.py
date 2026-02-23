"""Problem 6 — Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring that contains no repeating characters.

Example:
s = "abcabcbb"
Output: 3
# Explanation: The longest substring without repeating characters is "abc", length = 3"""

s = 'abcabcbb'

left = 0

length = 0

charset = set()

for right in range(len(s)):
    if s[right] in charset:
        charset.remove(s[left])
        left += 1
        
    charset.add(s[right])
    length = max(length, right - left + 1)
    
print(length)
    





    