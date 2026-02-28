"""Problem — Sum of Digits
Problem:
Write a recursive function that calculates the sum of all digits of a given non-negative integer n.

Example 1:
Input: 1234
Output: 10
Explanation: 1 + 2 + 3 + 4 = 10"""

def sum_of_digits(n):
    if n == 0:
        return 0
    while( n > 0):
        a = n % 10
        n = n // 10
        return a + sum_of_digits(n)

print(sum_of_digits(123))
        
        