"""
Question 8 (Day 4: collections module)
Count Elements Using Counter

Use collections.Counter to count the frequency of elements in a list.

Sample Input:
Enter numbers: 1 2 2 3 3 3 4

Sample Output:
Counter({3: 3, 2: 2, 1: 1, 4: 1})
"""

from collections import Counter

num = list(map(int, input("enter a values: ").split()))

freq = Counter(num)

print(freq)