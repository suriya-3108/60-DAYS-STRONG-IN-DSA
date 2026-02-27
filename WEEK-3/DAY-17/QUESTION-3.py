"""Practice 3
Write a recursive function to calculate factorial

Definition:
5! = 5 * 4 * 3 * 2 * 1

Example:
If input is 5

Output:
120"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

res = factorial(5)
print(res)