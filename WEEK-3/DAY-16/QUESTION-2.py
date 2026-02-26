"""Longest Consecutive Sequence
Question
You are given an unsorted array of integers.

Task:
Find the length of the longest sequence of consecutive integers.

Input
[100, 4, 200, 1, 3, 2]
Output
4"""

nums = [1, 2, 4, 5]

seen = set(nums)

length = 0

for n in seen:
    if n - 1 not in seen:
        curent = n 
        count = 1
        
        while curent + 1 in seen:
            curent += 1
            count += 1
        if count > length:
            length = count
print(length)