"""
Question 9: Second Largest Element

Write a program to find the second largest number in a list
(Do NOT use sort()).

Sample Input:
Enter numbers: 10 5 20 8

Sample Output:
Second largest is: 10
"""

num = list(map(int, input("enter numbers: ").split()))

largest = float("-inf")
 
second_largest = float("-inf")

for n in num:
    if n > largest:
        second_largest = largest
        largest = n
    
    elif n > second_largest and n != largest:
        second_largest = n

if second_largest == float('-inf'):
    print("None")
else:
    print(second_largest)