# 📘 Day 22 DSA Practice — Linear & Binary Search

Today I focused on **Linear and Binary Search**, understanding how to efficiently find elements in arrays and compare search algorithms. The goal was to **strengthen problem-solving with search techniques**, including iterative and recursive approaches, and handling duplicates in linear searches.

This day helped consolidate my understanding of **array traversal, pointer manipulation, and divide-and-conquer strategies**, which are essential for coding interviews and optimized algorithm design.

---

## 1️⃣ Linear Search — Basic & Variations

* **Basic Linear Search**

  * **Problem:** Find the index of a target element in an array.
  * **Logic:** Iterate over the array, compare each element with the target.
  * **Key Insight:** Simple and works for **unsorted arrays**.
  * **Example:** `[10, 25, 30, 45, 50], target=30` → Output: `2`

* **First & Last Occurrence (Linear)**

  * **Problem:** Return `[first_index, last_index]` of the target.
  * **Logic:** Loop through array, update `first` on first match, and keep updating `last` on subsequent matches.
  * **Example:** `[5,7,7,8,8,10], target=8` → Output: `[3,4]`

* **Key Considerations:**

  * Works on **unsorted arrays**
  * Time Complexity: **O(n)**
  * Space Complexity: **O(1)**

---

## 2️⃣ Binary Search — Basic (Iterative)

* **Problem:** Find the index of a target in a **sorted array**.
* **Logic:** Use two pointers `left` and `right`, calculate `mid`, compare `arr[mid]` with target:

  * `arr[mid] == target` → return `mid`
  * `arr[mid] < target` → search right half
  * `arr[mid] > target` → search left half
* **Key Insight:** Reduces search space by half each iteration.
* **Example:** `[10,20,30,40,50,60], target=40` → Output: `3`
* **Time Complexity:** O(log n)
* **Space Complexity:** O(1)

---

## 3️⃣ Binary Search — Recursive Version

* **Problem:** Same as iterative binary search.
* **Logic:** Recursively call function on left or right half until target found or subarray exhausted.
* **Key Insight:** Useful for practicing recursion and understanding divide-and-conquer.
* **Example:** `[10,20,30,40,50], target=30` → Output: `2`
* **Time Complexity:** O(log n)
* **Space Complexity:** O(log n) due to recursion stack

---

## 4️⃣ Linear vs Binary Search — Comparison

| Feature                 | Linear Search      | Binary Search      |
| ----------------------- | ------------------ | ------------------ |
| Works on sorted array   | Yes                | Yes                |
| Works on unsorted array | Yes                | No                 |
| Time Complexity (worst) | O(n)               | O(log n)           |
| Space Complexity        | O(1)               | O(1) (iterative)   |
| Efficiency              | Slower for large n | Faster for large n |

---

## 5️⃣ Binary Search — Last Occurrence

* **Problem:** Find the **last occurrence index** of a target in a **sorted array with duplicates**.
* **Logic:**

  * Initialize `result = -1`
  * Perform standard binary search
  * When `arr[mid] == target`, store `mid` in `result` and **move left pointer right** (`left = mid + 1`)
  * Return `result` after search completes
* **Example 1:** `[5, 7, 7, 8, 8, 8, 10], target=8` → Output: `5`
* **Example 2:** `[2, 2, 2, 3, 4, 5], target=2` → Output: `2`
* **Example 3 (Target Not Present):** `[1, 3, 5, 7, 9], target=4` → Output: `-1`
* **Time Complexity:** O(log n)
* **Space Complexity:** O(1)

---

## 6️⃣ Edge Cases Practiced

* Target at beginning or end
* Target not present
* Single-element arrays
* Empty arrays
* Arrays with duplicate elements

---

## ✅ Key Skills Practiced

* Array traversal with linear search
* Pointer manipulation and divide-and-conquer in binary search
* Iterative vs recursive thinking
* Handling edge cases in searches
* Understanding the efficiency difference between O(n) and O(log n)

---

## 📊 Problem-Solving Approaches Summary

| Topic                         | Technique Used                           | Time Complexity | Space Complexity |
| ----------------------------- | ---------------------------------------- | --------------- | ---------------- |
| Linear Search                 | Array iteration                          | O(n)            | O(1)             |
| Linear Search (first/last)    | Array iteration with first/last tracking | O(n)            | O(1)             |
| Binary Search                 | Iterative divide & conquer               | O(log n)        | O(1)             |
| Binary Search                 | Recursive divide & conquer               | O(log n)        | O(log n)         |
| Last Occurrence Binary Search | Iterative + store index + move right     | O(log n)        | O(1)             |

---

## 🧠 Key Takeaways

* **Linear search** is simple and works for all arrays but slower on large datasets.
* **Binary search** is efficient for sorted arrays and requires careful pointer management.
* Recursive and iterative approaches both work; recursion highlights divide-and-conquer thinking.
* **Last occurrence pattern**: move right when target is found to locate duplicates correctly.
* Edge cases are crucial: empty arrays, single-element arrays, targets not present, and duplicates.

---

This completes **Day 22 — Linear & Binary Search**, reinforcing **search algorithms, array traversal, iterative & recursive problem-solving**, and preparing for efficient coding patterns in interviews.