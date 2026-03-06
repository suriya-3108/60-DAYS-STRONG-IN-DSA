# 📘 Day 24 DSA Practice — Sorting Basics

Today I focused on **Sorting Algorithms**, learning how arrays can be arranged in ascending or descending order using fundamental sorting techniques. The goal was to **understand the internal mechanics of sorting**, including comparisons, swaps, and shifting elements.

This day helped strengthen my understanding of **basic sorting logic, algorithm efficiency, and array manipulation**, which are essential for algorithm design and coding interviews.

---

## 1️⃣ Bubble Sort

* **Problem:** Sort an array by repeatedly swapping adjacent elements if they are in the wrong order.

* **Logic:**

  * Compare adjacent elements
  * Swap if `arr[j] > arr[j+1]`
  * After each pass, the **largest element moves to the end**
  * Reduce the comparison range after each iteration

* **Example:** `[5,1,4,2,8]` → Output: `[1,2,4,5,8]`

* **Implementation:**

```python
arr = [5, 1, 4, 2, 8]

for i in range(0 ,len(arr) - 1):
    for j in range(0, len(arr) - 1):
        if arr[j] > arr[j + 1]:
            arr[j] , arr[j + 1] = arr[j + 1] , arr[j]

print(arr)
```

* **Time Complexity:** O(n²)
* **Space Complexity:** O(1)

---

## 2️⃣ Selection Sort

* **Problem:** Sort an array by repeatedly selecting the **minimum element** from the unsorted portion and placing it in the correct position.

* **Logic:**

  * Assume the current position holds the minimum
  * Scan the remaining array to find the smallest element
  * Swap the smallest element with the current position
  * Move to the next position and repeat

* **Example:** `[64,25,12,22,11]` → Output: `[11,12,22,25,64]`

* **Implementation:**

```python
arr = [64, 25, 12, 22, 11]

for pos in range(len(arr)):
    min = pos
    for i in range(pos + 1, len(arr)):
        if arr[i] < arr[min]:
            min = i
    arr[min], arr[pos] = arr[pos], arr[min]

print(arr)
```

* **Time Complexity:** O(n²)
* **Space Complexity:** O(1)

---

## 3️⃣ Insertion Sort

* **Problem:** Sort an array by inserting each element into its correct position in the already sorted portion of the array.

* **Logic:**

  * Start from the second element
  * Store the current element as `key`
  * Compare it with elements on the left
  * Shift larger elements to the right
  * Insert the key in the correct position

* **Example:** `[12,11,13,5,6]` → Output: `[5,6,11,12,13]`

* **Implementation:**

```python
arr = [12, 11, 13, 5, 6]

for i in range(1,len(arr)):
    current = arr[i]
    j = i - 1
    
    while (j >= 0) and (current < arr[j]):
        arr[j + 1] = arr[j]
        j -= 1
    
    arr[j + 1] = current

print(arr)
```

* **Time Complexity:**
  Best Case: O(n)
  Average Case: O(n²)
  Worst Case: O(n²)

* **Space Complexity:** O(1)

---

## 4️⃣ Edge Cases Practiced

* Arrays that are already sorted
* Arrays sorted in reverse order
* Small arrays (1 or 2 elements)
* Arrays with duplicate elements
* Handling shifting vs swapping in sorting algorithms

---

## ✅ Key Skills Practiced

* Understanding **fundamental sorting algorithms**
* Implementing **Bubble Sort, Selection Sort, and Insertion Sort**
* Learning the difference between **swapping vs shifting elements**
* Improving **array manipulation and iteration logic**
* Analyzing **time and space complexity of sorting algorithms**

---

## 📊 Problem-Solving Approaches Summary

| Algorithm      | Technique Used                | Time Complexity | Space Complexity |
| -------------- | ----------------------------- | --------------- | ---------------- |
| Bubble Sort    | Repeated adjacent swapping    | O(n²)           | O(1)             |
| Selection Sort | Find minimum and swap         | O(n²)           | O(1)             |
| Insertion Sort | Shift elements and insert key | O(n²)           | O(1)             |

---

## 🧠 Key Takeaways

* Sorting is a **fundamental algorithmic concept** used in many problems.
* **Bubble Sort** works by repeatedly swapping adjacent elements.
* **Selection Sort** finds the minimum element and places it correctly.
* **Insertion Sort** builds the sorted array incrementally like arranging cards.
* Although these algorithms are simple, they help understand **how advanced sorting algorithms work internally**.

---

This completes **Day 24 — Sorting Basics**, strengthening my understanding of **core sorting algorithms, array manipulation, and algorithm efficiency** for coding interviews.
