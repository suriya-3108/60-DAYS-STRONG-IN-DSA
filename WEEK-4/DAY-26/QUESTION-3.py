"""Merge Intervals
This is EXTREMELY common in interviews (Google, Amazon, Microsoft).

Example:
Input:
[[1,3],[2,6],[8,10],[15,18]]

Output:
[[1,6],[8,10],[15,18]]"""

arr = [[1,3],[2,6],[8,10],[15,18]]

arr.sort()

merged = [arr[0]]

for start, end in arr[1:]:
    last = merged[-1][1]
    
    if start <= last:
        merged[-1][1] = max(last, end)
    
    else:
        merged.append([start,end])
    
    
print(merged)