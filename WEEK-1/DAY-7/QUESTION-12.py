"""
🔹 Question 12: First Non-Repeating Character
Given a string, find the first non-repeating character.

Sample Input:
Enter string: aabbcdde

Sample Output:
c

If no such character exists, print:
None

⚠️ Must use dictionary (or Counter).
⚠️ Must return first non-repeating in order.
"""

s = input("enter a string: ")

dictionary = {}

for char in s:
    dictionary[char] = dictionary.get(char, 0) + 1
    

for char in s:
    if dictionary[char] == 1:
        print(char)
        break

else:
    print("None")