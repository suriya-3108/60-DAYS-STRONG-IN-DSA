# 📘 Day 21 DSA Practice — Week 3 Revision: Hashing, Recursion & Backtracking

Today I focused on **Week 3 Revision**, revisiting all topics: **Hashing, Recursion, Backtracking, Subsets, Permutations, and Combination Problems**. The goal was to **strengthen problem-solving patterns** and ensure I can apply each concept confidently under coding interview scenarios.

This day helped consolidate my understanding of **hash-based lookups, recursion patterns, and controlled backtracking selection**, while also reviewing **reuse, non-reuse, pruning, and duplicate handling**.

---

## 1️⃣ Hashing — Two Sum & Longest Consecutive Sequence

* **Two Sum Problem**

  * **Problem:** Find indices of two numbers in an array that sum to target.
  * **Logic:** Use a **hashmap/dictionary** to check complements while iterating.
  * **Key Insight:** Check complement **before storing current number** to avoid using the same element twice.
  * **Example:** `[4,1,5,3,2], target=6` → Output: `[1,2]`

* **Longest Consecutive Sequence**

  * **Problem:** Find the length of the longest consecutive elements sequence.
  * **Logic:** Convert array to a **set** for O(1) lookups, start counting only at sequence starts (`n-1` not in set).
  * **Example:** `[100,4,200,1,3,2]` → Output: `4` (sequence `1,2,3,4`)

---

## 2️⃣ Recursion — Sum of Digits & Power of X

* **Sum of Digits**

  * **Problem:** Compute sum of digits of a number recursively.
  * **Logic:** Base case: `n==0 → return 0`. Recursive case: `last_digit + sum_of_digits(rest)`.
  * **Example:** `1234` → Output: `10`

* **Power Function (x^n)**

  * **Problem:** Compute `x^n` using recursion efficiently.
  * **Logic:** Use **divide-and-conquer** (binary exponentiation):

    * Even `n`: `x^n = (x^(n/2))^2`
    * Odd `n`: `x^n = x * (x^(n//2))^2`
  * **Example:** `2^5 → 32`
  * **Key Insight:** Reduces recursion depth from `O(n)` to `O(log n)`

---

## 3️⃣ Backtracking — Subsets & Permutations

* **Subsets (Power Set)**

  * **Problem:** Generate all subsets of an array.
  * **Logic:** Include/exclude each element recursively.
  * **Key Insight:** Store `path[:]` to avoid reference issues, use `start index` to prevent duplicates.
  * **Example:** `[1,2,3]` → `[[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]`

* **Permutations**

  * **Problem:** Generate all permutations of an array.
  * **Logic:** Track **used elements** or remove from temporary list each recursion.
  * **Key Insight:** Order matters, standard backtracking pattern: **Choose → Explore → Undo**
  * **Example:** `[1,2,3]` → `[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]`

---

## 4️⃣ Combination Problems — Combination Sum & Subset Sum

* **Combination Sum (Reuse Allowed)**

  * **Problem:** Find all combinations summing to target, elements can be reused.
  * **Logic:** Use **running total**, prune if `total > target`.
  * **Example:** `[2,3,6,7], target=7` → `[[2,2,3],[7]]`

* **Subset Sum / Combination Sum II (No Reuse)**

  * **Problem:** Find all combinations summing to target, each element used at most once.
  * **Logic:** Move `index + 1` in recursion, prune if `total > target`.
  * **Example:** `[2,3,5], target=8` → `[[3,5]]`

---

## ✅ Key Skills Practiced

* Hashing for O(n) lookup and sequence detection
* Base case and recursive thinking in digit sums and power functions
* Backtracking patterns: **Choose → Explore → Undo**
* Controlled element selection: reuse vs non-reuse
* Pruning to optimize recursion
* Duplicate handling in combinations

---

## 📊 Problem-Solving Approaches Summary

| Topic                        | Technique Used                    | Time Complexity | Space Complexity |
| ---------------------------- | --------------------------------- | --------------- | ---------------- |
| Two Sum                      | HashMap lookup                    | O(n)            | O(n)             |
| Longest Consecutive Sequence | HashSet + sequence start check    | O(n)            | O(n)             |
| Sum of Digits                | Simple recursion                  | O(log n)        | O(log n)         |
| Power x^n                    | Binary exponentiation recursion   | O(log n)        | O(log n)         |
| Subsets                      | Backtracking                      | O(2^n)          | O(n)             |
| Permutations                 | Backtracking                      | O(n!)           | O(n)             |
| Combination Sum              | Backtracking + pruning + reuse    | O(2^n) approx   | O(n)             |
| Subset Sum / Combination II  | Backtracking + pruning + no reuse | O(2^n) approx   | O(n)             |

---

## 🧠 Key Takeaways

* **Hashing** enables O(1) lookups for complements and sequences
* **Recursion** requires clear base and recursive cases
* **Backtracking** is versatile: subsets, permutations, combinations
* Reuse vs non-reuse is controlled via **index management**
* Pruning improves efficiency and avoids unnecessary recursion
* Copying paths (`path[:]`) is crucial to avoid reference errors

---

## 💡 Advanced Insights

* Week 3 topics form the foundation for complex interview problems:

  * Subset sum variants
  * K-sum problems
  * Partition and combination problems
* Optimized recursion (e.g., binary exponentiation) reduces time complexity significantly
* Controlled backtracking with pruning and duplicate handling is key to scalable solutions

---

This completes **Day 21 — Week 3 Revision**, covering **Hashing, Recursion, Backtracking, Subsets, Permutations, and Combination Problems**, reinforcing **efficient problem-solving patterns and core DSA concepts**.
