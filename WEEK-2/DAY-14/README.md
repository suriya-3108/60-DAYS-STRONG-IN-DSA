# 📘 Day 14 DSA Practice — Revision + Mock Practice

Today I focused on **revision and mock practice** combining **arrays, two-pointer technique, sliding window, prefix sum, and string pattern problems**. This helped reinforce **problem-solving skills, pattern recognition, and efficient coding strategies**, which are crucial for **DSA fundamentals, competitive programming, and coding interviews**.

---

## 1️⃣ Longest Subarray with Sum = K

* **Problem:** Given an array `arr` and a number `k`, return the length of the longest subarray whose sum equals `k`.
* **Logic:**
  Check all possible subarrays, calculate sum, and track the maximum length where sum = k.
* **Example:**
  Input: `arr = [1, 2, 3, 1, 1, 1, 1], k = 3`
  Output: `3`
* **Key Insight:**
  Brute-force works, but using prefix sum + hashmap can optimize to O(n).
* **Complexity:**
  Time → **O(n²)**, Space → **O(1)**

---

## 2️⃣ Move All Zeros to End

* **Problem:** Move all zeros to the end while maintaining relative order of non-zero elements. Do it in-place.
* **Logic:**
  Use two pointers: left tracks position for next non-zero. Swap non-zero elements to left.
* **Example:**
  Input: `arr = [0,1,0,3,12]`
  Output: `[1,3,12,0,0]`
* **Key Insight:**
  Swapping preserves relative order of non-zero elements.
* **Complexity:**
  Time → **O(n)**, Space → **O(1)**

---

## 3️⃣ Maximum Sum Subarray of Size k

* **Problem:** Find the maximum sum of any contiguous subarray of size `k`.
* **Logic:**
  Use sliding window: sum first k elements, then slide window by subtracting left and adding right element.
* **Example:**
  Input: `arr = [2,1,5,1,3,2], k = 3`
  Output: `9` (subarray `[5,1,3]`)
* **Key Insight:**
  Sliding window avoids recomputing sums → O(n) instead of O(n*k).
* **Complexity:**
  Time → **O(n)**, Space → **O(1)**

---

## 4️⃣ Count Subarrays with Sum = K

* **Problem:** Count all contiguous subarrays whose sum equals `k`.
* **Logic:**
  Brute-force: check all subarrays and increment count if sum = k.
* **Example:**
  Input: `arr = [1,1,1], k = 2`
  Output: `2`
* **Key Insight:**
  Each distinct subarray is counted; optimized prefix sum + hashmap can improve to O(n).
* **Complexity:**
  Time → **O(n²)**, Space → **O(1)**

---

## 5️⃣ Check if Two Strings are Anagrams

* **Problem:** Determine if two strings `s1` and `s2` are anagrams.
* **Logic:**
  Count character frequency in both strings using dictionaries, then compare.
* **Example:**
  Input: `s1 = "listen", s2 = "silent"`
  Output: `True`
* **Key Insight:**
  Frequency maps ensure order-independent comparison.
* **Complexity:**
  Time → **O(n)**, Space → **O(n)**

---

## 6️⃣ First Unique Character in a String

* **Problem:** Find the index of the first non-repeating character in a string. Return -1 if none exists.
* **Logic:**
  Count character frequencies with a dictionary, then traverse string to find first with count = 1.
* **Example:**
  Input: `s = "aabb"`
  Output: `-1`
* **Key Insight:**
  Use dictionary for frequency and preserve original order using traversal.
* **Complexity:**
  Time → **O(n)**, Space → **O(n)**

---

## 7️⃣ Maximum Average Subarray of Size K

* **Problem:** Find the maximum average of any contiguous subarray of size `k`.
* **Logic:**
  Sliding window: sum first k elements, then slide window while updating sum and average.
* **Example:**
  Input: `arr = [1,12,-5,-6,50,3], k = 4`
  Output: `12.75` (subarray `[12,-5,-6,50]`)
* **Key Insight:**
  Sliding window allows O(n) computation for sum → maximum average.
* **Complexity:**
  Time → **O(n)**, Space → **O(1)**

---

## ✅ Key Skills Practiced

* **Array Traversal & Manipulation**
* **Two-Pointer Technique**
* **Sliding Window (Fixed & Variable)**
* **Prefix Sum & Subarray Sum Logic**
* **Frequency Counting & Anagram Checking**
* **In-Place Operations**
* **Edge Case Handling**
* **Optimizing Time Complexity**
* **Interview-Oriented Problem Solving**

---

## 📊 Problem-Solving Approaches Summary

| Problem                       | Technique Used           | Time Complexity | Space Complexity |
| ----------------------------- | ------------------------ | --------------- | ---------------- |
| Longest Subarray with Sum = K | Brute-force / Prefix Sum | O(n²) / O(n)    | O(1) / O(n)      |
| Move Zeros                    | Two-Pointer              | O(n)            | O(1)             |
| Max Sum Subarray              | Sliding Window           | O(n)            | O(1)             |
| Count Subarrays with Sum = K  | Brute-force / Prefix Sum | O(n²) / O(n)    | O(1) / O(n)      |
| Check Anagram                 | Frequency Map            | O(n)            | O(n)             |
| First Unique Character        | Frequency Map            | O(n)            | O(n)             |
| Max Average Subarray          | Sliding Window           | O(n)            | O(1)             |

---

This completes **Day 14 revision + mock practice**, consolidating all **key DSA patterns** for arrays, strings, and sliding window techniques.
