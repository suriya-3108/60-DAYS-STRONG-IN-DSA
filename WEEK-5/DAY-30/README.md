# 📘 Day 30 DSA Practice — Stack Patterns (Next Greater Element)

Today I focused on **Stack-based problem-solving patterns**, specifically the **Next Greater Element pattern**. The goal was to **understand how stacks can optimize brute-force comparisons** by efficiently tracking elements waiting for a greater value.

This day helped strengthen my understanding of **monotonic stacks, index tracking, and pattern-based problem solving**, which are frequently used in coding interviews and real-world algorithm design.

---

## 1️⃣ Next Greater Element I — Stack Pattern

* **Problem:** For each element in `nums1`, find the **next greater element** to its right in `nums2`.
* **Logic:**

  * Use a **monotonic decreasing stack** to track numbers whose next greater element has not yet been found.
  * Traverse `nums2`.
  * When a greater element appears, pop elements from the stack and map them to the current greater number.
  * Store results in a **dictionary (hash map)**.
* **Key Insight:** Instead of checking every element repeatedly, a stack helps determine the next greater element in **one pass**.
* **Example:**

```
nums1 = [4,1,2]
nums2 = [1,3,4,2]

Output → [-1,3,-1]
```

* **Time Complexity:** O(n)
* **Space Complexity:** O(n)

---

## 2️⃣ Daily Temperatures — Stack with Index Tracking

* **Problem:** Given daily temperatures, determine **how many days until a warmer temperature** occurs.
* **Logic:**

  * Use a stack to store **indices of days**.
  * Traverse the temperature array.
  * If the current temperature is greater than the temperature at the index on top of the stack:

    * Pop the index
    * Calculate the waiting days using `current_index - previous_index`.
* **Key Insight:** Using indices allows us to compute the **distance between days**.
* **Example:**

```
Input  → [73,74,75,71,69,72,76,73]
Output → [1,1,4,2,1,1,0,0]
```

* **Time Complexity:** O(n)
* **Space Complexity:** O(n)

---

## 3️⃣ Next Greater Element II — Circular Array

* **Problem:** Find the next greater element for each number in a **circular array**.
* **Logic:**

  * Traverse the array **twice** (`2 * n`) to simulate circular behavior.
  * Use `i % n` to access the original index.
  * Maintain a **monotonic stack** to track unresolved elements.
  * Only push indices during the **first pass**.
* **Key Insight:** Circular arrays can be handled efficiently by **simulating an extended traversal**.
* **Example:**

```
Input  → [1,2,1]
Output → [2,-1,2]
```

* **Time Complexity:** O(n)
* **Space Complexity:** O(n)

---

## 4️⃣ Monotonic Stack Pattern — Core Concept

A **monotonic stack** maintains elements in either **increasing or decreasing order**.

For Next Greater Element problems:

```
while stack and current > stack_top:
    pop stack
push current element
```

This pattern helps solve problems involving:

* Next Greater Element
* Daily Temperatures
* Stock Span
* Largest Rectangle in Histogram

---

## 5️⃣ Edge Cases Practiced

* Elements with **no greater value**
* Circular array wrap-around
* Arrays with repeated values
* Single-element arrays
* Strictly increasing or decreasing sequences

---

## ✅ Key Skills Practiced

* Using **stacks for efficient element comparison**
* Implementing the **monotonic stack pattern**
* Working with **indices vs values in stack problems**
* Handling **circular arrays**
* Reducing time complexity from **O(n²) → O(n)**

---

## 📊 Problem-Solving Approaches Summary

| Problem                 | Technique Used                       | Time Complexity | Space Complexity |
| ----------------------- | ------------------------------------ | --------------- | ---------------- |
| Next Greater Element I  | Monotonic stack + hash map           | O(n)            | O(n)             |
| Daily Temperatures      | Stack with index tracking            | O(n)            | O(n)             |
| Next Greater Element II | Monotonic stack + circular traversal | O(n)            | O(n)             |

---

## 🧠 Key Takeaways

* **Stacks help avoid repeated comparisons**, reducing time complexity significantly.
* The **monotonic stack pattern** is a powerful technique used in many interview problems.
* Storing **indices instead of values** is useful when distance or position calculations are needed.
* Circular arrays can be handled by **iterating twice and using modulo indexing**.
* Mastering stack patterns helps solve many **range and comparison-based problems efficiently**.

---

This completes **Day 30 — Stack Patterns**, strengthening my understanding of **monotonic stacks, next greater element patterns, and optimized array traversal techniques**.
