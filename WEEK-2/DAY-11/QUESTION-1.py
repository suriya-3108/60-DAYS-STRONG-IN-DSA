"""
Question 1 (Warm-up — MUST do)

Problem:
Given an array:
arr = [3, 1, 4, 2, 5]

You are given these queries:
(0, 2)
(1, 3)
(2, 4)
"""

arr = [3, 1, 4, 2, 5]

prefix = [0] * len(arr)

prefix[0] = arr[0]

for i in range(1,len(arr)):
    prefix[i] = prefix[i - 1] + arr[i]
    
print(prefix)

queries = [(0, 2),(1, 3),(2, 4)]

for l,r in queries:
    if l == 0:
        summed_answer = prefix[r]
    else:
        summed_answer = prefix[r] - prefix[l - 1]
        
    print(summed_answer)