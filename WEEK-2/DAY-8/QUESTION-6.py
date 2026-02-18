"""
Question of Day 8 (Slightly Harder)
Remove Duplicates from a Sorted Array (In-place)
Input:
[1,1,2,2,3,3,4]

Output:
[1,2,3,4]

Rules:
Array is already sorted
Modify in-place
O(n) time
O(1) extra space
Do NOT use set()
"""

# arr = [1,1,2,2,3,3,4]

# num = []

# for i in arr:
#     if i not in num:
#         num.append(i)
        
# print(num)

"""optimal solution"""

arr = [1,1,2,2,3,3,4]

if len(arr) == 0:
    print(arr)
else:
    j = 0

    for i in range(1, len(arr)):
        if arr[i] != arr[j]:
            j += 1
            arr[j] = arr[i]

    print(arr[:j+1])
