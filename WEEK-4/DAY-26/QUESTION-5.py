"""Problem 6: Sort Colors (Dutch National Flag Problem)
Problem

Given an array with 0s, 1s, and 2s, sort it in-place so that all 0s come first, then 1s, then 2s.

Do not use extra space and try to solve in one pass."""

nums = [2,0,2,1,1,0]

left  = 0
mid = 0
right = len(nums) - 1

while mid <= right:
    if nums[mid] == 0:
        nums[mid] , nums[left] = nums[left] , nums[mid]
        mid += 1
        left += 1
    
    elif nums[mid] == 1:
        mid += 1
        
    else:
        nums[mid] , nums[right] = nums[right], nums[mid]
        right -= 1

print(nums)