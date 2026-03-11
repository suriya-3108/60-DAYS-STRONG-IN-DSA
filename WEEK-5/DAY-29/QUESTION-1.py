"""Problem 1 — Implement Stack Using List

Create a Stack class using a Python list.

Requirements
Implement these methods:
push(x) → add element to stack
pop() → remove and return top element
peek() → return top element without removing
is_empty() → return True if stack is empty
size() → return number of elements"""

stack = [1,2,3,4]

stack.append(5)

print(f'After element pushed: {stack}')

popped_element = stack.pop()

peek = stack[-1]

if len(stack) == 0:
    is_empty = True
else:
    is_empty = False

print(f'popped element is: {popped_element}')
print(f'peek element: {peek}')
print(f'is_empty: {is_empty}')
print(len(stack)) 