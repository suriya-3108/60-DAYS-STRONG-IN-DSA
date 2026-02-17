"""
Question 14: Count Vowels in a String

Task:
Write a program that counts the number of vowels (a, e, i, o, u) in a given string.

Sample Input 1:
Enter a string: hello world

Sample Output 1:
Number of vowels: 3
"""

s = input("enter a string value: ")

VOWELS = ['A','E','I','O','U','a','e','i','o','u']

total_vowels = 0

for char in s:
    if char in VOWELS:
        total_vowels += 1
        
print(total_vowels)