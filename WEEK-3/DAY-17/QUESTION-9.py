"""Practice: Print All Even Numbers from N to 1 Recursively
Task:

Write a recursive function that prints all even numbers from N down to 1.
Example:

Input: 6
Output: 6 4 2"""

def num(n):
    if n == 0:
        return
    else:
        if n % 2 == 0:
            print(n, end=" ")
        num(n - 1)

n = 6
num(n)