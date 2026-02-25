"""Practice Question 4 (IMPORTANT)
Problem:
Given two lists, find the common elements.

Input
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
Output"""

a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

seen = set(a)
common = []

for x in b:
    if x in seen:
        common.append(x)

print(common)