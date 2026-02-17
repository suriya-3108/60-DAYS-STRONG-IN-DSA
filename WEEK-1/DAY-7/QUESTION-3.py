"""
Question 3: Maximum in a List
Task:
Write a program to find the maximum number in a list without using the built-in max() function.

Sample Input:
Enter numbers: 4 7 1 9 2

Sample Output:
Maximum number is: 9
"""

num = list(map(int,input("enter any numbers: ").split()))

max_number = float("-inf")

for n in num:
    if n > max_number:
        max_number = n

print(max_number)