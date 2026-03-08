"""Problem 1: Two Sum (Sorting + Two Pointer)
Problem
Given an array of integers and a target value, return two numbers whose sum equals the target.

Example:
nums = [2,7,11,15]
target = 9

Output:
[2,7]"""

nums = [2,7,11,15]

target = 9

nums.sort()

left = 0

right = len(nums) - 1

while (left < right):
    total = nums[left] + nums[right]
    
    if total == target:
        print([nums[left],nums[right]])
        break
    
    elif total < target:
        left += 1
        
    elif total > target:
        right -= 1


