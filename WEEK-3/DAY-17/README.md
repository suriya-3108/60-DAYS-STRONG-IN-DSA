# 📘 Day 17 DSA Practice — Recursion Basics & Call Stack

Today I focused on **Recursion Fundamentals**, exploring **how functions call themselves**, the **call stack**, and how **problems can be broken down into smaller subproblems**. The emphasis was on understanding **base cases, recursive calls, and the order of execution**, which is crucial for solving many algorithmic problems efficiently.

This day strengthened my ability to **trace recursive calls**, identify **base vs recursive cases**, and implement **mathematical, sequence, and conditional recursive solutions** — a core skill for **DSA and coding interviews**.

---

## 1️⃣ Print Numbers from N to 1

* **Problem:** Print numbers from N down to 1 using recursion.
* **Logic:** Print number → recursive call with `n-1`.
* **Example:** Input: `5` → Output: `5 4 3 2 1`
* **Key Insight:** Printing happens before the recursive call ("going down" the recursion).

---

## 2️⃣ Print Numbers from 1 to N

* **Problem:** Print numbers from 1 up to N using recursion.
* **Logic:** Recursive call with `n-1` → print number.
* **Example:** Input: `5` → Output: `1 2 3 4 5`
* **Key Insight:** Printing happens after the recursive call ("coming up" the recursion).

---

## 3️⃣ Factorial of a Number

* **Problem:** Compute `n!` recursively.
* **Logic:** `factorial(n) = n * factorial(n-1)` with base case `factorial(0) = 1`.
* **Example:** Input: `5` → Output: `120`
* **Key Insight:** Each recursive call multiplies the number by the result of the smaller subproblem, demonstrating how recursion "builds up" solutions.

---

## 4️⃣ Sum of First N Numbers

* **Problem:** Compute the sum of numbers from 1 to N recursively.
* **Logic:** `sum(n) = n + sum(n-1)` with base case `sum(0) = 0`.
* **Example:** Input: `5` → Output: `15`
* **Key Insight:** Recursion simplifies cumulative calculations by delegating the smaller problem to itself.

---

## 5️⃣ Power Calculation (`a^b`)

* **Problem:** Compute `a` raised to the power `b` recursively.
* **Logic:** `power(a, b) = a * power(a, b-1)` with base case `b = 0 → 1`.
* **Example:** Input: `(2, 3)` → Output: `8`
* **Key Insight:** Recursion handles repeated multiplication systematically without loops.

---

## 6️⃣ Fibonacci Sequence

* **Problem:** Print or calculate the first N Fibonacci numbers using recursion.
* **Logic:** `fib(n) = fib(n-1) + fib(n-2)` with base cases `fib(0)=0, fib(1)=1`.
* **Example:** Input: `6` → Output: `0 1 1 2 3 5`
* **Key Insight:** Recursion models sequences naturally but repeated calls highlight the need for optimization (like iterative or memoization approaches).

---

## 7️⃣ Sum of Digits of a Number

* **Problem:** Compute the sum of digits of a number recursively.
* **Logic:** `sum_digits(n) = n%10 + sum_digits(n//10)` with base case `n=0`.
* **Example:** Input: `1234` → Output: `10`
* **Key Insight:** Recursion breaks the problem into smaller subparts (last digit + remaining number).

---

## 8️⃣ Count Occurrences of a Digit in a Number

* **Problem:** Count how many times a digit appears in a number recursively.
* **Logic:** Check last digit → add 1 if it matches → recursive call on remaining number.
* **Example:** Input: `(1223, 2)` → Output: `2`
* **Key Insight:** Recursive accumulation eliminates the need for loops or global counters.

---

## 9️⃣ Print All Even Numbers from N to 1

* **Problem:** Print all even numbers in descending order recursively.
* **Logic:** Check if current number is even → print → call function for `n-1`.
* **Example:** Input: `6` → Output: `6 4 2`
* **Key Insight:** Conditional recursion allows selective processing of elements.

---

## ✅ Key Skills Practiced

* **Understanding base cases and recursive calls**
* **Tracing recursion and call stack behavior**
* **Mathematical recursion (factorial, sum, power)**
* **Sequence recursion (Fibonacci, digits sum, count occurrences)**
* **Conditional recursion (even numbers)**
* **Thinking in terms of "smaller subproblems"**

---

## 📊 Problem-Solving Approaches Summary

| Problem | Technique Used | Time Complexity | Space Complexity |
|---------|----------------|------------------|-------------------|
| Print Numbers N → 1 | Simple recursion | O(n) | O(n) |
| Print Numbers 1 → N | Simple recursion | O(n) | O(n) |
| Factorial | Mathematical recursion | O(n) | O(n) |
| Sum of Numbers | Mathematical recursion | O(n) | O(n) |
| Power a^b | Recursive multiplication | O(b) | O(b) |
| Fibonacci | Recursive formula | O(2^n) | O(n) |
| Sum of Digits | Digit-wise recursion | O(d) | O(d) |
| Count Digit Occurrences | Digit-wise recursion | O(d) | O(d) |
| Print Even Numbers N → 1 | Conditional recursion | O(n) | O(n) |

---

## 🧠 Key Takeaways

* **Recursion is all about breaking problems into smaller subproblems**
* **Base case is essential** to prevent infinite recursion
* **"Going down" vs "coming up"** helps understand how prints or calculations happen
* **Conditional recursion** enables selective operations
* **Tracing the call stack** is critical for debugging recursive solutions
* **Recursion often has higher space usage** due to function call stack

---

## 💡 Advanced Insights

* Recursive problems can be **mathematical, sequence-based, or conditional**
* Understanding recursion today sets the stage for **Day 18: Recursion Patterns**, where we'll apply these concepts to **pyramid/triangle patterns, nested structures, and more complex recursive outputs**
* Optimizing recursion (like memoization) will be key for sequences like Fibonacci in future practice

---

This completes **Day 17 — Recursion Basics & Call Stack**, covering all fundamental recursion concepts and problems needed for **DSA mastery and technical interviews** ✅