"""
Day 8 Extra Problem 5
Find Minimum and Maximum in Array in a Single Pass
📌 Problem:
Given an array of integers, find both the minimum and maximum elements in a single traversal.

Input:
arr = [3, 1, 5, 2, 4]

Output:
Min = 1, Max = 5
"""
arr = [3, 1, 5, 2, 4, 0]

largest = float("-inf")

smallest = float("inf")

for n in arr:
    if n > largest:
        largest = n 
    if n < smallest:
        smallest = n

print(smallest, largest)