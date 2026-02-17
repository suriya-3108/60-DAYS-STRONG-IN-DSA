"""
Question 1: Sum of Numbers
Write a Python program that takes a list of integers and returns the sum of all numbers in the list.
Example:
Input: [1, 2, 3, 4]
Output: 10
"""

num = list(map(int,input("enter any numbers: ").split()))

total = 0

for n in num:
    total += n

print("The Total is: ",total)