"""Write a recursive function to:

Find the sum of first N numbers

Example:
If n = 5

5 + 4 + 3 + 2 + 1 = 15"""

def sum_number(n):
    if n == 0:
        return 0
    else:
        return n + sum_number(n - 1)

print(sum_number(5))