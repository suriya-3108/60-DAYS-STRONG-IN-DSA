"""Practice Question 2 (still easy, next step)
Problem:
Given a list of numbers, print the first number that appears twice.

Input
nums = [4, 1, 2, 3, 1, 5]
Output
1"""

nums = [4, 1, 2, 3, 1, 5]

freq = {}

for n in nums:
    freq[n] = freq.get(n, 0) + 1

for n in nums:
    if freq[n] == 2:
        print(n)
        break