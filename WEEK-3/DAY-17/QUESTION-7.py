"""Practice: Sum of Digits of a Number
Task:
Write a recursive function that calculates the sum of all digits of a number.

Example:
Input: 1234
Output: 10   # 1 + 2 + 3 + 4"""
 
def cal(n):
    if n <= 0:
        return 0
    else:
        a = n % 10
        n = n // 10
        return a + cal(n) 

print(cal(1234))
    