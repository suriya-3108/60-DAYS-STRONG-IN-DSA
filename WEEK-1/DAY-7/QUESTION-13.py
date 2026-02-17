"""
Question 13: Anagram Check

Task:
Two strings are anagrams if they contain the same characters with the same frequency, but the order can be different.
Write a program that:
Takes two string inputs from the user.
Checks if they are anagrams using dictionary or collections.Counter (do not use sorting).
Prints "Anagram" if they are, otherwise "Not Anagram".

Sample Input 1:
Enter string 1: listen
Enter string 2: silent

Sample Output 1:
Anagram
"""

val1 = input("enter value-1: ")
val2 = input("enter value-2: ")

dictionary_1 ={}
dictionary_2 ={}

for char1 in val1:
    dictionary_1[char1] = dictionary_1.get(char1, 0) + 1

for char2 in val2:
    dictionary_2[char2] = dictionary_2.get(char2, 0) + 1
    
if dictionary_1 == dictionary_2:
    print("Anagram")
else:
    print("Not a Anagram")