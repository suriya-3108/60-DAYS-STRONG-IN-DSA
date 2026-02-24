"""Question 7 (Hard — Mixed Arrays + Sliding Window + Prefix Sum)

Problem: Maximum Average Subarray of Size K

Given an integer array arr and an integer k,
find the maximum average of any contiguous subarray of size k.
Return the maximum average as a float.

Example 1:
arr = [1, 12, -5, -6, 50, 3]
k = 4
# Output: 12.75"""

arr = [1, 12, -5, -6, 50, 3]

k = 4

summed_arr = sum(arr[:k])

average = summed_arr / k

output = average

for i in range(k ,len(arr)):
    summed_arr = summed_arr - arr[i - k] + arr[i]
    
    average = summed_arr / k
    
    output = max(output , average)
    
print(output)