"""Problem 1 — Sum of First N Natural Numbers
Problem:

Given n, return sum of first n numbers.
Example:

Input: 5
Output: 15"""

def sum_of_numbers(n):
    if n == 0:
        return 0
    else:
        return n + sum_of_numbers(n - 1)

res  = sum_of_numbers(5)
print(res)