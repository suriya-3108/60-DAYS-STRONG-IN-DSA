"""
Question 4 — Number Logic (DSA Foundation)

Write a program to:
Reverse a number without converting it to string

Requirements:

1) Use loop
2) Use math operations only
3) Make it inside a function

Example:
Input: 1234
Output: 4321

"""
def reverse_number(n):
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n = n // 10
    return rev

num = int(input("Enter a number: "))
print(reverse_number(num))
