"""Problem 1: Next Greater Element I

You are given two arrays nums1 and nums2.
nums1 is a subset of nums2.
For each element in nums1, find the next greater element in nums2.
The next greater element of a number x is the first greater number to its right in nums2.
If it does not exist → return -1.
Example

Input
nums1 = [4,1,2]
nums2 = [1,3,4,2]

Output
[-1,3,-1]"""

def solution(nums1, nums2):
    result = []
    
    for num in nums1:
        index = nums2.index(num)
        near_greatest = -1
        
        for i in range(index + 1, len(nums2)):
            if nums2[i] > num:
                near_greatest = nums2[i]
                break
        
        result.append(near_greatest)
    
    return result 

nums1 = [4,1,2]
nums2 = [1,3,4,2]
print(solution(nums1, nums2))