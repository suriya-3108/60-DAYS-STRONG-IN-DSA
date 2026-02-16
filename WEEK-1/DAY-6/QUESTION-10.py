"""
Question 10 (Array + String – Last Problem for Today)
🔹 Problem: Count Vowels in a List of Strings
Given a list of words, count total number of vowels (a, e, i, o, u) in all words combined.

📌 Example:
Input: ["hello", "world", "python"]
Output: 4   # 'e', 'o', 'o' 'o'

Input: ["apple", "banana", "grape"]
Output: 7   # a, e, a, a, a, e

⚡ Conditions:
Use loops only
Do NOT use count() or any advanced string functions
Time complexity → O(n * m) (n = number of words, m = length of word)
"""

val = ["apple", "banana", "grape"]
VOWELS = ['a','e','i','o','u','A','E','I','O','U']
count = 0 

for v in val:
    for s in v:
        if s in VOWELS:
            count += 1

print(count)
