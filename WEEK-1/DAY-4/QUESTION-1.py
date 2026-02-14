"""
Question 1 (Warm-up: Dictionary Frequency)

Write a Python program to:

Take a string as input
Count frequency of each character
Store the result in a dictionary
Print the dictionary

Example

Input:
banana

Output:
{'b': 1, 'a': 3, 'n': 2}

Rules:
Use a dictionary
Don’t use built-in Counter
Write full code
"""

# s = input("enter a string: ")
# dictionary = {}
# a =[]

# for str in s:
#     if str not in a:
#         count = 0
#         for chr in s:
#             if str == chr:
#                 count += 1
#         dictionary[str] = count
#         a.append(str)

# print(dictionary)

s = input("enter any string: ")
dictionary = {}

for str in s:
    dictionary[str] = dictionary.get(str, 0) + 1

print(dictionary)