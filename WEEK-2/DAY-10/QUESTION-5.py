"""
Problem 5 — Longest Substring with At Most K Distinct Characters
Given:
s = "eceba"
k = 2

Return the length of the longest substring that contains at most k distinct characters.
Expected Output:
3
Explanation:
"ece" → length 3 (only 2 distinct characters: e, c)
"""

s = "eceba"
k = 2
charset = set()
left = 0
length = 0

for right in range(len(s)):
    charset.add(s[right])
    
    if len(charset) > k:
        charset.discard(s[left])
        left += 1
        
    length = max(length , right - left + 1)
    
print(length)

        