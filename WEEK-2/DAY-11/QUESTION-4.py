"""
Question 3: Prefix given (no building)

Prefix array:
prefix = [5, 9, 9, 12, 20]
Array length = 5

Queries:
(1, 4)
(0, 2)
(3, 3)

Tasks:
Directly compute answers
State which formula you used (if or else case)
"""
prefix = [5, 9, 9, 12, 20]

queries = [(1, 4),(0, 2),(3, 3)]

for l , r in queries:
    if l == 0:
        answer = prefix[r]
    else:
        answer = prefix[r] - prefix[l - 1]
        
    print(answer)