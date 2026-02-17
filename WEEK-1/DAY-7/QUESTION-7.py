"""
Question 7 (Day 4: List Comprehension)
Square All Even Numbers

Task:
Given a list of numbers, create a new list containing the square of only even numbers using list comprehension.

Sample Input:
Enter numbers: 1 2 3 4 5 6

Sample Output:
[4, 16, 36]
"""

num = list(map(int,input('enter numbers: ').split()))

res_list = [i ** 2 for i in num if i % 2 == 0]

print(res_list)