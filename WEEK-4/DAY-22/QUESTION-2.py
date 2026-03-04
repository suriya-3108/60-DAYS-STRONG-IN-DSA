"""Problem 2 — Linear Search (First & Last Occurrence)
Now we increase difficulty slightly.

Question:
Given a list of integers and a target number,
return a list containing:
[first_index, last_index]
If the target does not exist, return:
[-1, -1]
Example 1:
arr = [5, 7, 7, 8, 8, 10]
target = 8

Output:
[3, 4]"""

def linear_search(arr, target):
    first  = -1
    last = -1
    
    for i in range(len(arr)):
        if arr[i] == target:
            if first == -1:
                first = i
            last = i
    return [first , last]

arr = [5, 7, 7, 8, 8, 10]
target = 8
res = linear_search(arr, target)
print(res)