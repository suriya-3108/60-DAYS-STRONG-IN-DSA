"""
Question 5 (Array – Slightly Logical)
🔹 Problem: Find All Duplicates in a List

Given a list of integers, print all elements that appear more than once.
📌 Example:
Input: [1,2,3,1,3,6,6]
Output: 1 3 6

If no duplicates exist, print:
None

⚡ Conditions:

Use dictionary (Day 3 knowledge allowed)
Do NOT use set directly to solve
Time complexity → O(n)
Do not print duplicate twice
"""

Input = [1,2,3,1,3,6,6]
dictionary = {}

for i in Input:
    dictionary[i] = dictionary.get(i, 0) + 1

for keys, values in dictionary.items():
    if values > 1:
        print(keys,end=' ')