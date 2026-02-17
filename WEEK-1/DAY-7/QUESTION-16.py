"""
Question 16: Reverse Words in a Sentence

Task:
Write a program to reverse the words in a sentence, but keep the letters in each word the same.

Sample Input 1:
Enter sentence: hello world from python

Sample Output 1:
python from world hello
"""

s = 'hello world from python'

word = s.split(' ')

reverse_word = ' '.join(word[::-1])

print(reverse_word)