"""Problem 3 — Count Subsets (Simple Version)

Given an array of size n,
How many subsets can we form?

Example:

arr = [1,2,3]
Output = 8"""


def calc(n):
    if n == 0:
        return 1
    else:
        return 2 * calc(n - 1)
    
arr = [1, 2]
n = len(arr)

res = calc(n)
print(res)