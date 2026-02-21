"""Question 3 (Edge Case Focus)

Problem:
Given:

arr = [-2, 4, -1, 3, -5]

Queries:
(1, 1)
(0, 2)
(2, 4)"""

arr = [-2, 4, -1, 3, -5]

prefix = [0] * len(arr)

prefix[0] = arr[0]

for i in range(1,len(arr)):
    prefix[i] = prefix[i - 1] + arr[i]
    
print(prefix)    #[-2, 2, 1, 4, -1]

queries = [(1, 1),(0, 2),(2, 4)]

for l, r in queries:
    if l == 0:
        answer = prefix[r]
    else:
       answer = prefix[r] - prefix[l - 1]
       
    print(answer)