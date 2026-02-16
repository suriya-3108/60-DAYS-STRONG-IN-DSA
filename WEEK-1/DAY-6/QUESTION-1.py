"""
Question 1 (Easy – Array)
🔹 Problem: Find the Second Largest Element in a List

Write a function that returns the second largest number in a list.

📌 Example:
Input: [10, 20, 4, 45, 99]
Output: 45

⚡ Conditions:
Do NOT use sort()
Do NOT use max() twice
Solve using loops only
Time complexity should be O(n)
"""

def find_second_largest(Input):
    largest = float("-inf")
    second_largest = float("-inf")
    for i in Input:
        if i > largest:
            second_largest = largest
            largest = i
    
        if i > second_largest and i != largest:
            second_largest = i
            
    if second_largest == float("-inf"):
        return None   
    return second_largest

Input = [10, 20, 4, 45, 99]
res = find_second_largest(Input)
print(res)
