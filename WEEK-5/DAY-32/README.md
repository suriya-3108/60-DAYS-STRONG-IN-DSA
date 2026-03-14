# 📘 Day 32 DSA Practice — Linked List Basics

Today I focused on **Linked List fundamentals**, understanding how nodes are connected using **pointers instead of contiguous memory like arrays**.

The goal was to **learn the structure of linked lists and practice basic operations such as traversal and insertion**, which are foundational for solving more complex linked list problems.

This day helped strengthen my understanding of **node structures, pointer manipulation, and efficient list operations**, which are frequently used in coding interviews and real-world data structure implementations.

---

## 1️⃣ Linked List Traversal — Visiting Every Node

* **Problem:** Print all elements of a linked list starting from the head node.
* **Logic:**

  * Start with a pointer called `current` pointing to the **head node**.
  * Traverse the list using `current = current.next`.
  * Continue until `current` becomes `None`.
* **Key Insight:** Traversal is the **basic operation for accessing linked list elements**, similar to iterating through arrays.
* **Example:**

```
Input  → 10 → 20 → 30 → 40
Output → 10 20 30 40
```

* **Time Complexity:** O(n)
* **Space Complexity:** O(1)

---

## 2️⃣ Insert Node at Beginning — Constant Time Operation

* **Problem:** Insert a new node at the **start of the linked list**.
* **Logic:**

  * Create a new node.
  * Set the new node's `next` pointer to the current head.
  * Update the head to point to the new node.
* **Key Insight:** Inserting at the beginning is very efficient because **no traversal is required**.
* **Example:**

```
Before → 10 → 20 → 30 → 40
Insert → 5
After  → 5 → 10 → 20 → 30 → 40
```

* **Time Complexity:** O(1)
* **Space Complexity:** O(1)

---

## 3️⃣ Insert Node at End — Linked List Traversal

* **Problem:** Add a new node at the **end of the linked list**.
* **Logic:**

  * Traverse the list until reaching the **last node** (`current.next == None`).
  * Attach the new node by updating the last node’s `next` pointer.
* **Key Insight:** Unlike arrays, linked lists require **traversing the list to find the last node**.
* **Example:**

```
Before → 10 → 20 → 30 → 40
Insert → 50
After  → 10 → 20 → 30 → 40 → 50
```

* **Time Complexity:** O(n)
* **Space Complexity:** O(1)

---

## 4️⃣ Find Middle of Linked List — Fast & Slow Pointer Pattern

* **Problem:** Find the **middle element of a linked list**.
* **Logic:**

  * Use two pointers:

    * `slow` moves **one step at a time**
    * `fast` moves **two steps at a time**
  * When `fast` reaches the end of the list, `slow` will be at the middle.
* **Key Insight:** The **fast and slow pointer technique** is a powerful pattern used in many linked list problems.
* **Example:**

```
Input  → 10 → 20 → 30 → 40 → 50
Output → 30
```

* **Time Complexity:** O(n)
* **Space Complexity:** O(1)

---

## 5️⃣ Core Linked List Structure

A **Linked List** consists of nodes where each node contains:

```
[Data | Next Pointer]
```

Example representation:

```
10 → 20 → 30 → 40 → None
```

Unlike arrays, linked lists **do not require contiguous memory**, allowing dynamic memory allocation.

---

## 6️⃣ Edge Cases Practiced

* Handling insertion when the **linked list is empty**
* Traversing until the **last node**
* Correctly updating the **head pointer**
* Preventing errors when reaching `None`
* Managing pointer updates during insertion

---

## ✅ Key Skills Practiced

* Understanding **node structure and pointers**
* Implementing **linked list traversal**
* Performing **insertion at the beginning**
* Performing **insertion at the end**
* Using the **fast and slow pointer technique**

---

## 📊 Problem-Solving Approaches Summary

| Problem                   | Technique Used      | Time Complexity | Space Complexity |
| ------------------------- | ------------------- | --------------- | ---------------- |
| Linked List Traversal     | Pointer Iteration   | O(n)            | O(1)             |
| Insert at Beginning       | Head Pointer Update | O(1)            | O(1)             |
| Insert at End             | List Traversal      | O(n)            | O(1)             |
| Find Middle of LinkedList | Fast & Slow Pointer | O(n)            | O(1)             |

---

## 🧠 Key Takeaways

* **Linked lists store elements using nodes and pointers instead of contiguous memory.**
* **Pointer manipulation is the core skill required to solve linked list problems.**
* Inserting at the **beginning is extremely efficient (O(1))**.
* Some operations like inserting at the **end require traversal**.
* The **fast and slow pointer pattern** is widely used for problems like finding the middle, detecting cycles, and splitting lists.

---

This completes **Day 32 — Linked List Basics**, strengthening my understanding of **node structures, pointer manipulation, and fundamental linked list operations**, which are essential for solving advanced linked list problems.
