"""Next Level (Recursion Revision)
Problem 3:
Write a recursive function to return the sum of digits of a number.
Example:

Input: 1234
Output: 10"""

def calculate(n):
    if n == 0:
        return 0
    else:
        a = n % 10
        n = n // 10
        return a + calculate(n)
    
n = 1234
res = calculate(n)
print(res)