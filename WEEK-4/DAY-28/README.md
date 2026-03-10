# 📘 Day 28 DSA Practice — Revision & Mixed Problems

Today I focused on **revising searching and sorting concepts through mixed problems**, applying binary search, array manipulation, and two-pointer techniques. The goal was to **strengthen problem-solving speed, revisit key patterns, and simulate a small mock interview environment**.

This day helped reinforce my understanding of **binary search logic, boundary conditions, and efficient array traversal**, which are crucial for solving real coding interview problems.

---

## 1️⃣ Search Insert Position (Binary Search)

* **Problem:** Given a sorted array and a target value, return the index if found, otherwise return the index where it should be inserted.
* **Logic:**

  * Use binary search with `left` and `right` pointers
  * Calculate `mid` index
  * If target found → return `mid`
  * If target smaller → search left half
  * If target greater → search right half
  * When loop ends → return `left` as insert position
* **Example:** `[1,3,5,6], target=2` → Output: `1`
* **Time Complexity:** O(log n)
* **Space Complexity:** O(1)

---

## 2️⃣ Find First and Last Position of Element in Sorted Array

* **Problem:** Find the first and last occurrence of a target value in a sorted array.
* **Logic:**

  * Use binary search twice
  * First search → find **first occurrence** by moving `right = mid - 1`
  * Second search → find **last occurrence** by moving `left = mid + 1`
  * Return `[first, last]`
* **Example:** `[5,7,7,8,8,10], target=8` → Output: `[3,4]`
* **Time Complexity:** O(log n)
* **Space Complexity:** O(1)

---

## 3️⃣ Find Peak Element (Binary Search Optimization)

* **Problem:** Find an element that is greater than its neighbors.
* **Logic:**

  * Use binary search to compare `nums[mid]` and `nums[mid+1]`
  * If `nums[mid] < nums[mid+1]` → move right
  * Otherwise → move left
  * Continue until `left == right`
* **Example:** `[1,2,3,1]` → Output: `2`
* **Time Complexity:** O(log n)
* **Space Complexity:** O(1)

---

## 4️⃣ Move Zeroes (Two-Pointer Technique)

* **Problem:** Move all zeros to the end of the array while maintaining the order of non-zero elements.
* **Logic:**

  * Use two pointers `left` and `right`
  * Traverse array with `right`
  * When a non-zero element is found → swap with `left`
  * Increment `left`
* **Example:** `[0,1,0,3,12]` → Output: `[1,3,12,0,0]`
* **Time Complexity:** O(n)
* **Space Complexity:** O(1)

---

## ✅ Key Skills Practiced

* Binary search implementation and variations
* Handling edge cases in sorted arrays
* Efficient index searching and boundary conditions
* Two-pointer techniques for array manipulation
* Optimized problem-solving with logarithmic complexity

---

## 🧠 Key Takeaways

* Binary search is extremely powerful for **sorted arrays and index-based problems**.
* Many problems can be solved by **slightly modifying the binary search boundaries**.
* Two-pointer techniques help solve **array rearrangement problems efficiently**.
* Practicing mixed problems improves **speed, pattern recognition, and interview readiness**.

---

This completes **Day 28 — Revision & Mixed Practice**, reinforcing **binary search mastery, array manipulation techniques, and efficient problem-solving strategies**.