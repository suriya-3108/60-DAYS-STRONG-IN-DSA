"""
Question 5 (Nested 2D List Transformation)

Write a Python program to:
Take a 2D list (matrix):
matrix = [[1, 2], [3, 4], [5, 6]]

Create a new 2D list where each number is multiplied by 2
Keep the 2D structure

Print the new 2D list
Example:

Output:
[[2, 4], [6, 8], [10, 12]]

Rules:
Use nested list comprehension
Maintain row structure
"""

# new 2D list where each number is multiplied by 2

matrix = [[1, 2], [3, 4], [5, 6]]

final_res = [[ j * 2 for j in i ]for i in matrix]

print(final_res)