"""
Problem 2 — Find Average of All Subarrays of Size K
Given:

arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k = 5

Output:

[2.2, 2.8, 2.4, 3.6, 2.8]
"""

arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]

k = 5

output = []

sum_arr = sum(arr[0:k]) 

avg_arr = sum_arr / k

output.append(avg_arr)

for i in range(k, len(arr)):
    
    sum_arr= (sum_arr - arr[i - k] + arr[i] ) 
    avg_arr = sum_arr / k
    output.append(avg_arr)

    
print(output)