"""
Day 8 Extra Problem 4
Maximum Product of Two Elements in an Array
📌 Problem:
Given an array of integers, find the maximum product of any two elements in the array.

Input:
arr = [3, 4, 5, 2]

Output:
20
"""

arr = [3, 4, 5, 2]

largest = float("-inf")

second_largest = float("-inf")

for n in arr:
    if n > largest:
        second_largest = largest
        largest = n
    elif n > second_largest and n != largest:
        second_largest = n

if second_largest == float("-inf"):
    print("cant define!")
    
else:
    res = largest * second_largest
    print(res)