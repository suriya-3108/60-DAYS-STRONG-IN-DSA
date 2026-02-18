"""
Question 1 (Warm-up)
🔹 Reverse an Array (Without using built-in reverse functions)
📌 Problem:

Given a list of integers, reverse the array in-place (do not use arr[::-1] or reverse()).

Input:
arr = [1, 2, 3, 4, 5]

Output:
[5, 4, 3, 2, 1]

⚠️ Rules:
Do NOT use built-in reverse methods
Try to do it in O(n) time
Extra space should be O(1)
"""

num = list(map(int, input("enter numbers: ").split()))

arr = []

for n in range(len(num) - 1, -1, -1):
    arr.append(num[n])
    
print(arr)
    