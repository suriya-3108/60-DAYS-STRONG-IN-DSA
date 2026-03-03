"""Revision Problem 2 (Advanced Hashing)
Problem: Longest Consecutive Sequence
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
⚠ Conditions:
Must run in O(n)
Cannot sort the array

Example 1:
Input:
nums = [100, 4, 200, 1, 3, 2]

Output:
4"""

nums = [100, 4, 200, 1, 3, 2]

seen = set(nums)

length = 0

for n in nums:
    if n - 1 not in seen:
        current = n
        count = 1
        
        while current + 1 in seen:
            current += 1
            count += 1
        
        if count > length:
            length = count

print(length)