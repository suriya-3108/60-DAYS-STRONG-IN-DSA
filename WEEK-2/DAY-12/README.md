# Day 12 DSA Practice — String Pattern & Sliding Window Techniques

Today I focused on **string pattern problems**, especially those involving **frequency counting and sliding window techniques**. This practice helped me understand **how to detect character patterns efficiently, maintain window validity, optimize string traversal, and avoid unnecessary recomputation**, which are crucial for **DSA fundamentals, competitive programming, and coding interviews**.

---

## 1️⃣ Checking if Two Strings Are Anagrams

- **Problem:** Determine whether two strings are anagrams of each other.
- **Logic:**  
  Two strings are anagrams if they have the **same length** and **same character frequencies**.  
  Count the frequency of each character in both strings and compare the maps.
- **Example:**  
  `"listen"` & `"silent"` → `True`  
  `"rat"` & `"car"` → `False`
- **Key Insight:**  
  Frequency comparison avoids sorting and runs in **O(n)** time.

---

## 2️⃣ First Non-Repeating Character in a String

- **Problem:** Find the first character that appears only once in a string.
- **Logic:**  
  First, count the frequency of each character.  
  Then, traverse the string again to preserve the **original order** and find the first character with frequency `1`.
- **Example:**  
  Input: `"aabbcddee"`  
  Output: `c`
- **Key Insight:**  
  Always scan the string again instead of iterating the dictionary to maintain order.

---

## 3️⃣ Find All Anagrams of a Pattern in a String

- **Problem:** Find all starting indices of substrings in `s` that are anagrams of `p`.
- **Logic:**  
  Use a **fixed-size sliding window** equal to the length of `p`.  
  Maintain two frequency maps:
  - Pattern frequency
  - Current window frequency  
  
  Slide the window by:
  - Adding the right character
  - Removing the left character
- **Example:**  
  `s = "cbaebabacd", p = "abc"`  
  Output: `[0, 6]`
- **Key Insight:**  
  Update the frequency map incrementally instead of rebuilding it every time.
- **Complexity:**  
  Time → **O(n)**, Space → **O(1)**

---

## 4️⃣ Valid Palindrome Permutation

- **Problem:** Check whether any permutation of a string can form a palindrome.
- **Logic:**  
  A string can form a palindrome **if at most one character has an odd frequency**.  
  Count character frequencies and track how many have odd counts.
- **Example:**  
  `"carrace"` → `True`  
  `"aabbcd"` → `False`
- **Key Insight:**  
  Palindromes require paired characters; only one unpaired character is allowed in the center.

---

## 5️⃣ Longest Substring Without Repeating Characters

- **Problem:** Find the length of the longest substring with all unique characters.
- **Logic:**  
  Use a **variable-size sliding window** and a set.  
  Expand the window using the right pointer.  
  Shrink the window using a `while` loop until duplicates are removed.
- **Example:**  
  Input: `"abcabcbb"`  
  Output: `3` (`"abc"`)
- **Key Insight:**  
  Use `while`, not `if`, to fully remove duplicates and keep the window valid.
- **Complexity:**  
  Time → **O(n)**, Space → **O(n)**

---

## ✅ Key Skills Practiced

- **Frequency Counting** using dictionaries and sets
- **Sliding Window Technique** (fixed and variable size)
- **String Pattern Recognition**
- **Optimizing Time Complexity** from O(n²) to O(n)
- **Window Expansion and Shrinking Logic**
- **Edge Case Handling** (duplicates, empty strings, small inputs)
- **Interview-Oriented Thinking**

---

This practice consolidated **Day 12 concepts** and strengthened my understanding of **string pattern problems, anagram detection, palindrome conditions, and sliding window optimization**, forming a strong foundation for **advanced topics like hashing, substring problems, and competitive programming challenges**.