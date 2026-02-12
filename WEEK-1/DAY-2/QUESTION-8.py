"""
Question 8 — Lists/Intermediate

Write a program to:
Merge two lists and remove duplicates (keep original order).

Example:

List1: [1,2,3]
List2: [2,4,5]
Output: [1,2,3,4,5]
"""

a = [1,2,3]
b = [2,4,5]
c = a + b
d = []
for i in c:
    if  i not in d:
        d.append(i)
print(d)