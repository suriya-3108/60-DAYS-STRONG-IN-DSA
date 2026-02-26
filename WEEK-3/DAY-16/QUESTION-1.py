"""Day 16 — Question 1 (Warm-up)
🔹 Problem 1: Check for Duplicates
(This prepares your brain for Longest Consecutive Sequence)
Problem Statement

Given an array of integers, return True if any value appears at least twice, else return False.
Example
Input:  [1, 2, 3, 1]
Output: True
"""

Input =  [1, 2, 3, 4]

seen = {}

for i in Input:
    if i in seen:
        print("True")
        break
    seen[i] = True
else:
    print("False")