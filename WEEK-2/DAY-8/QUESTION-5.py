"""
Question 5 (Tricky Concept)
Check if Array is Sorted (Ascending Order)
Input:
[1, 2, 3, 4, 5]
Output → True

[1, 3, 2, 4]
Output → False

Rules:
O(n)
No sorting allowed
Must handle duplicates

Example:
[1,1,2,2,3] → True
"""

num = list(map(int, input("enter values: ").split()))

for i in range(0, len(num) - 1):
    if num[i] == num[i + 1] or num[i] < num[i + 1]:
        continue
    else:
        print("False")
        break
else:
    print("True")