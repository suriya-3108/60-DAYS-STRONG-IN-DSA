"""
Question 2 (Slightly Harder)
Rotate Array Left by 1 (In-place)
Input:
[1, 2, 3, 4, 5]

Output:
[2, 3, 4, 5, 1]

Rules:
Modify same array
No extra array
O(n) time
"""


num = list(map(int, input("enter numbers: ").split()))

rotate = int(input("enter number: "))

length = len(num)

for n in range(rotate):
    first = num[0]
    for i in range(0, length - 1):
        num[i] = num[i + 1]
    num[-1] = first

print(num)