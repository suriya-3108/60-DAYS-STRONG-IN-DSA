# 📘 Day 26 DSA Practice — Sorting-Based Problems

Today I focused on **sorting-based problems**, learning how to manipulate arrays efficiently using sorting, two pointers, and in-place techniques. The goal was to **strengthen problem-solving with array manipulation, interval merging, duplicate handling, and category sorting**.

This day helped consolidate my understanding of **sorting strategies, pointer manipulation, and optimized array traversal**, which are essential for coding interviews and algorithm design.

---

## 1️⃣ Two Sum (Sorting + Two Pointers)

* **Problem:** Given an array of integers and a target value, return two numbers whose sum equals the target.
* **Logic:**

  * Sort the array
  * Initialize `left` and `right` pointers
  * Move pointers based on the sum compared to the target
* **Example:** `[2,7,11,15], target=9` → Output: `[2,7]`
* **Time Complexity:** O(n log n) (sorting) + O(n) (two pointers) = O(n log n)
* **Space Complexity:** O(1)

---

## 2️⃣ Contains Duplicate

* **Problem:** Determine if an array contains duplicates.
* **Logic:**

  * Sort the array
  * Check adjacent elements for equality
* **Example:** `[1,2,3,1]` → Output: `True`
* **Time Complexity:** O(n log n)
* **Space Complexity:** O(1)

---

## 3️⃣ Merge Intervals

* **Problem:** Merge all overlapping intervals in a list.
* **Logic:**

  * Sort intervals by start value
  * Initialize `merged` with the first interval
  * Iterate through remaining intervals:

    * If current start ≤ last merged end → merge
    * Else → append new interval
* **Example:** `[[1,3],[2,6],[8,10],[15,18]]` → Output: `[[1,6],[8,10],[15,18]]`
* **Time Complexity:** O(n log n)
* **Space Complexity:** O(n)

---

## 4️⃣ Intersection of Two Arrays

* **Problem:** Return common elements between two arrays (including duplicates).
* **Logic:**

  * Sort both arrays
  * Use two pointers to traverse both arrays
  * Add elements to result when equal, move pointers accordingly
* **Example:** `[1,2,2,3,4], [2,2,3,5]` → Output: `[2,2,3]`
* **Time Complexity:** O(n log n)
* **Space Complexity:** O(n)

---

## 5️⃣ Sort Colors (Dutch National Flag Problem)

* **Problem:** Sort an array of 0s, 1s, and 2s in-place.
* **Logic:**

  * Use three pointers: `left` (next 0), `mid` (current), `right` (next 2)
  * Iterate while `mid ≤ right`:

    * If 0 → swap with `left`, move `left` and `mid`
    * If 1 → move `mid`
    * If 2 → swap with `right`, move `right` only
* **Example:** `[2,0,2,1,1,0]` → Output: `[0,0,1,1,2,2]`
* **Time Complexity:** O(n)
* **Space Complexity:** O(1)

---

## ✅ Key Skills Practiced

* Sorting arrays and intervals
* Two-pointer techniques for sums and intersections
* In-place array manipulation and swapping
* Handling duplicates and edge cases
* Optimized array traversal without extra space

---

## 🧠 Key Takeaways

* Sorting is a **foundational tool** for array problems.
* Two-pointer approaches are powerful for **sum, intersection, and merging problems**.
* **In-place swapping and careful pointer updates** reduce space complexity.
* Understanding **interval merging and category sorting** prepares you for many interview questions.

---

This completes **Day 26 — Sorting-Based Problems**, reinforcing **efficient array manipulation, sorting strategies, and two-pointer problem-solving techniques**.
