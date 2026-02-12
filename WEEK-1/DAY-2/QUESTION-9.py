"""
Question 9 — Lists/Intermediate

Write a program to:
Count the frequency of each element in a list

Example:

Input: [1,2,2,3,1,4]
Output:
1: 2
2: 2
3: 1
4: 1
"""

n = [1,2,2,3,1,4]

a = []

for num in n:
    if num not in a:
        count = 0
        for x in n:
            if num == x:
                count += 1
                
        print(num,':', count)
        a.append(num)
