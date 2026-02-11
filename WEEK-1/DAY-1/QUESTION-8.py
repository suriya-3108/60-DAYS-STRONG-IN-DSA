"""
Problem 8 — Next Basic DSA Logic

1) Print the Fibonacci sequence up to N terms
2) Use loops only, no recursion
3) Use variables to track last two numbers

Example:
Input: 7
Output: 0 1 1 2 3 5 8
"""

n = int(input('enter a number: '))

a = 0 
b = 1

for i in range(n):
    print(a,end= " ")
    c = a + b
    a = b
    b = c
     