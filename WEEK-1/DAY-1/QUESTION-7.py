"""
Problem 7 — Next Challenge (Loops + Logic)

Check Armstrong Number

1) Write a program to check if a number is an Armstrong number.
2) An Armstrong number = sum of its digits each raised to the power of number of digits equals the number itself.
3) Use loops + math only, no strings.

Example:
Input: 153
Output: Armstrong  # because 1^3 + 5^3 + 3^3 = 153
"""

n = int(input('enter a number: '))
sum = 0
d = n 

while n > 0 :
    last = n % 10
    sum = sum + (last ** 3)
    n = n // 10
    
if sum == d:
    print("armstrong")
else:
    print("not a armstrong")