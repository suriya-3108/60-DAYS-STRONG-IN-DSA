"""
Question 11: Move All Zeros to End
Given a list, move all zeros to the end while maintaining the order of non-zero elements.
⚠️ Do NOT use extra list for filtering (try in-place if possible).

Sample Input:
Enter numbers: 0 1 0 3 12

Sample Output:
[1, 3, 12, 0, 0]
"""

num = list(map(int, input("enter numbers: ").split()))

index = 0

for i in range(len(num)):
    if num[i] != 0:
        num[i] , num[index] = num[index] , num[i]
        index += 1
    
print(num) 