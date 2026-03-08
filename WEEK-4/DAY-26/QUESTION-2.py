"""Problem 2: Contains Duplicate
Problem
Given an integer array nums, return True if any value appears at least twice, and return False if every element is unique.

Example 1
nums = [1,2,3,1]

Output
True"""

nums = [1,2,3,1]

duplicate = False

nums.sort()

for i in range(len(nums) - 1):
    if nums[i] == nums[i + 1]:
        duplicate = True
        break

print(duplicate)