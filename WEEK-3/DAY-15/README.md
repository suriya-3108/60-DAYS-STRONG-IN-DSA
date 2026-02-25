# 📘 Day 15 DSA Practice — Hash Maps (Deep Dive)

Today I focused on **Hash Maps (Dictionaries & Sets)** and their applications in solving problems efficiently. The emphasis was on understanding **why hash maps are used**, how they reduce time complexity, and applying them to **classic interview problems** like **frequency counting, duplicate detection, Two Sum, and Group Anagrams**.

This day strengthened my ability to convert **nested-loop solutions into optimal O(n) approaches**, which is critical for **DSA fundamentals and coding interviews**.

---

## 1️⃣ Frequency Count of Elements

* **Problem:** Given a list of numbers, count how many times each element appears.
* **Logic:** Use a hash map where keys are elements and values are their counts.
* **Example:** Input: `nums = [1, 2, 2, 3, 3, 3]` → Output: `{1: 1, 2: 2, 3: 3}`
* **Key Insight:** Hash maps allow constant-time updates and lookups.
* **Complexity:** Time → **O(n)**, Space → **O(n)**

---

## 2️⃣ First Duplicate Element

* **Problem:** Find the first number that appears more than once in the list.
* **Logic:** Traverse the list and store seen elements in a hash map or set. If an element already exists, it is the first duplicate.
* **Example:** Input: `nums = [4, 1, 2, 3, 1, 5]` → Output: `1`
* **Key Insight:** Checking existence in a hash map/set is O(1).
* **Complexity:** Time → **O(n)**, Space → **O(n)**

---

## 3️⃣ Check if Array Contains Duplicate

* **Problem:** Determine if any element appears more than once.
* **Logic:** Store elements in a set while traversing. If an element is already present, a duplicate exists.
* **Example:** Input: `nums = [1, 2, 3, 4, 5]` → Output: `False`
* **Key Insight:** Sets are ideal when only existence matters (no frequency required).
* **Complexity:** Time → **O(n)**, Space → **O(n)**

---

## 4️⃣ Find Common Elements Between Two Arrays

* **Problem:** Find all elements common to two arrays.
* **Logic:** Convert one array to a set and check each element of the second array for membership.
* **Example:** Input: `a = [1, 2, 3, 4]`, `b = [3, 4, 5, 6]` → Output: `[3, 4]`
* **Key Insight:** Hash-based lookup avoids nested loops.
* **Complexity:** Time → **O(n + m)**, Space → **O(n)**

---

## 5️⃣ Two Sum (Using Hash Map)

* **Problem:** Given an array and a target, check if any two numbers add up to the target.
* **Logic:** For each number, calculate the complement (`target - current`) and check if it already exists in the hash map.
* **Example:** Input: `nums = [2, 7, 11, 15]`, `target = 9` → Output: `True`
* **Key Insight:** Hash map eliminates the need for sorting or nested loops.
* **Complexity:** Time → **O(n)**, Space → **O(n)**

---

## 6️⃣ Group Anagrams

* **Problem:** Group strings that are anagrams of each other.
* **Logic:** Use a hash map where the key is the **sorted version of the string** and the value is a list of words matching that key.
* **Example:** Input: `["eat","tea","tan","ate","nat","bat"]` → Output: `[["eat","tea","ate"], ["tan","nat"], ["bat"]]`
* **Key Insight:** Sorting removes character order, making all anagrams share the same key.
* **Complexity:** Time → **O(n × k log k)**, Space → **O(n)** (`k` = length of string)

---

## ✅ Key Skills Practiced

* **Hash Map (Dictionary) Fundamentals**
* **Set-Based Lookup**
* **Frequency Counting**
* **Duplicate Detection**
* **Complement-Based Logic (Two Sum)**
* **Grouping Data Using Hash Maps**
* **Reducing Nested Loops to O(n)**
* **Interview-Oriented Problem Solving**

---

## 📊 Problem-Solving Approaches Summary

| Problem            | Technique Used     | Time Complexity | Space Complexity |
| ------------------ | ------------------ | --------------- | ---------------- |
| Frequency Count    | Hash Map           | O(n)            | O(n)             |
| First Duplicate    | Hash Map / Set     | O(n)            | O(n)             |
| Contains Duplicate | Set                | O(n)            | O(n)             |
| Common Elements    | Set Lookup         | O(n + m)        | O(n)             |
| Two Sum            | Hash Map           | O(n)            | O(n)             |
| Group Anagrams     | Hash Map + Sorting | O(n·k log k)    | O(n)             |

---

## 🧠 Key Takeaways

* **Hash maps provide O(1) average-time lookup**
* **Keys are used only for grouping or tracking**
* **Final answers often come from hash map values**
* **Choosing the right data structure simplifies logic and improves performance**

---

This completes **Day 15 — Hash Maps deep dive**, covering essential patterns required for **DSA mastery and technical interviews** ✅