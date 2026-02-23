"""Problem 5 — Move All Zeros to End
Given an array arr, move all zeros to the end while maintaining the relative order of non-zero elements. Do it in-place.

Example:
arr = [0, 1, 0, 3, 12]

Output:
[1, 3, 12, 0, 0]"""

arr = [0, 1, 0, 3, 12]

left = 0

for right in range(len(arr)):
    if arr[right] != 0:
        arr[right] , arr[left] = arr[left] , arr[right]
        left += 1
    
print(arr)