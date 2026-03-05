# 📘 Day 23 DSA Practice — Binary Search Variations

Today I focused on **Binary Search Variations**, exploring how to efficiently find elements in sorted arrays and handle duplicates. The goal was to **strengthen problem-solving using divide-and-conquer strategies**, including first/last occurrence, count, lower bound, and upper bound searches.

This day helped consolidate my understanding of **binary search boundaries, edge cases, and optimized search techniques**, which are essential for coding interviews and algorithm design.

---

## 1️⃣ First Occurrence

* **Problem:** Find the **first index** of a target in a **sorted array with duplicates**.
* **Logic:**

  * Initialize `result = -1`
  * Standard binary search
  * When `arr[mid] == target`, store `mid` in `result` and **move left** (`right = mid - 1`)
* **Example:** `[1,2,2,2,3], target=2` → Output: `1`
* **Time Complexity:** O(log n)
* **Space Complexity:** O(1)

---

## 2️⃣ Last Occurrence

* **Problem:** Find the **last index** of a target in a sorted array with duplicates.
* **Logic:**

  * Initialize `result = -1`
  * Standard binary search
  * When `arr[mid] == target`, store `mid` in `result` and **move right** (`left = mid + 1`)
* **Example:** `[1,2,2,2,3], target=2` → Output: `3`
* **Time Complexity:** O(log n)
* **Space Complexity:** O(1)

---

## 3️⃣ Count Occurrences

* **Problem:** Count how many times a target appears in a sorted array.
* **Logic:**

  * Find **first occurrence** and **last occurrence**
  * Count = `last - first + 1`
  * If target not found → return 0
* **Example:** `[1,2,2,2,3], target=2` → Output: `3`
* **Time Complexity:** O(log n)
* **Space Complexity:** O(1)

---

## 4️⃣ Lower Bound

* **Problem:** Find the **first index where element ≥ target**.
* **Logic:**

  * Initialize `result = len(arr)`
  * Binary search with condition `arr[mid] >= target`
  * If true → store `mid` and move left (`right = mid - 1`)
  * Else → move right (`left = mid + 1`)
* **Example 1:** `[1,2,4,6,8], target=5` → Output: `3`
* **Example 2:** `[1,2,4,6,8], target=10` → Output: `5`
* **Time Complexity:** O(log n)
* **Space Complexity:** O(1)

---

## 5️⃣ Upper Bound

* **Problem:** Find the **first index where element > target**.
* **Logic:**

  * Initialize `result = len(arr)`
  * Binary search with condition `arr[mid] > target`
  * If true → store `mid` and move left (`right = mid - 1`)
  * Else → move right (`left = mid + 1`)
* **Example 1:** `[1,2,4,6,8], target=4` → Output: `3`
* **Example 2:** `[1,2,4,6,8], target=8` → Output: `5`
* **Time Complexity:** O(log n)
* **Space Complexity:** O(1)

---

## 6️⃣ Edge Cases Practiced

* Target at beginning or end of array
* Target not present
* Single-element arrays
* Empty arrays
* Arrays with duplicate elements
* Target larger than all elements (lower/upper bound)

---

## ✅ Key Skills Practiced

* Binary search variations (first/last occurrence, count, lower & upper bound)
* Array traversal and divide-and-conquer thinking
* Handling duplicates and boundary conditions
* Efficient O(log n) search strategies
* Careful pointer manipulation and iterative logic

---

## 📊 Problem-Solving Approaches Summary

| Topic             | Technique Used                      | Time Complexity | Space Complexity |
| ----------------- | ----------------------------------- | --------------- | ---------------- |
| First Occurrence  | Binary search + move left on match  | O(log n)        | O(1)             |
| Last Occurrence   | Binary search + move right on match | O(log n)        | O(1)             |
| Count Occurrences | First + Last Occurrence             | O(log n)        | O(1)             |
| Lower Bound       | Binary search + condition >= target | O(log n)        | O(1)             |
| Upper Bound       | Binary search + condition > target  | O(log n)        | O(1)             |

---

## 🧠 Key Takeaways

* Binary search is a **powerful divide-and-conquer tool** for sorted arrays.
* **Boundary search patterns** (first/last occurrence, lower/upper bound) are crucial for interview questions.
* Edge cases are important: empty arrays, single-element arrays, targets not present, and duplicates.
* Understanding **when and how to move left/right** is key for variations.

---

This completes **Day 23 — Binary Search Variations**, reinforcing **optimized search techniques, boundary detection, and handling duplicates** for coding interviews.
