"""
Question 6 — Remove Specific Element In-Place

Problem:
Given an array arr and a value val, remove all occurrences of val in-place and return the new length.
Do not use extra array
Order of elements can change
Just return the new length and modify the array in-place

Example 1
Input: arr = [3, 2, 2, 3], val = 3
Output: 2
"""

arr = [0,1,2,2,3,0,4,2]
val = 2

index = 0

for i in range(0,len(arr)):
        if arr[i] != val:
            arr[index] = arr[i]
            index += 1

print(index)
print(arr)