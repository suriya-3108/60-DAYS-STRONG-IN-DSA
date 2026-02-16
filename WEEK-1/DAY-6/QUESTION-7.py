"""Question 7 (Array – Sum Problem)
🔹 Problem: Find the Sum of All Elements in a List

Given a list of integers, calculate and print the sum of all elements.

📌 Example:
Input: [1, 2, 3, 4, 5]
Output: 15

⚡ Conditions:
Use loops only
Do NOT use built-in sum()
Solve with O(n) time complexity"""

num = list(map(int, input("enter numbers: ").split()))
sum = 0

for n in num:
    sum += n
print(sum) 