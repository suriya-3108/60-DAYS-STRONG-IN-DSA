"""
Final Bonus Question (Day 3 Master Check)

Try this:
👉 Check if two strings are anagrams using dictionary or set
Example:

listen
silent
→ True
"""

str1 = 'listen'
str2 = 'silent'
a = []
b = []
dictionary1 = {}
dictionary2 = {}

if len(str1) == len(str2):
    
    for s in str1:
        if s not in a:
            count = 0 
            for r in str1:
                if s == r:
                    count += 1
            dictionary1[s] = count
            a.append(s)

    for m in str2:
        if m not in b:
            count = 0 
            for n in str2:
                if m == n:
                    count += 1
            dictionary2[m] = count
            b.append(m)
    
if dictionary1 == dictionary2:
    print("true")
else:
    print("False")