"""
Question 3 — Lists

Write a program to:
Find the largest element in a list — without using max()

Example:

Input: 3 8 2 10 5
Output: 10
"""

num = list(map(int, input("Enter any numbers: ").split()))
largest = float("-inf")
smallest = float("-inf")

for n in num:
    if n > largest:
        smallest = largest
        largest = n
        
    if n > smallest and n != largest:
        smallest = n
        
print("The largest elements is: ",largest)