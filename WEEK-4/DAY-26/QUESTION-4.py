"""Problem 4: Intersection of Two Arrays
Problem
Given two arrays, return the common elements present in both arrays.

Example
Input
arr1 = [1,2,2,3,4]
arr2 = [2,2,3,5]

Output
[2,2,3]"""

arr1 = [1,2,2,3,4]
arr2 = [2,2,3,5]

arr1.sort()
arr2.sort()

charset = set(arr1)
result = []

for i in arr2:
    if i in charset:
        result.append(i)
    
print(result)