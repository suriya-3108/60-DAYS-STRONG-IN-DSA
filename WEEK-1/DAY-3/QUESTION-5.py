"""
Question 5 (Final Level — Dictionary + Set Thinking)

Try this:
👉 Given a string
👉 Print the first non-repeating character

Example:
input: aabbcdde
output: c

Hint:
Use dictionary for frequency

Then loop string again
"""

s = input("enter a string: ")
dictionary = {}
arr = []

for str in s:
    if str not in arr:
        count = 0
        for chr in s:
            if str == chr:
                count += 1
        dictionary[str] = count
        arr.append(str)



for keys,values in dictionary.items():
    if values == 1:
        print(keys)
        break
        