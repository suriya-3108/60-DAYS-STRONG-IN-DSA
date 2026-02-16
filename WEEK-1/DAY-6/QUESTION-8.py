"""
Question 8 (Array – Sum of Even Numbers)
🔹 Problem: Sum of All Even Numbers in a List
Given a list of integers, calculate and print the sum of all even numbers only.

📌 Example:
Input: [1, 2, 3, 4, 5, 6]
Output: 12   # 2 + 4 + 6

⚡ Conditions:
Use loops only
Do NOT use list comprehensions or filter()
Time complexity → O(n)
"""

num = list(map(int, input("enter values: ").split()))

sum = 0

for n in num:
    if n % 2 == 0:
        sum += n

print(sum)