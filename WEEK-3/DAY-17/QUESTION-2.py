"""Practice 2
Now write a recursive function to:
Print numbers from N to 1

Example:
If n = 5

Output:
5
4
3
2
1"""

def print_number(n):
    if n == 0:
        return
    print(n)
    print_number(n - 1)
    print(n)

print_number(5)