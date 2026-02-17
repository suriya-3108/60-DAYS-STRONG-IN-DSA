"""
Question 17: Find Maximum Repeated Element

Task:
Given a list of numbers, find the element that occurs the most times. If multiple elements have the same maximum frequency, return any one of them.

Sample Input 1:
Enter numbers: 1 2 2 3 3 3 4

Sample Output 1:
Most frequent element: 3
"""
num = list(map(int, input("enter nmubers: ").split()))

dictionary = {}

freq = 0

freq_key = 0

for n in num:
    dictionary[n] = dictionary.get(n, 0) + 1
    
print(dictionary)

for keys,values in dictionary.items():
    if values > freq:
        freq = values
        freq_key = keys
        
print(freq_key)

