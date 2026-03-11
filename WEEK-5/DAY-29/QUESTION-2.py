"""Problem 2 — Valid Parentheses (Very Important)

This is one of the most common stack interview problems.

Problem

Given a string containing only:
( ) { } [ ]
Return True if the brackets are valid."""

def is_valid(s):
    dictionary = {')': '(', '}': '{', ']':'['}
    stack = []
    
    for char in s:
        if char in '({[':
            stack.append(char)
        
        elif char in ')}]':
            if not stack:
                return False
            if stack.pop() != dictionary[char]:
                return False
    return False if stack else True

s = '(]'
res = is_valid(s)
print(res)