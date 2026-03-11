# 📘 Day 29 DSA Practice — Stack Basics & Problems

Today I focused on **Stack Basics**, learning how to efficiently use stacks for problem-solving in Python. The goal was to **strengthen problem-solving using the LIFO principle**, including implementing a stack, validating parentheses, removing adjacent duplicates, and simulating stack operations for scoring problems.

This day helped consolidate my understanding of **stack operations, edge cases, and practical patterns**, which are essential for coding interviews and algorithmic thinking.

---

## 1️⃣ Implement Stack Using Python List

* **Problem:** Create a Stack class with `push`, `pop`, `peek`, `is_empty`, and `size` methods.
* **Logic:**

  * Use a Python list to store elements.
  * `push(x)` → `append(x)`
  * `pop()` → remove last element if stack not empty
  * `peek()` → return last element without removing
  * `is_empty()` → check if list length is 0
  * `size()` → return length of list
* **Example:**

```python
s = Stack()
s.push(10)
s.push(20)
print(s.peek())     # 20
print(s.pop())      # 20
print(s.size())     # 1
```

* **Time Complexity:** O(1) per operation
* **Space Complexity:** O(n)

---

## 2️⃣ Valid Parentheses

* **Problem:** Given a string containing only `()[]{}`, return True if the brackets are valid.
* **Logic:**

  * Use a stack to store opening brackets.
  * For closing brackets, check if the top of stack matches the corresponding opening bracket.
  * Return False if mismatch or stack empty at any point.
  * Return True if stack is empty after processing.
* **Example:** `"()[]{}"` → True, `"(]"` → False
* **Time Complexity:** O(n)
* **Space Complexity:** O(n)

---

## 3️⃣ Remove Adjacent Duplicates in String

* **Problem:** Remove adjacent duplicate characters repeatedly from a string.
* **Logic:**

  * Traverse string character by character.
  * If current character equals stack top → pop.
  * Else → push current character.
  * Return `''.join(stack)` at the end.
* **Example:** `"abbaca"` → `"ca"`
* **Time Complexity:** O(n)
* **Space Complexity:** O(n)

---

## 4️⃣ Baseball Game (Stack Simulation)

* **Problem:** Simulate scoring rules using stack operations.
* **Rules:**

  * Number → push score
  * `"C"` → remove last score
  * `"D"` → double last score
  * `"+"` → sum last two scores
* **Logic:**

  * Use a stack to track scores.
  * Apply each operation according to rules.
  * Return sum of final stack.
* **Example:** `["5","2","C","D","+"]` → 30
* **Time Complexity:** O(n)
* **Space Complexity:** O(n)

---

## 5️⃣ Edge Cases Practiced

* Empty string for parentheses
* Only opening or only closing brackets
* Strings with all duplicates
* Negative numbers in Baseball Game
* Operations starting with `"+"` or `"D"` when stack has fewer elements

---

## ✅ Key Skills Practiced

* Stack implementation using Python list
* LIFO principle and stack operations (`push`, `pop`, `peek`)
* Matching patterns using stack (parentheses, duplicates)
* Stack simulation for algorithmic problems
* Handling edge cases and constraints efficiently

---

## 📊 Problem-Solving Approaches Summary

| Topic                      | Technique Used               | Time Complexity    | Space Complexity |
| -------------------------- | ---------------------------- | ------------------ | ---------------- |
| Stack Implementation       | Python list + class methods  | O(1) per operation | O(n)             |
| Valid Parentheses          | Stack + dictionary matching  | O(n)               | O(n)             |
| Remove Adjacent Duplicates | Stack for character tracking | O(n)               | O(n)             |
| Baseball Game              | Stack simulation             | O(n)               | O(n)             |

---

## 🧠 Key Takeaways

* Stacks are **fundamental LIFO data structures** widely used in coding interviews.
* Using a stack helps **simplify problems involving sequences, reversals, and pattern matching**.
* Many advanced problems (Next Greater Element, expression evaluation) build directly on these patterns.
* Understanding **when to push, pop, and peek** is crucial for efficient problem-solving.

---

This completes **Day 29 — Stack Basics**, reinforcing **stack implementation, pattern recognition, and simulation techniques** for coding interviews and algorithmic thinking.
