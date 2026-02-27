"""Write a recursive function to:
Print numbers from 1 to N

Example:
If n = 5

Output:
1
2
3
4
5"""

def number_print(n):
    if n == 0:
        return
    number_print(n - 1)
    print(n)

n = int(input("Enter a number: "))
number_print(n)
    