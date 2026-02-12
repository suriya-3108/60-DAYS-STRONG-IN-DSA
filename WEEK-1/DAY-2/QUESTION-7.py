"""
Question 7 — Lists/Intermediate

Write a program to:
Find the second largest number in a list (without using sort() or max() twice).

Example:
Input: [5, 1, 9, 3, 7]
Output: 7
"""
num = [5,1,9,3,7]

biggest = float("-inf")
smallest = float("-inf")

for i in num:
    if i > biggest:
        smallest = biggest
        biggest = i
    
    if i > smallest and i != biggest:
        smallest = i

print("The Second smallest element: ",smallest)
