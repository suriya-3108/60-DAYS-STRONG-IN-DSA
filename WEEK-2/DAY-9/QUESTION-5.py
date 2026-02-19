"""
Question 5 — Pair with Given Sum (Unsorted Array)

Problem:
Given an unsorted array and a target sum, check if any pair exists in the array whose sum equals the target.
Return True if such a pair exists, otherwise False.

Example 1
Input: arr = [8, 7, 2, 5, 3, 1], target = 10
Output: True

"""

def is_total(arr, target):
    left = 0
    right = len(arr) - 1
    while (left < right):
        total = arr[left] + arr[right]
        if total == target:
            return True
        elif total < target:
            left += 1
        elif total > target:
            right -= 1

arr = [8, 7, 2, 5, 3, 1]

arr.sort()

target = 10

print(is_total(arr, target))