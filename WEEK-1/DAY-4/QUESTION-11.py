"""Question 11 (Deque – Queue Implementation)

Write a Python program to:
Create a deque

Add elements to both ends
Remove elements from both ends
Print the deque after each operation

Example Steps:

Start with an empty deque
Add 1 to the right
Add 2 to the left
Add 3 to the right
Remove one element from left
Remove one element from right

Expected output sequence:

After adding 1 to right: deque([1])
After adding 2 to left: deque([2, 1])
After adding 3 to right: deque([2, 1, 3])
After removing from left: deque([1, 3])
After removing from right: deque([1])

Rules:
Use collections.deque
Practice append, appendleft, pop, popleft
"""

from collections import deque

arr = deque()

arr.append(1)
arr.appendleft(2)
arr.append(3)
arr.popleft()
arr.pop()

print(arr)