"""Problem 4 — Move Zeroes
Move all 0s to the end of the array while maintaining the relative order of non-zero elements.

Example:
Input:
[0,1,0,3,12]

Output:
[1,3,12,0,0]"""

arr = [0,1,0,3,12]

left = 0

for right in range(len(arr)):
    if arr[right] != 0:
        arr[left] , arr[right] = arr[right] , arr[left]
        left += 1

print(arr)