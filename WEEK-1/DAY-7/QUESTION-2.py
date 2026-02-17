"""
Question 2: Check Even or Odd (Using Function)
Task:
Write a Python function is_even(n) that returns True if n is even, otherwise False. Then, take an integer input from the user and print "Even" or "Odd" based on the function result.

Sample Input:
Enter a number: 10

Sample Output:
Even
"""

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

n = int(input("enter a number: "))
res = is_even(n)

if res:
    print("Even")
else:
    print("Odd")