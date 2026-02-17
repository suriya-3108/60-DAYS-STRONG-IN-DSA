"""
Question 10: Palindrome Check (Without slicing)

Write a program to check whether a string is a palindrome
⚠️ Do NOT use slicing ([::-1]).

Sample Input:
Enter string: madam

Sample Output:
Palindrome
"""
s = input("enter a string: ")
a = ''

for char in range(len(s) - 1, -1, -1):
    a += s[char]
 
if s == a:
    print("palindrome")
else:
    print("Not a palindrome")
