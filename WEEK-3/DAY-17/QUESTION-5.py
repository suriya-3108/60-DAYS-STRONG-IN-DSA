"""Next Practice (Slightly Harder)

Write a recursive function to:

Calculate a^b (a to the power b)

Example:

a = 2, b = 3
Output: 8  (2*2*2)"""

def cal(a, b):
    if b == 0:
        return 1
    else:
        return a * cal(a, b - 1)

print(cal(2, 3))