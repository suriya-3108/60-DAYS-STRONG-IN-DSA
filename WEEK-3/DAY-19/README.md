# 📘 Day 19 DSA Practice — Backtracking

Today I focused on **Backtracking**, exploring **how recursion can systematically explore all possibilities** in combinatorial problems. The emphasis was on **subsets, permutations, combinations, and sum constraints**, which are foundational for **complex DSA problems and coding interviews**.

This day strengthened my ability to **choose, explore, and backtrack (undo choices)**, and to **trace recursion with constraints**, essential for solving **all combinatorial and decision-tree problems**.

---

## 1️⃣ Subsets (Power Set)

* **Problem:** Generate all subsets of a list of numbers.
* **Logic:** Use backtracking with **include/exclude pattern**.
* **Example:** Input: `[1,2,3]` → Output: `[[], [1], [1,2], [1,2,3], [1,3], [2], [2,3], [3]]`
* **Key Insight:** Backtracking explores **all combinations of elements** by appending and popping elements.

---

## 2️⃣ Permutations

* **Problem:** Generate all possible orderings of numbers in a list.
* **Logic:** Use backtracking and remove chosen element from remaining numbers.
* **Example:** Input: `[1,2,3]` → Output: `[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]`
* **Key Insight:** Backtracking explores **all sequences** and uses `path.pop()` to **undo choices** for new sequences.

---

## 3️⃣ Combinations of Size K

* **Problem:** Generate all subsets of size `k`.
* **Logic:** Backtracking stops recursion when **path length = k**.
* **Example:** Input: `[1,2,3], k=2` → Output: `[[1,2],[1,3],[2,3]]`
* **Key Insight:** Use `start` index to **avoid duplicates** and ensure combinations are unique.

---

## 4️⃣ Combination Sum (Target Sum)

* **Problem:** Find all combinations whose sum equals a target.
* **Logic:** Backtracking **explores numbers**, keeps running total, stops if total > target.
* **Example:** Input: `[1,2,3], target=3` → Output: `[[1,2],[3]]`
* **Key Insight:** Use recursion with **running total** and **backtracking** to explore valid sums efficiently.

---

## ✅ Key Skills Practiced

* Subsets, permutations, and combinations with backtracking
* Include/exclude pattern in recursion
* Handling constraints (size k, target sum)
* Avoiding duplicates with sorting and skipping
* Tracing recursion and undoing choices (`path.pop()`)

---

## 📊 Problem-Solving Approaches Summary

| Problem                | Technique Used                | Time Complexity | Space Complexity |
| ---------------------- | ----------------------------- | --------------- | ---------------- |
| Subsets (Power Set)    | Backtracking, include/exclude | O(2^n)          | O(n)             |
| Permutations           | Backtracking, element removal | O(n!)           | O(n)             |
| Combinations of size k | Backtracking with constraints | O(n choose k)   | O(k)             |
| Combination Sum        | Backtracking, target sum      | O(2^n)          | O(n)             |

---

## 🧠 Key Takeaways

* **Backtracking = choose → explore → undo choice**
* **Start index** ensures **no duplicates** in combinations
* **Constraints** like size or target sum guide recursion stopping conditions
* Sorting input helps **avoid duplicate solutions**
* Visualizing recursion tree makes backtracking flow clear

---

## 💡 Advanced Insights

* Backtracking patterns today form a bridge from **recursion** to **combinatorial problem solving**
* Understanding **when and how to prune recursion** is key for efficiency
* Practicing these problems prepares for **subset/permutation/combination interview questions** ✅

---

This completes **Day 19 — Backtracking**, covering **subsets, permutations, combinations, and combination sums** with a focus on **systematic exploration and constraints**.