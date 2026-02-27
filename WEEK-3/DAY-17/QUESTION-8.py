"""Practice: Count Occurrences of a Digit in a Number (Recursion)
Task:

Write a recursive function that counts how many times a specific digit appears in a number.

Example:
Input: number = 1223, digit = 2
Output: 2   # because '2' appears twice"""

def cal(number, digit):
    if number == 0:
        return 0
    else:
        a = number % 10
        if a == digit:
            return 1 + cal(number // 10, digit)
        else:
            return cal(number // 10, digit)

number = 1223
digit = 2
print(cal(number, digit)) 