"""Extra Problem 1 (Easy, Confidence Builder)
First Repeating Element
Problem Statement

Given an array of integers, print the first element that repeats.

“First” means first in order of appearance, not smallest.

If no repeating element exists, print -1.

Sample Input 1
[10, 5, 3, 4, 3, 5, 6]
Sample Output 1
5"""

arr = [10, 5, 3, 4, 3, 5, 6]

freq = {}

for n in arr:
    freq[n] = freq.get(n, 0) + 1

for n in arr:
    if freq[n] > 1:
        print(n)
        break
else:
    print("-1")