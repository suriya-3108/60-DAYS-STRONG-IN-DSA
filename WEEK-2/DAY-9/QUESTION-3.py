"""
Question 3 — Move Zeros (Classic)
Given an array, move all 0s to the end while maintaining the relative order of non-zero elements.

You must:
Modify array in-place
Use O(1) extra space
Time complexity O(n)

Example 1
Input:
[0, 1, 0, 3, 12]

Output:
[1, 3, 12, 0, 0]
"""

arr = [0, 1, 0, 3, 12]

k = 0

for i in range(len(arr)):
    if arr[i] != 0:
        arr[i] , arr[k] = arr[k] , arr[i]
        k += 1
        
print(arr)