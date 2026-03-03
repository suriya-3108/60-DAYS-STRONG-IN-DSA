"""Revision Problem 1 (Hashing – Basic)
Problem: Two Sum (Revised Version)
Given an integer array nums and an integer target, return the indices of the two numbers such that they add up to target.
You:
Must use HashMap
Time complexity should be O(n)
Cannot use nested loops

Example:
Input:
nums = [4, 1, 5, 3, 2]
target = 6

Output:
[1, 2]"""

# nums = [4, 1, 5, 3, 2]

# target = 6

# left = 0

# right = len(nums) - 1

# while left < right:
#     total = nums[left] + nums[right]
    
#     if total == target:
#         print([left, right])
#         break
    
#     elif total < target:
#         left += 1
        
#     elif total > target:
#          right -= 1


nums = [4, 1, 5, 3, 2]

target = 6

output = {}

for i in range(len(nums)):
    complement = target - nums[i]
    
    if complement in output:
        print([output[complement],i])
        break
    
    output[nums[i]] = i
              