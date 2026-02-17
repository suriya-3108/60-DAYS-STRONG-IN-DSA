# Day 7 DSA Practice — Revision & Re-solving Problems

Today I focused on **revising and re-solving previous DSA problems** from Days 1–6, including **Python basics, lists, strings, dictionaries, sets, comprehensions, and easy array/string problems**. This helped improve my **problem-solving skills, logic accuracy, edge case handling, and preparation for coding interviews**.

---

## 1️⃣ Python Basics & Fundamentals

* **Sum of All Elements in a List** — Using loops and accumulation  
  *Example:* `[1, 2, 3, 4, 5]` → `15`

* **Sum of Even Numbers in a List** — Conditional accumulation using loops  
  *Example:* `[1, 2, 3, 4, 5, 6]` → `12`

* **Check Even or Odd** — Use modulus operator to determine parity  
  *Example:* `5` → `Odd`, `10` → `Even`

* **Find Maximum Number in a List** — Iterate and compare to track largest value  
  *Example:* `[1, 5, 9, 2]` → `9`

* **Palindrome Check (Without Slicing)** — Compare characters from start and end using loops  
  *Example:* `"madam"` → `Palindrome`, `"hello"` → `Not Palindrome`

---

## 2️⃣ Lists / Arrays

* **Second Largest Element** — Find second largest number using two variables  
  *Example:* `[10, 20, 4, 45, 99]` → `45`

* **Move Zeros to End** — In-place reordering to shift zeros while preserving order  
  *Example:* `[0, 1, 0, 3, 12]` → `[1, 3, 12, 0, 0]`

* **Find Maximum Repeated Element** — Count frequencies using dictionary and return most frequent  
  *Example:* `[1, 2, 2, 3, 3, 3, 4]` → `3`

* **Find All Duplicates in a List** — Use dictionary to count frequency and print elements >1  
  *Example:* `[1, 2, 3, 1, 3, 6, 6]` → `[1, 3, 6]`

* **Check Common Elements Between Two Lists** — Use sets/dictionaries to find intersecting numbers  
  *Example:* `[1, 2, 3]` & `[3, 4, 5]` → `[3]`

---

## 3️⃣ Strings

* **Character Frequency in a String** — Use dictionary to count occurrences  
  *Example:* `"programming"` → `{'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 1, 'n': 1}`

* **First Non-Repeating Character** — Track frequency, iterate string to get first unique character  
  *Example:* `"aabbcdde"` → `'c'`, `"aabbcc"` → `None`

* **Check Anagram** — Compare frequency dictionaries of two strings  
  *Example:* `"listen"` & `"silent"` → `Anagram`

* **Count Vowels in a String** — Loop through characters and check against vowel set  
  *Example:* `"hello world"` → `3`

* **Reverse Words in a Sentence** — Split string into words, reverse order, join back  
  *Example:* `"hello world from python"` → `"python from world hello"`

---

## 4️⃣ Combined / Logic Skills

* **Looping + Conditionals** — Applied nested loops for character-level and word-level operations  
* **In-Place Array Manipulation** — Practiced shifting elements without extra space using pointers  
* **Frequency Counting** — Applied dictionaries to count numbers and characters  
* **Edge Case Thinking** — Considered empty lists, all zeros, repeated characters, single-element lists, and equal-length strings  
* **Order Preservation** — Ensured first occurrence or original sequence when required

---

## ✅ Key Skills Practiced

* **Python Basics** — Variables, loops, functions, conditionals, input/output operations  
* **Lists & Arrays** — Iteration, indexing, in-place modification, sum calculations, duplicate detection  
* **Strings** — Traversal, reversal, character frequency, palindrome check, anagram check, vowel counting, word reversal  
* **Dictionaries & Sets** — Frequency counting, duplicates detection, intersections between collections  
* **Problem-Solving Patterns** — Nested loops, conditional logic, order maintenance, edge case handling  
* **Optimization Awareness** — Thinking about time (O(n)) and space (O(1)–O(n)) efficiency

---

This revision consolidates **all fundamental topics from Days 1–6**, reinforcing **Python basics, arrays, strings, dictionaries, sets, and basic problem-solving patterns**, providing a strong foundation for **future DSA topics and coding challenges**.