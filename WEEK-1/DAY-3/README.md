# Day 3 DSA Practice — Dictionaries & Sets

Today I focused on strengthening my **Python DSA fundamentals** by practicing **dictionaries and sets**, including frequency counting, lookups, and duplicate detection. This helped improve my **problem-solving skills, logic building, and optimization techniques**.

---

## 1️⃣ Dictionaries

* **Character Frequency in a String** — Count occurrences of each character using a dictionary  
  *Example:* `"banana"` → `{'b': 1, 'a': 3, 'n': 2}`

* **Most Frequent Number in a List** — Find the number with the highest frequency  
  *Example:* `[1, 2, 2, 3, 1, 2, 4]` → `2`

* **First Non-Repeating Character** — Track character frequency to identify the first unique element  
  *Example:* `"aabbcdde"` → `c`

* **Anagram Check Using Dictionaries** — Build frequency dictionaries for two strings and compare using `==`  
  *Example:* `"listen"` & `"silent"` → `True`

---

## 2️⃣ Sets

* **Find All Duplicates in a List** — Use two sets (seen and duplicates) to track repeated elements  
  *Example:* `[1, 2, 3, 2, 4, 1, 5]` → `{1, 2}`

* **First Duplicate Element** — Detect the first repeated element efficiently using a set and break  
  *Example:* `[3, 5, 1, 4, 5, 2]` → `5`

* **Lookup Optimization** — Use set membership for O(1) lookup instead of nested loops

---

## 3️⃣ Combined Problems

* **Handling Case and Spaces** — Normalize strings before counting frequencies for problems like anagrams

* **Order Preservation** — For first non-repeating character, iterate string to maintain original order

* **Frequency Comparison** — Compare two frequency dictionaries directly with `==` to determine equality

---

## ✅ Key Skills Practiced

* **Dictionaries** — Frequency counting, key-value mapping, dictionary comparison  
* **Sets** — Duplicate detection, fast membership checking, first duplicate detection  
* Problem-solving patterns for strings and lists  
* **Optimization** — Reducing nested loops → O(n) solutions  
* Translating problem ideas into efficient Python code

---

This practice covers **all fundamental operations with dictionaries and sets**, forming a strong foundation for **future DSA topics** like hashing, frequency-based problems, and efficient lookups.