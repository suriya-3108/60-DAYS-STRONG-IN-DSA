"""Mixed Practice — Problem 2
Find First and Last Position of Element in Sorted Array

Given a sorted array nums and a target value,
return the first and last position of the target.

If the target is not found, return [-1, -1].

Example
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]"""

nums = [5,7,7,8,8,10]

target = 8

first = -1

last = -1

for i in range(len(nums)):
    if nums[i] == target:
        if first == -1:
            first = i
        last = i 
    
print([first,last])