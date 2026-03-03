"""Next Level (Recursion Pattern)
Problem 4:
Write a recursive function to compute:
Power of X
Compute x^n using recursion.

Example:
Input: x = 2, n = 5
Output: 32"""

def calculation(x, n):
    if n == 0:
        return 1
    
    power = calculation(x, n // 2)
    
    if n % 2 == 0:
        return power * power
    else:
        return x * power * power
    
x = 2
n = 5
res = calculation(x, n)
print(res)
    