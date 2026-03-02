# 📘 Day 20 DSA Practice — Combination Problems

Today I focused on **Combination Problems**, strengthening my understanding of **controlled selection using backtracking**. The emphasis was on generating combinations of fixed size and solving **target-based combination problems**, which are very common in coding interviews.

This day helped me clearly understand the difference between **permutations and combinations**, and how to handle **reuse, non-reuse, pruning, and duplicate avoidance** in recursion.

---

## 1️⃣ Combinations (n Choose k)

* **Problem:** Generate all possible combinations of `k` numbers from `1` to `n`.
* **Logic:** Use backtracking with a **start index** and stop when `len(path) == k`.
* **Example:** Input: `n=4, k=2` → Output: `[[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]`
* **Key Insight:**

  * Use `start` index to move forward.
  * Use `i + 1` to avoid reusing previous elements.
  * Order does NOT matter in combinations.

---

## 2️⃣ Combination Sum (Reuse Allowed)

* **Problem:** Find all combinations whose sum equals a target.
* **Logic:** Backtracking with a **running total**, stop when total exceeds target.
* **Example:** Input: `[2,3,6,7], target=7` → Output: `[[2,2,3],[7]]`
* **Key Insight:**

  * Use `backtrack(i, ...)` to reuse the same element.
  * Stop recursion when `total > target` (pruning).
  * This pattern combines **combination + constraint checking**.

---

## 3️⃣ Combination Sum II (No Reuse + Duplicate Handling)

* **Problem:** Find unique combinations that sum to target, where input may contain duplicates.
* **Logic:**

  * Sort array first
  * Skip duplicates using:

    ```
    if i > index and candidates[i] == candidates[i - 1]:
        continue
    ```
  * Use `i + 1` since reuse is NOT allowed.
* **Example:** Input: `[10,1,2,7,6,1,5], target=8`
* **Key Insight:**

  * Sorting groups duplicates together.
  * `i > index` ensures duplicates are skipped only at the same recursion level.
  * Prevents repeated combination branches.

---

## ✅ Key Skills Practiced

* Backtracking with controlled element selection
* Using `start` index properly
* Reuse vs non-reuse logic (`i` vs `i + 1`)
* Pruning when total exceeds target
* Sorting + duplicate skipping
* Understanding recursion tree behavior

---

## 📊 Problem-Solving Approaches Summary

| Problem                   | Technique Used                    | Time Complexity | Space Complexity |
| ------------------------- | --------------------------------- | --------------- | ---------------- |
| Combinations (n choose k) | Backtracking with start index     | O(n choose k)   | O(k)             |
| Combination Sum           | Backtracking + pruning            | O(2^n) approx   | O(n)             |
| Combination Sum II        | Backtracking + duplicate handling | O(2^n) approx   | O(n)             |

---

## 🧠 Key Takeaways

* **Combination ≠ Permutation** (order does NOT matter)
* `i + 1` → move forward (no reuse)
* `i` → reuse allowed
* Sorting helps eliminate duplicate solutions
* Pruning (`total > target`) improves efficiency
* Backtracking pattern remains:
  **Choose → Explore → Undo (pop)**

---

## 💡 Advanced Insights

* Combination problems are a core extension of recursion.
* Handling duplicates correctly is a major interview skill.
* Understanding when to reuse elements vs move forward is critical.
* These problems build the foundation for more advanced problems like:

  * Subset sum variations
  * K-sum problems
  * Partition problems

---

This completes **Day 20 — Combination Problems**, covering **n choose k, combination sum, and duplicate-handling combinations**, with a strong focus on **controlled selection and pruning in backtracking**.
