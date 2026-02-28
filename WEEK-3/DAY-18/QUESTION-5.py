"""Problem — Count Ways to Reach Top
Problem:
You have a staircase with n steps. You can climb 1 step or 2 steps at a time.
Write a recursive function to count how many different ways you can reach the top.

Example 1:

Input: n = 3
Output: 3

Explanation: 
Ways to climb 3 steps:
1. 1 + 1 + 1
2. 1 + 2
3. 2 + 1"""

def calc(n):
    if n == 0:
        return 1
    if n < 0:
        return 0
    return calc(n - 1) + calc(n - 2)

print(calc(5))