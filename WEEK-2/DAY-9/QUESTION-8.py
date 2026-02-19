"""
Problem Statement:
A palindrome is a word, phrase, or sequence that reads the same forwards and backwards (ignoring spaces and punctuation). Given a string, check if it's a palindrome using two pointers.

Examples:
"racecar" → True (reads same forwards and backwards)
"hello" → False (reads "hello" vs "olleh")
"A man a plan a canal Panama" → True (ignoring spaces)
"""

def find_palindrome(left , right, b):
    while(left < right):
        if b[left] != b[right]:
            return False
        left += 1
        right -= 1
        
    return True

s = 'A man a plan a canal Panama'
a = [n for n in s.strip().lower().split(" ")]
b = ''.join(a)
left = 0
right = len(b) - 1

print(find_palindrome(left , right, b))