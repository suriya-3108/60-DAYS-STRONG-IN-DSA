"""
Problem 9 — Sum of Even and Odd Digits

Write a program to separately calculate the sum of even digits and odd digits of a number.

Example:
Input: 1234
Output:
Sum of even digits = 6  (2 + 4)
Sum of odd digits  = 4  (1 + 3)
"""

n = int(input("enter a number: "))

even = 0
odd = 0

while n > 0:
    last = n % 10
    if last % 2 == 0:
        even = even + last
    else:
        odd = odd + last
    n = n // 10
    
print('even: ',even, 'odd: ',odd)