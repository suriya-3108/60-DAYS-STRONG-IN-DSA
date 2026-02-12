"""
Question 1 — Lists

Write a program to:
Take a list of integers as input and print the sum of all elements (without using sum()).

Example:

Input: 4 7 1 3
Output: 15
"""

a = list(map(int,input("enter any numbers: ").split()))
total = 0
for num in a:
    total += num
    
print("The sum of the list elements are: ",total)