"""
Question 2 — Functions + Logic

Write a Python program to:

Create a function that checks whether a number is Prime or Not.

Requirements:

1) Use a function
2) Return True/False
3) Don’t use built-in shortcuts
4) Efficient loop logic

Example:
Input: 7
Output: Prime      """

def checkprime(x):
    
    if x <= 1:
        return False
    
    for i in range(x - 1, 1, -1):
        if (x % i == 0):
            return False
            break
    else:
        return True
    
x = int(input("Enter any number: "))
res = checkprime(x)

if res:
    print("Prime")
else:
    print("Not a prime")