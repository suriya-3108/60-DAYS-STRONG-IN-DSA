"""
Question 2 — Lists

Write a program to:
Count how many even numbers and how many odd numbers are in a list.

Example:

Input: 1 2 3 4 5 6
Output:
Even = 3
Odd = 3
"""

num = list(map(int, input("Enter any numbers: ").split()))
even_counter = 0
odd_counter = 0

for n in num:
    if (n % 2 == 0):
        even_counter += 1
    else:
        odd_counter += 1

print("The Even count is: ",even_counter, "The Odd counter is: ",odd_counter)