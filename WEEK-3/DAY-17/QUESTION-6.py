"""Practice 6 — Fibonacci Sequence (Recursion)
Goal:
Write a recursive function to find the Nth Fibonacci number.

Definition:
F(0) = 0
F(1) = 1
F(n) = F(n-1) + F(n-2)   for n >= 2

Example:
Input: n = 5
Output: 5  (sequence: 0, 1, 1, 2, 3, 5)"""

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

print(fib(5))