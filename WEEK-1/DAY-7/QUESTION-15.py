"""
Question 15: Find Duplicate Elements in a List

Task:
Write a program that finds all duplicate elements in a list and prints them once.

Sample Input:
Enter numbers: 1 2 3 2 4 1 5

Sample Output:
Duplicates: [1, 2]
"""

numbers = list(map(int, input("Enter numbers: ").split()))

seen = set()
duplicates = set()

for num in numbers:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)

print("Duplicates:", list(duplicates))
