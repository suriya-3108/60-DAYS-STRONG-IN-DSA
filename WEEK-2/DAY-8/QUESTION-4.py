"""
Question 4 (Important)
Find the Second Largest Element in an Array
Input:
[10, 5, 20, 8]

Output:
10

Rules:
Do NOT sort the array
Must be O(n)
Handle duplicates properly
If no second largest exists → print something like "No second largest"

Example:
[5, 5, 5] → No second largest
"""

num = list(map(int,input("enter numbers: ").split()))

largest = float("-inf")
second_largest = float("-inf")

for n in num:
    if n > largest:
        second_largest = largest
        largest = n
    
    elif n > second_largest and n != largest:
        second_largest = n

if second_largest == float("-inf"):
    print("No second largest number in the given array!!!")
else:
    print(second_largest)