"""
Problem 10 - Count Number of Digits in a Number

Task:
Write a program to count how many digits a number has using loops only, without converting the number to a string.

Example:

Input: 12345
Output: 5
"""

n = int(input("enter a number: "))
count = 0
if n == 0:
    count = 1

while n > 0:
    n = n // 10
    count += 1
    
print(count)
