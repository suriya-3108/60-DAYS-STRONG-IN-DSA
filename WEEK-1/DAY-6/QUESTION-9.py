"""
🔹 Problem: Longest Word in a List of Strings
Given a list of words (strings), find and print the longest word.
If multiple words have the same maximum length, print the first one.

📌 Example:
Input: ["cat", "elephant", "dog", "hippopotamus", "rat"]
Output: "hippopotamus"

Input: ["apple", "banana", "pear", "grape"]
Output: "banana"

⚡ Conditions:
Use loops only
Do NOT use built-in functions like max() or sorted()
Time complexity → O(n)
Space complexity → O(1) extra space
"""

val = ["cat", "elephant", "dog", "hippopotamus", "rat"]
max_length = 0
word = ''

for v in val:
    if len(v) > max_length:
        max_length = len(val)
        word = v

print(word)
