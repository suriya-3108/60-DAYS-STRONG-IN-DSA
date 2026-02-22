"""Problem 3 (VERY IMPORTANT)
Find All Anagrams in a String
Problem Statement

Given two strings s and p, find all starting indices of p’s anagrams in s.
Example
Input:
s = "cbaebabacd"
p = "abc"

Output:
[0, 6]"""

# s = "abab" 

# p = "ab"

s = "cbaebabacd"
p = "abc"
left = 0
right = len(p) - 1
# total = ''
dict_s = {}
dict_p = {}
output = []

for char2 in p:
    dict_p[char2] = dict_p.get(char2 , 0) + 1

while(right < len(s)):
    total = ''
    for i in range(left, right + 1):
        total += s[i]
    
    for char1 in total:
        dict_s[char1] = dict_s.get(char1, 0) + 1
       
    print(dict_s)
    
    if dict_s == dict_p:
        output.append(left)
        print(dict_p, dict_s)
        
    dict_s.clear()
    left += 1
    right += 1

print(f"Output: {output}")