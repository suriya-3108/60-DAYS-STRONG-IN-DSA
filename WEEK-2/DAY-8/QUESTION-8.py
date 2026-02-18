"""
Day 8 Extra Problem 2
Move All Even Numbers to Front (Relative Order Preserved)
📌 Problem:

Given an array of integers, move all even numbers to the front while keeping the relative order of both even and odd numbers unchanged.

Input:
arr = [1, 2, 3, 4, 5, 6]

Output:
[2, 4, 6, 1, 3, 5]
"""

# arr = [1,2,3,4,5,6]

# even_arr = []
# odd_arr = []

# for i in arr:
#     if i % 2 == 0:
#         even_arr.append(i)
#     else:
#         odd_arr.append(i)

# even_arr.sort()
# odd_arr.sort()

# res = even_arr + odd_arr

# print(res)


arr = [1, 2, 3, 4, 5, 6]

n = len(arr)
pos = 0  

for i in range(n):
    if arr[i] % 2 == 0:
        even = arr[i]
        for j in range(i, pos, -1):
            arr[j] = arr[j - 1]
        arr[pos] = even
        pos += 1

print(arr)
