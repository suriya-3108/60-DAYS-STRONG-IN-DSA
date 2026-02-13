"""
Question 3 (Sets: Find Duplicates)

Write a Python program to:
👉 Take numbers as input
👉 Find all duplicate elements
👉 Use set (no dictionary allowed for this one)
👉 Print duplicates as a set

✅ Example
Input:
1 2 3 2 4 1 5

Output:
{1, 2}

✅ Hint (DSA thinking)
Use two sets:

seen → store first time elements
dup  → store duplicates

Logic idea:

if number already in seen → add to dup
else → add to seen

✅ Rules for your solution

Use set
Only one loop (O n)
No nested loops
No dictionary
Write full program
"""

num = list(map(int,input("enter values: ").split()))
a  = set()
b = set()

for n in num:
    if n in a:
        b.add(n)
    else:
        a.add(n)

print(b)