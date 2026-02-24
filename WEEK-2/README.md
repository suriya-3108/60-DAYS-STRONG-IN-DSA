# Week 2: Arrays, Strings & Core Algorithmic Techniques

## 📌 Overview

Week 2 focused on **mastering fundamental algorithmic techniques** for arrays and strings — the building blocks of coding interviews. Starting with array traversal and manipulation, I progressed through **two-pointer technique, sliding window, prefix sum, string pattern problems**, and finally consolidated everything through revision and mixed practice problems.

This week transformed my approach from **basic operations to optimized, interview-ready solutions** using core algorithmic patterns.

---

## 📚 Topics Covered Day-Wise

### [Day 8: Arrays & Strings — Traversal & Manipulation](./day8/readme.md)
- **Array Traversal & Basic Operations:** Reverse an array, left rotate by k, move zeros to end
- **Array Manipulation & Two-Pointer Thinking:** Stable even-odd partition, maximum product of two elements, find min/max in single pass, remove all occurrences of a value (in-place)
- **Combined/Logic Skills:** In-place manipulation, frequency counting, edge case thinking, order preservation
- **Key Insight:** O(n) solutions for rotations, max product, and min/max problems through efficient traversal

**Problems Practiced:** Reverse array, left rotation, move zeros, even-odd partition, max product pair, min-max find, remove element

---

### [Day 9: Two-Pointer Technique](./day9/readme.md)
- **Two Sum (Sorted Array):** Left/right pointers moving based on sum comparison
- **Pair with Given Sum (Unsorted Array):** Sort + two-pointer approach
- **Remove Duplicates from Sorted Array:** Slow/fast pointers for in-place overwriting
- **Move Zeros to End:** Two-pointer swap preserving non-zero order
- **Squared Sorted Array:** Compare absolute values from both ends
- **Remove Specific Element In-Place:** Slow pointer overwrites target values
- **Reverse Words in a String:** Split, two-pointer reverse, join
- **Palindrome Check:** Left/right character comparison ignoring spaces/punctuation

**Key Insight:** Two pointers reduce nested loops to single pass O(n) with O(1) space

---

### [Day 10: Sliding Window Technique](./day10/readme.md)
- **Fixed-Size Window:** Maximum sum subarray of size k, average of all subarrays of size k
- **Variable-Size Window:** Smallest subarray with sum ≥ target
- **String Sliding Window:** Longest substring without repeating characters, longest substring with at most k distinct characters
- **Deque Optimization:** Maximum of all subarrays of size k using deque

**Key Insight:** Sliding window transforms O(n²) brute force into O(n) efficient solutions by reusing computations

**Problems Practiced:** Max sum subarray (k), subarray averages, smallest subarray with sum ≥ target, longest substring without repeats, longest substring with k distinct chars, max in sliding window

---

### [Day 11: Prefix Sum Technique](./day11/readme.md)
- **Building Prefix Sum Array:** Cumulative sums from start to each index
- **Range Sum Queries:** O(1) subarray sum calculation using `prefix[r] - prefix[l-1]`
- **Performance Improvement:** O(n²) brute force → O(n) preprocessing + O(1) per query
- **Edge Case Handling:** Special condition for l = 0 to avoid index errors
- **Index Understanding:** Relationship between prefix array and original array indices

**Key Insight:** Prefix sum enables constant-time subarray sum queries after linear preprocessing

**Problems Practiced:** Prefix array construction, range sum queries (multiple), subarray sum optimization

---

### [Day 12: String Pattern & Sliding Window Techniques](./day12/readme.md)
- **Anagram Checking:** Frequency map comparison for O(n) detection
- **First Non-Repeating Character:** Frequency counting + second pass for order preservation
- **Find All Anagrams in a String:** Fixed-size sliding window + frequency maps
- **Valid Palindrome Permutation:** At most one odd frequency character
- **Longest Substring Without Repeating Characters:** Variable window + set with while loop for duplicate removal

**Key Insight:** String pattern problems combine frequency counting with sliding window for optimal solutions

**Problems Practiced:** Anagram check, first non-repeating character, all anagram indices, palindrome permutation, longest unique substring

---

### [Day 13: Mixed Practice Problems](./day13/readme.md)
- **Rotate Array (Without Extra Array):** Iterative in-place rotation
- **Remove Duplicates from Sorted Array:** Two-pointer technique
- **Maximum Sum Subarray of Size k:** Fixed sliding window
- **Find All Anagrams in a String:** Sliding window + frequency map
- **Move All Zeros to End:** Two-pointer swapping
- **Longest Substring Without Repeating Characters:** Variable sliding window + set

**Key Insight:** Recognizing which technique to apply for different problem types through mixed practice

**Problems Practiced:** Array rotation, duplicate removal, max sum subarray, anagram finding, zero movement, longest unique substring

