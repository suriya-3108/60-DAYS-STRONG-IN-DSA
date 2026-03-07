"""Implement Merge Sort
Write a function that sorts an array using the Merge Sort algorithm.

Example
Input
[8, 3, 5, 2]

Output
[2, 3, 5, 8]"""

def Merge_sort(arr):
    
    if len(arr) > 1:
        middle = len(arr) // 2
        
        left = arr[:middle]
        right = arr[middle:]
        
        Merge_sort(left)
        Merge_sort(right)
        
        lp = 0
        rp = 0
        fp = 0
        
        while (lp < len(left)) and (rp < len(right)):
            if left[lp] < right[rp]:
                arr[fp] = left[lp]
                lp += 1
            
            else:
                arr[fp] = right[rp]
                rp += 1
                
            fp += 1
        
        while lp < len(left):
            arr[fp] = left[lp]
            lp += 1
            fp += 1
        
        while rp < len(right):
            arr[fp] = right[rp]
            rp += 1
            fp += 1 
         
arr = [8, 3, 5, 2]
Merge_sort(arr)
print(arr)