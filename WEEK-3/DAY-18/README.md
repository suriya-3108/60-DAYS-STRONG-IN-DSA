# 📘 Day 18 DSA Practice — Recursion Patterns

Today I focused on **Recursion Patterns**, exploring **how recursion can be applied systematically** to solve problems like **mathematical sequences, combinatorial sums, and nested structures**. The emphasis was on **recognizing patterns in recursion**, implementing **include/exclude logic, divide & conquer, and structured recursive outputs**, which is essential for **complex DSA problems and coding interviews**.

This day strengthened my ability to **trace recursive calls for patterns**, **apply base and recursive cases cleverly**, and **break down problems into smaller subproblems with predictable behavior**.

---

## 1️⃣ Sum of First N Numbers (Recursive)

* **Problem:** Compute the sum of numbers from 1 to N using recursion.
* **Logic:** `sum(n) = n + sum(n-1)` with base case `sum(0)=0`.
* **Example:** Input: `5` → Output: `15`
* **Key Insight:** Demonstrates **simple mathematical pattern** in recursion.

---

## 2️⃣ Fibonacci Sequence

* **Problem:** Calculate the N-th Fibonacci number recursively.
* **Logic:** `fib(n) = fib(n-1) + fib(n-2)` with base cases `fib(0)=0, fib(1)=1`.
* **Example:** Input: `5` → Output: `5`
* **Key Insight:** Recursion naturally models **sequences with dependent subproblems**.

---

## 3️⃣ Power Set / Subset Count (Preview of Backtracking)

* **Problem:** Count all subsets of N elements recursively.
* **Logic:** `count_subsets(n) = count_subsets(n-1) + count_subsets(n-1)` for including or excluding element.
* **Example:** Input: `3` → Output: `8` subsets
* **Key Insight:** Recursive **include/exclude pattern** prepares for backtracking.

---

## 4️⃣ Power Calculation (`a^b`) — Divide & Conquer

* **Problem:** Compute `a^b` recursively using divide & conquer.
* **Logic:**

```python id="s6p1a1"
half = power(a, b//2)
if b % 2 == 0:
    return half * half
else:
    return a * half * half
```

* **Example:** Input `(3,6)` → Output: `729`
* **Key Insight:** Shows **halving the problem reduces recursion depth** → O(log n) time.

---

## 5️⃣ Count Ways to Climb Stairs (Include/Exclude Pattern)

* **Problem:** Count ways to reach the top of N steps if you can take 1 or 2 steps.
* **Logic:** `ways(n) = ways(n-1) + ways(n-2)` with base cases `ways(0)=1, ways(n<0)=0`.
* **Example:** Input: `5` → Output: `8`
* **Key Insight:** Demonstrates **recursion patterns with multiple choices** (include/exclude logic).

---

## 6️⃣ Sum of Digits

* **Problem:** Compute the sum of digits of a number recursively.
* **Logic:** `sum_digits(n) = n%10 + sum_digits(n//10)` with base case `n=0`.
* **Example:** Input: `1234` → Output: `10`
* **Key Insight:** Recursive **pattern over parts of input**, not just numeric indices.

---

## ✅ Key Skills Practiced

* Recognizing **recursion patterns**
* Divide & Conquer recursion (`a^b`)
* Include/Exclude pattern (stairs, subsets)
* Mathematical and sequence recursion
* Digit-wise recursion
* Understanding **how intermediate results are combined** during recursion

---

## 📊 Problem-Solving Approaches Summary

| Problem             | Technique Used          | Time Complexity | Space Complexity |
| ------------------- | ----------------------- | --------------- | ---------------- |
| Sum of Numbers      | Mathematical recursion  | O(n)            | O(n)             |
| Fibonacci           | Sequence recursion      | O(2^n)          | O(n)             |
| Power Set Count     | Include/Exclude         | O(2^n)          | O(n)             |
| Power a^b           | Divide & Conquer        | O(log n)        | O(log n)         |
| Count Ways (Stairs) | Include/Exclude pattern | O(2^n)          | O(n)             |
| Sum of Digits       | Part-wise recursion     | O(d)            | O(d)             |

---

## 🧠 Key Takeaways

* **Identify patterns in recursion** — sequences, sums, choices
* **Divide & conquer recursion** reduces time complexity significantly
* **Include/exclude logic** is foundational for backtracking problems
* **Intermediate results (`half`, partial sums`) are combined using return statements**
* Tracing recursion visually or using a stack diagram helps understand flow

---

## 💡 Advanced Insights

* Recursion patterns today build a bridge to **Day 19: Backtracking**
* Understanding **how to combine results from subproblems** is critical
* Memoization or iterative versions can optimize some of these recursive patterns in practice

---

This completes **Day 18 — Recursion Patterns**, covering **pattern recognition, divide & conquer, and include/exclude recursion logic**, preparing for **backtracking and combinatorial DSA problems** ✅
