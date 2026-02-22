"""
Problem 5: Longest Substring Without Repeating Characters
Example
Input: "abcabcbb"
Output: 3  # "abc"

This combines:
Strings
Sliding window
Frequency / set logic
"""


input = "abcabcbb"

left = 0

length = 0

charset = set()

for right in range (len(input)):
    if input[right] in charset:
        charset.remove(input[left])
        left += 1
        
    charset.add(input[right])
    length = max(length, right - left + 1)
    
print(length)

