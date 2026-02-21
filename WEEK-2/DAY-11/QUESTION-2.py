"""Question 2 (Medium — think carefully)
Problem:

Given:
arr = [5, 2, -1, 3, 4]

Queries:
(0, 4)
(1, 3)
(2, 2)
"""

arr = [5, 2, -1, 3, 4]

prefix = [0] * len(arr)

prefix[0] = arr[0]

for i in range(1, len(arr)):
    prefix[i] = prefix[i - 1] + arr[i]

print(prefix)    # [5, 7, 6, 9, 13]

queries = [(0, 4),(1, 3),(2, 2)]

for l, r in queries:
    if l == 0:
        summed_answer = prefix[r]
    else:
        summed_answer = prefix[r] - prefix[l - 1]

    print(summed_answer)