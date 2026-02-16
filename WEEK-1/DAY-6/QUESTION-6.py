"""
Question 6 (Array & String – Slightly Tricky)
🔹 Problem: Count Frequency of Each Character in a String
Given a string, print each character and its frequency in order of first appearance.

📌 Example:
Input: "programming"
Output:
p 1
r 2
o 1
g 2
a 1
m 2
i 1
n 1

⚡ Conditions:
Do NOT use collections.Counter or advanced modules
Use loops and dictionaries only
Maintain first occurrence order
Time complexity → O(n)
"""
s  = input("Enter a string value: ")
dictionary = {}

for str in s:
    dictionary[str] = dictionary.get(str, 0) + 1

for keys ,values in dictionary.items():
    print(keys,values)