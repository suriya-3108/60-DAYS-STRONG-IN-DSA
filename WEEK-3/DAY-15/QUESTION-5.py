"""Practice Question 5 (Two Sum - beginner version)
Problem:
Given an array and a target, return True if any two numbers add up to the target.

Input
nums = [2, 7, 11, 15]
target = 9
Output
True"""

# nums = [2, 7, 11, 15]

# target = 9

# left = 0

# right = len(nums) - 1

# while(left < right):
#     total = nums[left] + nums[right]
    
#     if total == target:
#         print("True")
#         break
    
#     elif total < target:
#         left += 1
        
#     elif total > target:
#         right -= 1


"""Hash-map solution"""

nums = [2, 7, 11, 15]
target = 9

seen = {}

for n in nums:
    rem = target - n
    if rem in seen:
        print("True")
        break
    seen[n] = True