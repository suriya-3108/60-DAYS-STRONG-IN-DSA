"""Problem 2 — Fibonacci Number
Problem:

Return nth Fibonacci number.
Fibonacci definition:
fib(0) = 0
fib(1) = 1
fib(n) = fib(n-1) + fib(n-2)

Example:
Input: 5
Output: 5"""

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

print(fib(5))