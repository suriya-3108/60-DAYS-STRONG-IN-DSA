"""Problem 1 (Optimized): Next Greater Element I — Stack Solution"""

def solution(nums1, nums2):
    stack = []
    greater = {}
    
    for num in nums2:
        while stack and num > stack[-1]:
            smaller = stack.pop()
            greater[smaller] = num
        stack.append(num)
    
    while stack:
        greater[stack.pop()] = -1
    
    result = []
    for nums in nums1:
        result.append(greater[nums])
    
    return result

nums1 = [4,1,2]
nums2 = [1,3,4,2]
print(solution(nums1, nums2))