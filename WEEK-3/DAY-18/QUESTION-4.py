"""Problem 4 — Power of X (Fast Exponentiation Thinking)
Instead of:
x^n = x * x * x * x * x (n times)

We think:
x^n = (x^(n/2)) * (x^(n/2))

This reduces time.
Your Problem for Day 18

Write recursive function:
power(x, n)

Example:
power(2, 5) → 32"""

# def calc(a, b):
#     if b == 0:
#         return 1
#     else:
#         return a * calc(a, b - 1)

# res = calc(2, 5)
# print(res)

def calc(a, b):
    if b == 0:
        return 1
    
    half = calc(a, b//2)
    
    if b % 2 == 0:
        return half * half
    else:
        return a * half * half

print(calc(2,4))