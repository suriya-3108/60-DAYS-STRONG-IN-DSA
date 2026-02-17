"""
Question 6 (Day 3: Sets)
Remove Duplicates from a List

Task:
Write a program to remove duplicates from a list using a set, and print the result as a list.

Sample Input:
Enter numbers: 1 2 2 3 4 4 5

Sample Output:
[1, 2, 3, 4, 5]
"""
num = list(map(int, input("enter a values: ").split()))

res_list = set(num)

print(list(res_list))