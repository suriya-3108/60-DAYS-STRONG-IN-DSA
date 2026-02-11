"""Question 3 — List + Loop (Core DSA Base)

Write a program to:
Find the second largest number in a list

Requirements:

1) No sorting
2) Single pass if possible
3) Use variables to track values

Example:
Input: [4, 9, 2, 7, 5]
Output: 7       """

max = float("-inf")
min = float("-inf")
Input= [4, 9, 2, 7, 5]

for i in range(len(Input)):
    if Input[i] > max:
        min = max
        max = Input[i]
        
    if Input[i] > min and Input[i] != max:
        min = Input[i]

print(min)