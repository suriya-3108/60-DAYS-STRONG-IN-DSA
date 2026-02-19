"""
Question 7 — Reverse Words in a String

Problem:
Given a string s containing words separated by spaces, reverse the order of words.
Words are separated by single or multiple spaces
No extra spaces at the start or end in the output
Must use two-pointer approach to reverse in-place (or similar logic)

Example 1
Input: "the sky is blue"
Output: "blue is sky the"
"""


# s = "  hello   world  "
# s.strip()
# a = s.split(" ")

# n = len(a) // 2

# for i in range(n):
#     a[i], a[-n - i + 1] = a[-n - i + 1] , a[i]
# for b in a:
#     print(b, end=" ")

s = "  hello   world  "
words = [word for word in s.strip().split(" ") if word]

left = 0
right = len(words) - 1
while left < right:
    words[left], words[right] = words[right], words[left]
    left += 1
    right -= 1

result = " ".join(words)
print(result)

