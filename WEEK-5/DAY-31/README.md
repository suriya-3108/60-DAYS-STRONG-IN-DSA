# 📘 Day 31 DSA Practice — Queue & Deque Patterns

Today I focused on **Queue and Deque data structures**, understanding how **FIFO (First In First Out)** processing works and how queues help manage ordered data efficiently.  

The goal was to **practice queue-based problem solving and sliding window techniques**, which are commonly used in streaming data, scheduling systems, and algorithm optimization.

This day helped strengthen my understanding of **queue operations, deque-based sliding window optimization, and data structure simulation**, which are important patterns for coding interviews.

---

## 1️⃣ Number of Recent Calls — Queue Window Pattern

* **Problem:** Design a system that counts the number of requests received in the **last 3000 milliseconds**.
* **Logic:**

  * Use a **queue (deque)** to store incoming request timestamps.
  * When a new request arrives, add it to the queue.
  * Remove timestamps that are **older than `t - 3000`**.
  * The remaining elements in the queue represent valid requests within the time window.
* **Key Insight:** A queue naturally maintains **chronological order**, making it ideal for time-based window problems.
* **Example:**

```
Input  → [1,100,3001,3002]
Output → [1,2,3,3]
```

* **Time Complexity:** O(n)
* **Space Complexity:** O(n)

---

## 2️⃣ Sliding Window Maximum — Deque Optimization

* **Problem:** Given an array and window size `k`, find the **maximum value in every sliding window**.
* **Logic:**

  * Use a **deque to store indices of useful elements**.
  * Remove indices that are **outside the current window**.
  * Remove elements smaller than the current element from the back of the deque.
  * The front of the deque always contains the **index of the maximum element** for the current window.
* **Key Insight:** Maintaining a **monotonic decreasing deque** avoids repeated maximum calculations and reduces complexity.
* **Example:**

```
Input  → nums = [1,3,-1,-3,5,3,6,7], k = 3
Output → [3,3,5,5,6,7]
```

* **Time Complexity:** O(n)
* **Space Complexity:** O(k)

---

## 3️⃣ Implement Queue using Stacks — Data Structure Simulation

* **Problem:** Implement a **queue using two stacks** while maintaining FIFO behavior.
* **Logic:**

  * Use **two stacks**:
    * `stack1` for push operations
    * `stack2` for pop and peek operations
  * When `stack2` is empty and a pop/peek operation is needed:
    * Move all elements from `stack1` to `stack2`.
  * This reversal ensures the **oldest element is removed first**.
* **Key Insight:** Transferring elements between stacks reverses order and simulates queue behavior.
* **Example:**

```
Operations → push(1), push(2), peek(), pop(), empty()
Output     → [1,1,false]
```

* **Time Complexity:** O(1) amortized
* **Space Complexity:** O(n)

---

## 4️⃣ Queue vs Deque — Core Concept

A **Queue** allows insertion at the rear and deletion from the front.

```
enqueue → add element
dequeue → remove element
```

A **Deque (Double Ended Queue)** allows insertion and deletion from **both ends**.

```
append()      → add to right
appendleft()  → add to left
popleft()     → remove from left
pop()         → remove from right
```

Deque is extremely useful for **sliding window problems and monotonic data structures**.

---

## 5️⃣ Edge Cases Practiced

* Windows smaller or larger than the array size
* Removing elements outside the sliding window
* Handling queues when they become empty
* Arrays with negative values
* Multiple elements with the same value

---

## ✅ Key Skills Practiced

* Implementing **queue operations using deque**
* Understanding **FIFO processing**
* Using **deque for sliding window optimization**
* Simulating one data structure using another
* Reducing time complexity using **efficient data structures**

---

## 📊 Problem-Solving Approaches Summary

| Problem                      | Technique Used                | Time Complexity | Space Complexity |
| ---------------------------- | ----------------------------- | --------------- | ---------------- |
| Number of Recent Calls       | Queue + Sliding Time Window   | O(n)            | O(n)             |
| Sliding Window Maximum       | Monotonic Deque               | O(n)            | O(k)             |
| Implement Queue using Stacks | Two Stack Simulation          | O(1) amortized  | O(n)             |

---

## 🧠 Key Takeaways

* **Queues are ideal for sequential processing and streaming data problems.**
* **Deque enables efficient sliding window optimization.**
* Using a **monotonic deque** avoids repeated maximum calculations.
* **Data structure simulation** (queue using stacks) helps understand underlying behavior.
* Choosing the right data structure can **reduce time complexity dramatically**.

---

This completes **Day 31 — Queue & Deque Patterns**, strengthening my understanding of **FIFO processing, sliding window optimization, and queue-based algorithm design**.
```