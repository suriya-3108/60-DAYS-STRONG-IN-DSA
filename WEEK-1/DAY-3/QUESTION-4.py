"""
Question 4 (Very Similar — Try Yourself)

Write program to:
👉 Take numbers list
👉 Print first duplicate element only
👉 Using set
👉 Stop once found

Example:
Input: 3 5 1 4 5 2
Output: 5
"""

# num = list(map(int,input("enter values: ").split()))
# seen = set()
# dup = set()

# for n in num:
#     if n in seen:
#         dup.add(n)
#         break
#     else:
#         seen.add(n)
        
# print(dup)


# optimised version

num = list(map(int, input("enter values: ").split()))
seen = set()

for n in num:
    if n in seen:
        print(n)
        break
    else:
        seen.add(n)