---

### [Day 14: Revision + Mock Practice](./day14/readme.md)
- **Longest Subarray with Sum = K:** Brute-force and prefix sum approaches
- **Move All Zeros to End:** Two-pointer in-place
- **Maximum Sum Subarray of Size k:** Sliding window
- **Count Subarrays with Sum = K:** Brute-force counting
- **Check if Two Strings are Anagrams:** Frequency map
- **First Unique Character in a String:** Frequency + order preservation
- **Maximum Average Subarray of Size k:** Sliding window

**Key Insight:** Revision reinforces pattern recognition and technique selection across problem types

**Problems Practiced:** Longest subarray with sum K, zero movement, max sum subarray, subarray counting, anagram check, first unique char, max average subarray

---

## 🎯 Key Techniques Mastered

### Algorithmic Patterns
- ✅ **Two-Pointer Technique:** Left/right scanning, slow/fast pointers, in-place modification
- ✅ **Sliding Window:** Fixed-size and variable-size windows for arrays and strings
- ✅ **Prefix Sum:** Preprocessing for O(1) range sum queries
- ✅ **Frequency Counting:** Dictionaries/sets for character and element tracking
- ✅ **In-Place Manipulation:** Rotations, removals, swaps without extra space

### Array/String Operations
- ✅ **Traversal & Indexing:** Single pass, multiple passes, bidirectional traversal
- ✅ **Rotations:** Left/right shift, in-place rotation techniques
- ✅ **Partitioning:** Stable even-odd, move zeros, duplicate removal
- ✅ **Extreme Value Tracking:** Min, max, second max in single pass
- ✅ **Subarray Problems:** Sum, average, maximum, counting

### Optimization Skills
- ✅ **Time Complexity Reduction:** O(n²) → O(n) using two pointers, sliding window, prefix sum
- ✅ **Space Efficiency:** O(1) in-place operations when possible
- ✅ **Deque Usage:** O(n) sliding window maximum
- ✅ **Memoization:** Reusing computations instead of recalculating

### Problem-Solving Mindset
- ✅ **Pattern Recognition:** Identifying which technique fits each problem
- ✅ **Edge Case Handling:** Empty inputs, duplicates, zeros, single elements
- ✅ **Order Preservation:** Maintaining sequence when required
- ✅ **Multiple Approaches:** Brute force → optimization → optimal solution

---

## 📊 Complexity Patterns Summary

| Technique | Time Complexity | Space Complexity | Use Case |
|-----------|-----------------|------------------|----------|
| Basic Traversal | O(n) | O(1) | Simple operations, find min/max |
| Two-Pointer | O(n) | O(1) | Sorted arrays, duplicates, partitioning |
| Sliding Window (Fixed) | O(n) | O(1) | Subarray sums/averages of size k |
| Sliding Window (Variable) | O(n) | O(n) | Longest substring, smallest subarray |
| Prefix Sum | O(n) preprocess + O(1) query | O(n) | Multiple range sum queries |
| Frequency Map | O(n) | O(k) where k = distinct elements | Anagrams, duplicates, counting |
| Deque + Sliding Window | O(n) | O(k) | Max/min in all subarrays of size k |
| Brute Force | O(n²) or worse | O(1) | Small inputs, baseline understanding |

---

## 💡 Key Takeaways

1. **Techniques over syntax** — Week 2 shifted from Python basics to algorithmic thinking patterns
2. **Two-pointer is versatile** — Works for sorted/unsorted arrays, strings, in-place modifications
3. **Sliding window eliminates recomputation** — Reusing window sums/counts is the key to O(n) solutions
4. **Prefix sum enables O(1) queries** — Linear preprocessing pays off for multiple queries
5. **Frequency maps + sliding window** — Powerful combination for string pattern problems
6. **In-place operations save space** — But require careful index management and order preservation
7. **Edge cases reveal robustness** — Always test empty arrays, duplicates, zeros, single elements
8. **Pattern recognition improves with practice** — Mixed problems help build intuition for technique selection
9. **Optimization is incremental** — Start with brute force, then identify redundancies to eliminate
10. **Revision solidifies learning** — Re-solving problems reveals gaps and reinforces patterns

---

## ✅ Week 2 Progress Checklist

- [x] Day 8: Array traversal, manipulation, in-place operations mastered
- [x] Day 9: Two-pointer technique applied to multiple problem types
- [x] Day 10: Sliding window (fixed and variable) thoroughly practiced
- [x] Day 11: Prefix sum construction and range queries understood
- [x] Day 12: String patterns and sliding window combinations mastered
- [x] Day 13: Mixed practice — recognizing and applying appropriate techniques
- [x] Day 14: Comprehensive revision and mock practice completed

---

*This week transformed my problem-solving approach — from basic operations to optimized, pattern-based solutions ready for coding interviews.*