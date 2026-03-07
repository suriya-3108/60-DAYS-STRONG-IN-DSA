"""Question 2 — Quick Sort
Now implement Quick Sort.

Problem
Write a function to sort an array using Quick Sort.

Example
Input
[7, 2, 9, 1, 5]

Output
[1, 2, 5, 7, 9]"""

import random

def Quick_sort(array):
    
    if len(array) <= 1:
        return array
    
    pivot = random.choice(array)
    
    left = []
    for i in range(len(array)):
        if array[i] < pivot:
            left.append(array[i])
    
    right = []
    for j in range(len(array)):
        if array[j] > pivot:
            right.append(array[j])
    
    middle = []
    for k in range(len(array)):
        if array[k] == pivot:
            middle.append(array[k])
    
    return Quick_sort(left) + middle + Quick_sort(right)
    
array = [7, 2, 9, 1, 5]
res = Quick_sort(array)       
print(res)