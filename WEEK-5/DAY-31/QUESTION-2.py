"""Deque Problem (Very Important)
Sliding Window Maximum
Problem

You are given an integer array nums and an integer k.
There is a sliding window of size k that moves from left → right across the array.
Your task is to return the maximum value in each window."""

# nums = [1,3,-1,-3,5,3,6,7]
# k = 3

# left = 0
# maxxed = max(nums[:k])

# result = []

# result.append(maxxed)

# for i in range(k, len(nums)):
#     left += 1
#     maxxed = max(nums[left:i + 1])
#     result.append(maxxed)

# print(result)

from collections import deque

def sliding_window_max(nums, k):
    dq = deque()
    result = []

    for i in range(len(nums)):

        while dq and dq[0] <= i - k:
            dq.popleft()

        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        dq.append(i)

        if i >= k - 1:
            result.append(nums[dq[0]])

    return result


nums = [1,3,-1,-3,5,3,6,7]
k = 3

print(sliding_window_max(nums, k))