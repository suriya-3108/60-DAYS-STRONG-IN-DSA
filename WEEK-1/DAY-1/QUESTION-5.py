"""Question 5 — Basic Logic + Functions

Write a program that prints the factorial of a number using a function.

Requirements:

1) Use a function factorial(n)
2) Use loop inside the function
3) Don’t use math.factorial

Example:
Input: 5
Output: 120       """

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

n = int(input('enter a number: '))
res = factorial(n)
print(res)