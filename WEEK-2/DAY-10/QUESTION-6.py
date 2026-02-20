"""
Problem 6 — Maximum of All Subarrays of Size K

Given:
arr = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

Output:
[3, 3, 5, 5, 6, 7]
"""
arr = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

left = 0

arr2 = max(arr[left:k])

maximum_arr = []

maximum_arr.append(arr2)

for i in range(k, len(arr)):
    left += 1
    arr2 = max(arr[left: i + 1])
    maximum_arr.append(arr2)
print(maximum_arr)