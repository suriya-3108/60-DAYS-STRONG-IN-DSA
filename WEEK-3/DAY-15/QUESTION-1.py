"""Practice Question 1 (VERY EASY)
Problem:
Given a list of numbers, count how many times each number appears.

Input
nums = [1, 2, 2, 3, 3, 3]
Expected Output
{1: 1, 2: 2, 3: 3}"""

nums = [1, 2, 2, 3, 3, 3]

freq = {}

for n in nums:
    freq[n] = freq.get(n, 0) + 1

print(freq)