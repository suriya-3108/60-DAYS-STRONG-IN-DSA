"""Problem: Search Insert Position

You are given a sorted array of distinct integers and a target value.

Return the index if the target is found.
If not, return the index where it would be inserted to keep the array sorted.

Example 1
Input: nums = [1,3,5,6], target = 5
Output: 2"""

def search_insert_position(nums, target):
    
    left  = 0
    right = len(nums) - 1
    while (left <= right):
        middle = (left + right) // 2
        if nums[middle] == target:
            return middle

        elif nums[middle] > target:
            right = middle - 1
    
        elif nums[middle] < target:
            left = middle + 1

    return left

nums = [1,3,5,6]

target = 5

res = search_insert_position(nums, target)

print(res)