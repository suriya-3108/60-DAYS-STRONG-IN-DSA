"""
Question 2 (Dictionary + Condition)

Write a program to:
👉 Take a list of numbers
👉 Print the number that appears maximum times
👉 Use dictionary frequency counting

Example
Input:

[1,2,2,3,1,2,4]

Output:
2
"""

num = list(map(int, input("enter numbers: ").split()))
a = []
dictionary = {}

for n in num:
    if n not in a:
        count = 0
        for m in num:
            if n == m:
                count += 1
        dictionary[n] = count
        a.append(n)

max_count = float("-inf")
min_count = float("-inf")

for key, value in dictionary.items():
    if value > max_count:
        min_count = max_count
        max_count = key
        
    if value > min_count and value != max_count:
        min_count = key

print(max_count)