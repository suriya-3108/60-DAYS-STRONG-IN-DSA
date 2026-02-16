"""
Question 2 (Easy – String)
🔹 Problem: First Non-Repeating Character

Write a function that returns the first non-repeating character in a string.
If all characters repeat, return None.

📌 Example:
Input: "leetcode"
Output: "l"

Input: "aabbcc"
Output: None

⚡ Conditions:
Do NOT use collections module
Do NOT use advanced Python tricks
You can use loops and dictionary (Day 3 knowledge)
Time complexity should be O(n)
"""

s = input("enter a string values: ")
dictionary = {}

for str in s:
    dictionary[str] = dictionary.get(str, 0) + 1

for values in dictionary.values():
    if values == 1:
        print("1")
        break
else:
    print("None")
