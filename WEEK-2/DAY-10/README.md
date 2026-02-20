# Day 10 DSA Practice — Sliding Window Technique

Today I focused on **sliding window problems on arrays and strings**, including **maximum/average of subarrays, smallest subarray with sum ≥ target, and longest substring problems**. This helped improve my **problem-solving skills, logic building, edge case handling, and preparation for coding interviews**.

---

## 1️⃣ Maximum Sum Subarray of Size K

* **Problem:** Given an array and a number `k`, find the maximum sum of any contiguous subarray of size `k`.
* **Logic:** Use a **fixed-size sliding window**; calculate initial sum of first `k` elements, then slide the window by subtracting the element leaving the window and adding the new element entering.
* **Example:** `[2, 1, 5, 1, 3, 2]`, k=3 → `8` (subarray `[5,1,3]`)

---

## 2️⃣ Find Average of All Subarrays of Size K

* **Problem:** Given an array and `k`, return a list of averages of all contiguous subarrays of size `k`.
* **Logic:** Use **fixed-size sliding window**; maintain a running sum, update average as window slides.
* **Example:** `[1, 3, 2, 6, -1, 4, 1, 8, 2]`, k=5 → `[2.2, 2.8, 2.4, 3.6, 2.8]`

---

## 3️⃣ Smallest Subarray with Sum ≥ Target

* **Problem:** Given an array and a target sum, find the length of the smallest contiguous subarray whose sum is ≥ target.
* **Logic:** Use **variable-size sliding window**; expand window until sum ≥ target, then shrink from left to minimize length.
* **Example:** `[2, 1, 5, 2, 3, 2]`, target=7 → `2` (subarray `[5,2]`)

---

## 4️⃣ Longest Substring Without Repeating Characters

* **Problem:** Given a string, find the length of the longest substring without repeating characters.
* **Logic:** Use **variable-size sliding window + set/dictionary**; expand window and add characters, shrink from left if a duplicate occurs, track max length.
* **Example:** `"abcabcbb"` → `3` (substring `"abc"`)

---

## 5️⃣ Longest Substring with At Most K Distinct Characters

* **Problem:** Given a string and number `k`, find the length of the longest substring containing at most `k` distinct characters.
* **Logic:** Use **variable-size sliding window + dictionary**; expand window, count character frequencies, shrink from left if distinct count > k, update max length.
* **Example:** `"eceba"`, k=2 → `3` (substring `"ece"`)

---

## 6️⃣ Maximum of All Subarrays of Size K

* **Problem:** Given an array and number `k`, return a list of maximums for all contiguous subarrays of size `k`.
* **Logic:** Use **deque** to track indices of potential maximum elements; front of deque always holds max for current window.
* **Example:** `[1, 3, -1, -3, 5, 3, 6, 7]`, k=3 → `[3, 3, 5, 5, 6, 7]`

---

## ✅ Key Skills Practiced

* **Sliding Window Technique** — fixed-size and variable-size windows
* **Window Expansion & Shrinking Logic** — maintain sums, counts, or unique elements
* **Hashing / Set / Dictionary Use** — track duplicates or distinct elements
* **Deque for Max Tracking** — efficient O(n) solution for maximum in subarray
* **Array & String Traversal** — contiguous subarrays, substring problems
* **Edge Case Handling** — small arrays, repeated characters, negative numbers

---

This practice consolidated **Day 10 concepts** and strengthened **sliding window logic, sum/average tracking, substring analysis, maximum element tracking, and edge case handling**, preparing me for **more advanced array/string problems** in upcoming DSA practice.

---
