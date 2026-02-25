"""FINAL PRACTICE (Day 15 boss question)
Problem:
Group the anagrams together.

Input
strs = ["eat","tea","tan","ate","nat","bat"]
Output
[["eat","tea","ate"], ["tan","nat"], ["bat"]]"""

strs = ["eat","tea","tan","ate","nat","bat"]

groups = {}

for word in strs:
    key = ''.join(sorted(word))
    
    if key not in groups:
        groups[key] = []
    
    groups[key].append(word)

print(list(groups.values()))     # [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]