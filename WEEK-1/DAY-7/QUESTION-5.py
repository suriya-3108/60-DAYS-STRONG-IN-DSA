"""
Question 5: Character Frequency

Task:
Write a program to count the frequency of each character in a string using a dictionary.

Sample Input:
Enter a string: banana

Sample Output:
{'b': 1, 'a': 3, 'n': 2}
"""

s = input("Enter a string value: ")

dictionary = {}

for str in s:
    dictionary[str] = dictionary.get(str, 0) + 1
    
print(dictionary)