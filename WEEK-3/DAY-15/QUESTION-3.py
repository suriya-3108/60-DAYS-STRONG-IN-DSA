"""Practice Question 3 (next level, still easy)
Problem:
Check if a list contains any duplicate.

Input
nums = [1, 2, 3, 4, 5]
Output
False"""

nums = [1, 2, 3, 4, 5]

freq = {}

for n in nums:
    freq[n] = freq.get(n, 0) + 1
   
for n in nums:
    if freq[n] > 1:
        print("True")
        break
else:
    print("False")