"""Problem (Day 29 – Problem 3)

Now try this important stack pattern.

Remove Adjacent Duplicates in String
Problem

Given a string, remove adjacent duplicate characters repeatedly.

Example
Input: "abbaca"
Output: "ca" """

def remove_duplicate(s):
    stack = []
    
    for c in s:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    return ''.join(stack)

s = 'abbaca'
res = remove_duplicate(s)
print(res)