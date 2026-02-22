"""Problem 2: First Non-Repeating Character
📌 Problem Statement

Given a string s, find and print the first character that does not repeat.
If no such character exists, print -1.

Example
Input:  "aabbcddee"
Output: c
"""

# s = input("Enter a string value: ")
# dict1 = {}

# for char in s:
#     dict1[char] = dict1.get(char, 0) + 1

# for keys, values in dict1.items():
#     if values == 1:
#         print(f"first non repeated character: {keys}")
#         break
# else:
#     print("-1")

"""preserve order in dictionary..."""

s = input("Enter a string value: ")
freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

for ch in s:
    if freq[ch] == 1:
        print(ch)
        break
else:
    print("-1")