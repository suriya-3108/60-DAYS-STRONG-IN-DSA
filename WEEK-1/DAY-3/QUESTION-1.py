"""
Question 1 (Warm-up: Dictionary Frequency)

Write a Python program to:
👉 Take a string as input
👉 Count frequency of each character
👉 Store result in a dictionary
👉 Print the dictionary

Example

Input:
banana

Output:
{'b':1, 'a':3, 'n':2}

Rules:
Use dictionary
Don’t use built-in Counter
Write full code
"""

s = input("enter a value: ")
a = []
b = {}

for i in s:
    if i not in a:
        count = 0
        for j in s:
            if i == j:
                count += 1
        b[i] = count
        a.append(i)
print(b) 