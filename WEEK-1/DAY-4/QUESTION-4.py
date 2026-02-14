"""
Question 4 (Flatten a 2D List)

Write a Python program to:
Take a 2D list (list of lists)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Flatten it into a single 1D list using list comprehension

Print the flattened list
Example:

Output:
[1, 2, 3, 4, 5, 6, 7, 8, 9]

Rules:
Use list comprehension
Maintain the order of elements
"""

# Flatten into a single 1D list using list comprehension

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

final_result = [num for row in matrix for num in row]

print(final_result)