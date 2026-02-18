"""
Question 3 (Important Interview Question)
Move All Zeros to End (In-place)
Input:
[0, 1, 0, 3, 12]

Output:
[1, 3, 12, 0, 0]

Rules:
Maintain order of non-zero elements
No extra array
O(n) time
O(1) space
"""

lst = list(map(int, input("enter nmubers: ").split()))

counter = 0

for l in range(0, len(lst)):
    if lst[l] != 0:
        lst[l] , lst[counter] = lst[counter], lst[l]
        counter += 1

print(lst)
        