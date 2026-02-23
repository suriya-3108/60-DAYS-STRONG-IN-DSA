# Day 13 DSA Practice — Mixed Practice Problems

Today I focused on **mixed practice problems** combining **array manipulation, two-pointer technique, sliding window, and string pattern recognition**. This practice helped me reinforce **multiple problem-solving approaches and recognize which technique to apply for different problem types**, which are crucial for **DSA fundamentals, competitive programming, and coding interviews**.

---

## 1️⃣ Rotate Array (Without Extra Array)

- **Problem:** Given an array and a number k, rotate the array to the right by k steps.
- **Logic:**  
  Perform k rotations by moving the last element to the front and shifting all elements right. Works in-place without extra array.
- **Example:**  
  Input: `arr = [1,2,3,4,5,6,7], k = 3`  
  Output: `[5,6,7,1,2,3,4]`
- **Key Insight:**  
  Moving elements from end to beginning requires careful index management to avoid overwriting.
- **Complexity:**  
  Time → **O(n*k)**, Space → **O(1)**

---

## 2️⃣ Remove Duplicates from Sorted Array

- **Problem:** Given a sorted array, remove duplicates in-place and return the new length.
- **Logic:**  
  Use two pointers: i for unique elements, n for traversal. When a new unique element is found, place it at position i+1.
- **Example:**  
  Input: `[1,1,2,2,3,4,4]`  
  Output: `[1,2,3,4]` Length = 4
- **Key Insight:**  
  The sorted property allows us to compare adjacent elements to detect duplicates.
- **Complexity:**  
  Time → **O(n)**, Space → **O(1)**

---

## 3️⃣ Maximum Sum Subarray of Size k

- **Problem:** Find the maximum sum of any contiguous subarray of size k.
- **Logic:**  
  Calculate sum of first window, then slide window by subtracting left element and adding right element, tracking maximum sum.
- **Example:**  
  Input: `arr = [2,1,5,1,3,2], k = 3`  
  Output: `9` (subarray `[5,1,3]`)
- **Key Insight:**  
  Sliding window avoids recalculating sum from scratch for each window → O(n) instead of O(n*k).
- **Complexity:**  
  Time → **O(n)**, Space → **O(1)**

---

## 4️⃣ Find All Anagrams in a String

- **Problem:** Find all starting indices where a substring is an anagram of pattern p.
- **Logic:**  
  Create frequency maps for pattern and current window. Slide window of size len(p) through s and compare frequency maps.
- **Example:**  
  Input: `s = "cbaebabacd", p = "abc"`  
  Output: `[0, 6]`
- **Key Insight:**  
  Frequency comparison is more efficient than sorting each substring.
- **Complexity:**  
  Time → **O(n)**, Space → **O(k)** where k is pattern length

---

## 5️⃣ Move All Zeros to End

- **Problem:** Move all zeros to the end while maintaining relative order of non-zero elements. Do it in-place.
- **Logic:**  
  Use two pointers: left tracks position for next non-zero. When right finds non-zero, swap with left.
- **Example:**  
  Input: `arr = [0,1,0,3,12]`  
  Output: `[1,3,12,0,0]`
- **Key Insight:**  
  Swapping ensures relative order of non-zero elements is preserved.
- **Complexity:**  
  Time → **O(n)**, Space → **O(1)**

---

## 6️⃣ Longest Substring Without Repeating Characters

- **Problem:** Find the length of the longest substring with all unique characters.
- **Logic:**  
  Use sliding window with left and right pointers. Maintain a set of characters in current window. When duplicate found, remove from left until duplicate is gone.
- **Example:**  
  Input: `s = "abcabcbb"`  
  Output: `3` (`"abc"`)
- **Key Insight:**  
  Using a set allows O(1) lookup for duplicate detection while maintaining window.
- **Complexity:**  
  Time → **O(n)**, Space → **O(n)**

---

## ✅ Key Skills Practiced

- **Array Rotation** without extra space
- **Two-Pointer Technique** for in-place operations
- **Sliding Window** (fixed and variable size)
- **Frequency Counting** using dictionaries and sets
- **String Pattern Recognition** (anagrams)
- **In-Place Array Manipulation**
- **Optimizing Time Complexity** from O(n²) to O(n)
- **Window Expansion and Shrinking Logic**
- **Edge Case Handling** (duplicates, zeros, empty strings)
- **Interview-Oriented Thinking**

---

## 📊 Problem-Solving Approaches Summary

| Problem | Technique Used | Time Complexity | Space Complexity |
|---------|---------------|-----------------|------------------|
| Rotate Array | Iterative Rotation | O(n*k) | O(1) |
| Remove Duplicates | Two-Pointer | O(n) | O(1) |
| Max Sum Subarray | Sliding Window (Fixed) | O(n) | O(1) |
| Find Anagrams | Sliding Window + Frequency Map | O(n) | O(k) |
| Move Zeros | Two-Pointer (Swap) | O(n) | O(1) |
| Longest Substring | Sliding Window (Variable) + Set | O(n) | O(n) |

---

This practice consolidated **Day 13 concepts** and strengthened my understanding of **mixed problem types**, helping me build the intuition to **identify the right technique for each problem** — a crucial skill for **coding interviews and competitive programming challenges**.