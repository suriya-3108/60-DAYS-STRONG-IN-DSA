# 📘 Day 16 DSA Practice — Advanced Hashing & Longest Consecutive Sequence

Today I focused on **Advanced Hashing Techniques** including **duplicate detection**, **consecutive sequence finding**, **first repeating element**, and **subarray sum problems**. The emphasis was on understanding **optimal approaches for sequence-based problems**, **order-aware frequency counting**, and **sliding window with hash maps**.

This day strengthened my ability to identify **optimal vs. brute force solutions** and apply **hash-based logic** to various array problems, which is critical for **DSA fundamentals and coding interviews**.

---

## 1️⃣ Check if Array Contains Duplicate

* **Problem:** Given an array of integers, return True if any value appears at least twice, else return False.
* **Logic:** Store elements in a set while traversing. If an element is already present, a duplicate exists.
* **Example:** Input: `[1, 2, 3, 1]` → Output: `True`
* **Key Insight:** Sets provide O(1) lookup and early termination improves average performance.
* **Complexity:** Time → **O(n)**, Space → **O(n)**

---

## 2️⃣ Longest Consecutive Sequence

* **Problem:** Find the length of the longest consecutive elements sequence in an unsorted array.
* **Logic:** Use a set for O(1) lookups. For each number, check if it's the start of a sequence (no left neighbor), then count consecutive numbers.
* **Example:** Input: `[100, 4, 200, 1, 3, 2]` → Output: `4` (Sequence: [1, 2, 3, 4])
* **Key Insight:** Only start counting from numbers that have no left neighbor to avoid redundant calculations.
* **Complexity:** Time → **O(n)**, Space → **O(n)**

---

## 3️⃣ First Repeating Element

* **Problem:** Given an array of integers, print the first element that repeats (by order of appearance). If no repeating element exists, print -1.
* **Logic:** First pass → count frequencies using hash map. Second pass → find first element with frequency > 1.
* **Example:** Input: `[10, 5, 3, 4, 3, 5, 6]` → Output: `5`
* **Key Insight:** Two-pass approach ensures we respect "first in order of appearance" condition.
* **Complexity:** Time → **O(n)**, Space → **O(n)**

---

## 4️⃣ Longest Subarray with Sum = K

* **Problem:** Given an array of integers and a number K, find the length of the longest subarray whose sum equals K.
* **Logic:** Use sliding window technique when all numbers are positive. Expand right pointer to add elements, shrink left pointer when sum exceeds K, and track maximum length when sum equals K.
* **Example:** Input: `arr = [1, 2, 3, 4, 5]`, `K = 9` → Output: `3` (Subarray: [2, 3, 4])
* **Key Insight:** Sliding window works efficiently for positive numbers by maintaining a dynamic window based on sum comparison.
* **Complexity:** Time → **O(n)**, Space → **O(1)**

---

## ✅ Key Skills Practiced

* **Set-Based Duplicate Detection**
* **Set-Based Sequence Detection**
* **Optimizing Consecutive Element Problems**
* **Frequency Counting with Order Preservation**
* **Sliding Window Technique**
* **Early Termination Strategies**
* **Pattern Recognition in Arrays**
* **Interview-Oriented Problem Solving**

---

## 📊 Problem-Solving Approaches Summary

| Problem                      | Technique Used        | Time Complexity | Space Complexity |
| ---------------------------- | --------------------- | --------------- | ---------------- |
| Contains Duplicate           | Set with Early Stop   | O(n)            | O(n)             |
| Longest Consecutive Sequence | Set + Sequence Check  | O(n)            | O(n)             |
| First Repeating Element      | Two-Pass Hash Map     | O(n)            | O(n)             |
| Longest Subarray Sum = K     | Sliding Window        | O(n)            | O(1)             |

---

## 🧠 Key Takeaways

* **Use sets for O(1) membership tests** when order doesn't matter
* **For consecutive sequences**, only process potential sequence starts to achieve O(n) complexity
* **Two-pass approaches** help when order of appearance matters for output
* **Sliding window** is powerful for subarray problems with positive numbers
* **Early termination** improves average-case performance in duplicate detection
* **Choosing the right data structure** (set vs. dict) depends on whether you need counts or just existence

---

## 💡 Advanced Insights

* **Longest Consecutive Sequence** teaches us to think in terms of **sequence boundaries** rather than sorting (O(n) vs O(n log n))
* **First Repeating Element** demonstrates why sometimes two passes are necessary when order matters
* **Sliding window** problems require careful pointer management to avoid off-by-one errors
* **Duplicate detection** problems build foundation for more complex frequency-based algorithms
* **Problem variations** often require adapting the same core technique to new constraints

---

This completes **Day 16 — Advanced Hashing & Longest Consecutive Sequence**, covering essential patterns required for **DSA mastery and technical interviews** ✅