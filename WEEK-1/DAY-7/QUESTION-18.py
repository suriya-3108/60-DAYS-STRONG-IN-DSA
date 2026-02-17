"""
Question 18: Check if Two Lists Have Common Elements

Task:
Write a program that checks if two lists of numbers have any common elements.

If yes, print "Yes" and all the common elements (once).
If no, print "No".

Sample Input 1:
Enter first list: 1 2 3 4
Enter second list: 3 4 5 6

Sample Output 1:
Yes
Common elements: [3, 4]
"""

lst1 = list(map(int, input("enter numbers: ").split()))
lst2 = list(map(int, input("enter numbers: ").split()))

set1 = set()
set2 = set()

for n in lst1:
    set1.add(n)

for m in lst2:
    if m in set1:
        set2.add(m)
    else:
        set1.add(m)

if len(set2) > 0:
    print("yes")
    print(list(set2))
else:
    print("No")      
