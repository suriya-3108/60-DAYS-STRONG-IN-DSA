"""Question 1 — Basic Logic + Loops

Write a Python program to:

Print all numbers from 1 to N that are divisible by both 3 and 5.

Requirements:

1) Take N as input
2) Use loop
3) Use condition check
4) Print each valid number on a new line

Example:

Input:
50

Output:
15
30
45    """       

N = int(input('enter any number: '))

for i in range(1, N + 1):
    if (i % 3 == 0 and i % 5 == 0):
        print('The Numbers divided by 3 and 5 are: ',i)
