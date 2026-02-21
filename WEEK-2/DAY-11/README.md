# Day 11 DSA Practice — Prefix Sum Technique

Today I focused on the **Prefix Sum technique** for arrays, which is used to **efficiently calculate subarray sums**. This practice helped me understand **preprocessing arrays, optimizing time complexity, handling edge cases, and avoiding nested loops**, which is very important for **DSA fundamentals and coding interviews**.

---

## 1️⃣ Building a Prefix Sum Array

- **Problem:** Given an array, create a prefix sum array where each index stores the sum of elements from the start up to that index.
- **Logic:**  
  Initialize the first prefix value with the first array element.  
  For every next index, add the current array value to the previous prefix sum.
- **Example:**  
  Array: `[2, 4, 6, 8, 10]`  
  Prefix: `[2, 6, 12, 20, 30]`

---

## 2️⃣ Find Sum of a Subarray (Range Sum Query)

- **Problem:** Find the sum of elements between indices `l` and `r` (inclusive).
- **Logic:**  
  If `l == 0`, the answer is directly `prefix[r]`.  
  Otherwise, subtract `prefix[l - 1]` from `prefix[r]`.
- **Formula:**  
  `sum = prefix[r] - prefix[l - 1]`
- **Example:**  
  Array: `[2, 4, 6, 8, 10]`  
  `l = 1, r = 3` → `18` (subarray `[4, 6, 8]`)

---

## 3️⃣ Why Prefix Sum Improves Performance

- **Problem:** Brute-force subarray sum calculation takes too much time for large inputs.
- **Logic:**  
  Brute force uses nested loops → **O(n²)**.  
  Prefix sum preprocesses once → **O(n)**.  
  Each query is answered in **O(1)** time.
- **Benefit:** Efficient for **multiple range sum queries**.

---

## 4️⃣ Handling Edge Case When `l = 0`

- **Problem:** Accessing `prefix[l - 1]` causes an index error when `l = 0`.
- **Logic:**  
  Use a condition check for `l == 0`.  
  This avoids invalid indexing and gives correct results.
- **Example:**  
  Sum from index `0` to `r` is already stored in `prefix[r]`.

---

## 5️⃣ Understanding Prefix Array Indexing

- **Problem:** Understanding how prefix indices relate to array indices.
- **Logic:**  
  `prefix[i]` stores sum from index `0` to `i`.  
  `prefix[i - 1]` represents sum before the current element.  
  Subtraction removes unwanted part of the array.
- **Key Insight:** Prefix sum stores **accumulated history of values**.

---

## ✅ Key Skills Practiced

- **Prefix Sum Technique** — preprocessing arrays for fast queries
- **Subarray Sum Optimization** — avoiding nested loops
- **Time Complexity Analysis** — reducing from O(n²) to O(n)
- **Index Handling** — avoiding out-of-bound errors
- **Array Traversal** — cumulative addition logic
- **Edge Case Handling** — `l = 0`, small arrays

---

This practice consolidated **Day 11 concepts** and strengthened my understanding of **prefix sum construction, range sum queries, time complexity optimization, and edge case handling**, building a strong foundation for **advanced array problems like difference arrays, 2D prefix sums, and range query optimizations**.