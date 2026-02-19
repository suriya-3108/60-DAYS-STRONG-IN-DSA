"""
Question 2 — Remove Duplicates (Two Pointer Classic)
Given a sorted array, remove duplicates in-place and return the length of unique elements.

Example:
Input:  [1,1,2,2,3,4,4]
Output: 4
Modified array: [1,2,3,4,...]

Rules:
Must modify array in-place
Use O(1) extra space
Return count of unique elements
"""

arr = [1,1,2,2,3,4,4]

left = 0

for right in range(1,len(arr)):
    if arr[left] != arr[right]:
        left += 1
        arr[left] = arr[right]
        
print(left + 1)
print(f"modified array: {arr}")
        