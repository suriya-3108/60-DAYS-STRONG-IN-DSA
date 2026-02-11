""" Problem 6 — Sum of Digits

Write a program to find the sum of all digits of a number using a loop (no strings).

Requirements:

1) Use a loop
2) Take input from user
3) Use only math operations

Example:
Input: 1234
Output: 10   # because 1+2+3+4=10     """

n = 1234
sum = 0
while n > 0:
    last = n % 10
    sum = sum + last
    n = n // 10

print(sum)