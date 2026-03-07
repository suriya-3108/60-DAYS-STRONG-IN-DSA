# 📘 Day 25 DSA Practice — Merge Sort & Quick Sort

Today I focused on **Divide and Conquer Sorting Algorithms**, specifically **Merge Sort and Quick Sort**, which are more efficient than basic sorting algorithms. The goal was to **understand recursive problem solving, array partitioning, and efficient sorting strategies**.

This day helped strengthen my understanding of **advanced sorting techniques, recursion, and algorithm optimization**, which are essential concepts for technical interviews and large-scale data processing.

---

## 1️⃣ Merge Sort

* **Problem:** Sort an array using the **Merge Sort algorithm**, which divides the array into smaller parts, sorts them recursively, and merges them back together.

* **Logic:**

  * Divide the array into two halves
  * Recursively apply merge sort on both halves
  * Merge the two sorted halves into one sorted array
  * Continue until the entire array is sorted

* **Example:** `[8,3,5,2]` → Output: `[2,3,5,8]`

* **Implementation:**

```python
def merge_sort(arr):

    if len(arr) > 1:
        middle = len(arr) // 2

        left = arr[:middle]
        right = arr[middle:]

        merge_sort(left)
        merge_sort(right)

        lp = 0
        rp = 0
        fp = 0

        while lp < len(left) and rp < len(right):

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
merge_sort(arr)
print(arr)
```

* **Time Complexity:**
  Best Case: O(n log n)
  Average Case: O(n log n)
  Worst Case: O(n log n)

* **Space Complexity:** O(n)

---

## 2️⃣ Quick Sort

* **Problem:** Sort an array using the **Quick Sort algorithm**, which selects a pivot element and partitions the array into smaller and larger elements.

* **Logic:**

  * Choose a **pivot element**
  * Partition the array into:

    * Elements smaller than the pivot
    * Elements equal to the pivot
    * Elements greater than the pivot
  * Recursively apply quick sort to the left and right partitions
  * Combine the results

* **Example:** `[7,2,9,1,5]` → Output: `[1,2,5,7,9]`

* **Implementation:**

```python
import random

def quick_sort(array):

    if len(array) <= 1:
        return array

    pivot = random.choice(array)

    left = []
    middle = []
    right = []

    for num in array:

        if num < pivot:
            left.append(num)

        elif num > pivot:
            right.append(num)

        else:
            middle.append(num)

    return quick_sort(left) + middle + quick_sort(right)


array = [7, 2, 9, 1, 5]
print(quick_sort(array))
```

* **Time Complexity:**
  Best Case: O(n log n)
  Average Case: O(n log n)
  Worst Case: O(n²)

* **Space Complexity:** O(log n) recursion stack (average)

---

## 3️⃣ Edge Cases Practiced

* Arrays with **duplicate elements**
* Arrays with **single element**
* Arrays that are **already sorted**
* Arrays sorted in **reverse order**
* Small arrays to verify **recursion termination**

---

## ✅ Key Skills Practiced

* Understanding **Divide and Conquer strategy**
* Implementing **Merge Sort and Quick Sort**
* Using **recursion to solve complex problems**
* Learning **pivot-based partitioning**
* Comparing **efficient vs basic sorting algorithms**

---

## 📊 Problem-Solving Approaches Summary

| Algorithm  | Technique Used                 | Time Complexity | Space Complexity |
| ---------- | ------------------------------ | --------------- | ---------------- |
| Merge Sort | Divide and merge sorted halves | O(n log n)      | O(n)             |
| Quick Sort | Pivot partitioning             | O(n log n) avg  | O(log n)         |

---

## 🧠 Key Takeaways

* **Merge Sort** divides the array and merges sorted halves efficiently.
* **Quick Sort** works by selecting a pivot and partitioning the array.
* Both algorithms use the **Divide and Conquer approach**.
* Merge Sort guarantees **O(n log n)** time complexity.
* Quick Sort is often **faster in practice** due to in-place partitioning.

---

This completes **Day 25 — Merge Sort & Quick Sort**, strengthening my understanding of **efficient sorting algorithms, recursion, and divide-and-conquer strategies** used in real-world applications and coding interviews.
