"""Problem 2 — Remove Duplicates from Sorted Array
Given a sorted array, remove duplicates in-place and return the new length.

Example:
Input:
[1,1,2,2,3,4,4]

Output:
[1,2,3,4]
Length = 4"""

arr = [1,1,2,2,3,4,4]

i = 0

for n in range(1,len(arr)):
    if arr[n] != arr[i]:
        i += 1
        arr[i] = arr[n]

length = i + 1

print(length)
print(arr[:length])
