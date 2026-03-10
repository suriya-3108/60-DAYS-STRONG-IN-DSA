"""Problem (Problem 3 — Very Common Interview)
Find Peak Element
A peak element is greater than its neighbors.
Return the index of any peak element.

Example:
Input: nums = [1,2,3,1]
Output: 2

Because:
3 > 2 and 3 > 1"""

def findPeakElement(nums):

    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return left

nums = [1,2,3,1]
print(findPeakElement(nums))