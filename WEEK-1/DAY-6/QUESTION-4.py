"""
Question 4 (Slightly Trickier – Array)
🔹 Problem: Move All Zeros to End

Given a list, move all zeros to the end
while maintaining the order of non-zero elements.

Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

Conditions:
Do NOT use another list
Modify the same list
Time complexity O(n)
"""


# inp = [0,1,0,3,12]
# out = []

# for a in inp:
#     if a > 0 :
#         out.append(a)

# cal = len(inp) - len(out)

# out.extend([0]* cal)

# print(out)


""" optimized solution"""

arr = [0,1,0,3,12]

index = 0 

for i in range(len(arr)):
    if arr[i] != 0:
        arr[index], arr[i] = arr[i], arr[index]
        index += 1

print(arr)
