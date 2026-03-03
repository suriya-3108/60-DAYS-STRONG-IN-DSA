# Week 3: Hashing, Recursion & Backtracking

## 📌 Overview

Week 3 focused on **mastering three interconnected paradigms** — Hashing for efficient lookups, Recursion for breaking down problems, and Backtracking for systematic exploration of possibilities. Starting with hash map fundamentals, I progressed through recursion patterns and finally into backtracking for combinatorial problems like subsets, permutations, and combinations.

This week transformed my approach from **linear thinking to recursive problem decomposition** and built the foundation for solving **complex combinatorial problems** in coding interviews.

---

## 📚 Topics Covered Day-Wise

### [Day 15: Hash Maps — Deep Dive](./day15/readme.md)
- **Frequency Counting:** Dictionary-based element counting with O(1) updates
- **Duplicate Detection:** Sets vs maps for existence checking vs frequency needs
- **First Duplicate Element:** Order-aware duplicate detection using hash sets
- **Common Elements Between Arrays:** Set conversion + membership testing
- **Two Sum (Hash Map Approach):** Complement-based lookup eliminating nested loops
- **Group Anagrams:** Sorted string as key, list of anagrams as value

**Key Insight:** Hash maps provide O(1) average-time lookup, transforming O(n²) nested loops into O(n) solutions

**Problems Practiced:** Frequency count, first duplicate, contains duplicate, common elements, two sum, group anagrams

---

### [Day 16: Advanced Hashing & Consecutive Sequences](./day16/readme.md)
- **Contains Duplicate (Optimized):** Set with early termination for average-case improvement
- **Longest Consecutive Sequence:** Set-based approach counting only from sequence starts
- **First Repeating Element:** Two-pass approach respecting order of appearance
- **Longest Subarray with Sum = K:** Sliding window for positive numbers

**Key Insight:** For consecutive sequences, only process potential sequence starts (no left neighbor) to achieve O(n) complexity without sorting

**Problems Practiced:** Contains duplicate (optimized), longest consecutive sequence, first repeating element, longest subarray sum = K

---

### [Day 17: Recursion Basics & Call Stack](./day17/readme.md)
- **Print Numbers N→1 and 1→N:** Understanding "going down" vs "coming up" in recursion
- **Factorial:** Mathematical recursion with base case factorial(0)=1
- **Sum of First N Numbers:** Cumulative calculation through recursive decomposition
- **Power Calculation (a^b):** Repeated multiplication without loops
- **Fibonacci Sequence:** Natural sequence modeling with recursive formula
- **Sum of Digits:** Digit-wise recursion breaking number into parts
- **Count Digit Occurrences:** Conditional recursion for selective counting
- **Print Even Numbers:** Conditional recursion with filtering

**Key Insight:** Recursion is about breaking problems into smaller subproblems with clear base cases and understanding call stack behavior

**Problems Practiced:** Number printing (both orders), factorial, sum of N, power, Fibonacci, sum of digits, count digit occurrences, even number printing

---

### [Day 18: Recursion Patterns](./day18/readme.md)
- **Sum of First N Numbers (Pattern Recognition):** Simple mathematical recursion
- **Fibonacci (Sequence Pattern):** Problems with dependent subproblems
- **Power Set / Subset Count:** Include/exclude pattern (backtracking preview)
- **Power Calculation — Divide & Conquer:** Halving problem reduces depth to O(log n)
- **Count Ways to Climb Stairs:** Include/exclude with multiple choices
- **Sum of Digits:** Pattern over parts of input, not just indices

**Key Insight:** Different recursion patterns emerge — mathematical, sequence-based, include/exclude, divide & conquer, and part-wise decomposition

**Problems Practiced:** Sum of N, Fibonacci, subset count, power (divide & conquer), climb stairs, sum of digits

---

### [Day 19: Backtracking](./day19/readme.md)
- **Subsets (Power Set):** Include/exclude pattern with path.append() and path.pop()
- **Permutations:** All possible orderings using element removal and backtracking
- **Combinations of Size K:** Start index to ensure uniqueness, stop at path length = k
- **Combination Sum (Target Sum):** Running total with pruning when total > target

**Key Insight:** Backtracking = choose → explore → undo choice — systematic exploration of all possibilities with controlled recursion

**Problems Practiced:** Subsets, permutations, combinations of size k, combination sum

---

### [Day 20: Combination Problems](./day20/readme.md)
- **Combinations (n Choose k):** Start index + i+1 to move forward, no reuse
- **Combination Sum (Reuse Allowed):** Backtrack with i (not i+1) for element reuse
- **Combination Sum II (No Reuse + Duplicates):** Sorting + duplicate skipping with `i > index and candidates[i] == candidates[i-1]`

**Key Insight:** Combination problems teach controlled element selection — reuse vs non-reuse controlled by index management, duplicate handling through sorting and skipping

**Problems Practiced:** n choose k, combination sum (reuse), combination sum II (duplicate handling)

---

### [Day 21: Week 3 Revision — Hashing, Recursion & Backtracking](./day21/readme.md)
- **Hashing Review:** Two Sum (hashmap complement), Longest Consecutive Sequence (set + sequence starts)
- **Recursion Review:** Sum of digits, Power x^n (binary exponentiation — O(log n))
- **Backtracking Review:** Subsets (include/exclude), Permutations (all orderings)
- **Combination Problems Review:** Combination sum (reuse), subset sum (no reuse)

**Key Insight:** Revision consolidates pattern recognition — knowing when to use hashing vs recursion vs backtracking based on problem characteristics

**Problems Practiced:** Two sum, longest consecutive sequence, sum of digits, power x^n, subsets, permutations, combination sum, subset sum

---

## 🎯 Key Techniques Mastered

### Hashing Techniques
- ✅ **Hash Map (Dictionary) Fundamentals:** O(1) lookups and updates
- ✅ **Set-Based Operations:** Membership testing, duplicate detection
- ✅ **Frequency Counting:** Tracking occurrences with order preservation
- ✅ **Complement-Based Logic:** Two Sum and similar "pair finding" problems
- ✅ **Grouping Data:** Using transformed keys (sorted strings) for categorization

### Recursion Patterns
- ✅ **Base Case Identification:** Essential for preventing infinite recursion
- ✅ **Call Stack Understanding:** Tracing "going down" vs "coming up"
- ✅ **Mathematical Recursion:** Factorial, sum, power
- ✅ **Sequence Recursion:** Fibonacci and dependent subproblems
- ✅ **Divide & Conquer:** Halving problems for O(log n) depth
- ✅ **Part-Wise Recursion:** Breaking inputs into smaller parts (digits)

### Backtracking Patterns
- ✅ **Include/Exclude Pattern:** Foundation for subsets and combinatorial generation
- ✅ **Permutation Generation:** All possible orderings with element tracking
- ✅ **Controlled Selection:** Start index for combinations, reuse vs non-reuse
- ✅ **Pruning:** Early termination when constraints violated (total > target)
- ✅ **Duplicate Handling:** Sorting + skipping identical elements at same recursion level
- ✅ **Path Management:** Appending and popping to maintain current state

### Optimization Skills
- ✅ **Time Complexity Reduction:** O(n²) → O(n) using hash maps
- ✅ **Recursion Depth Optimization:** Divide & conquer for O(log n) instead of O(n)
- ✅ **Pruning:** Eliminating impossible branches early in backtracking
- ✅ **Memoization Awareness:** Recognizing when recursion can be optimized (Fibonacci)

---

## 📊 Complexity Patterns Summary

| Technique | Time Complexity | Space Complexity | Use Case |
|-----------|-----------------|------------------|----------|
| Hash Map Lookup | O(n) | O(n) | Frequency counting, two sum, duplicates |
| Set Operations | O(n) | O(n) | Existence checks, common elements |
| Longest Consecutive Sequence | O(n) | O(n) | Sequence finding without sorting |
| Simple Recursion | O(n) | O(n) | Factorial, sum of N, printing |
| Fibonacci (naive) | O(2ⁿ) | O(n) | Sequence problems (needs optimization) |
| Divide & Conquer Recursion | O(log n) | O(log n) | Power calculation, binary exponentiation |
| Subsets (Backtracking) | O(2ⁿ) | O(n) | All possible combinations |
| Permutations (Backtracking) | O(n!) | O(n) | All possible orderings |
| Combinations (n choose k) | O(C(n,k)) | O(k) | Fixed-size selections |
| Combination Sum | O(2ⁿ) approx | O(n) | Target sum with/without reuse |

---

## 💡 Key Takeaways

1. **Hash maps enable O(1) lookups** — Transform nested loops into linear solutions
2. **Sets are for existence, maps are for frequency** — Choose based on whether counts matter
3. **Recursion requires clear base cases** — Without them, recursion never ends
4. **"Going down" vs "coming up"** — Understanding when operations happen relative to recursive calls
5. **Divide & conquer reduces depth** — Halving problems achieves O(log n) recursion depth
6. **Backtracking = choose → explore → undo** — The universal pattern for combinatorial problems
7. **Start index controls combinations** — i+1 for no reuse, i for reuse allowed
8. **Duplicate handling requires sorting** — Then skip identical elements at same recursion level
9. **Pruning optimizes backtracking** — Stop early when constraints are violated
10. **Pattern recognition improves with practice** — Mixed revision reveals which technique fits which problem

---

## 🔗 Connections Between Topics

| Topic Connection | Why It Matters |
|------------------|----------------|
| Hash Maps → Recursion | Both decompose problems — maps by key-value, recursion by smaller instances |
| Recursion → Backtracking | Backtracking IS recursion with exploration and undo |
| Include/Exclude → Subsets | The foundation pattern for all combinatorial generation |
| Two Sum → Combination Sum | Both find pairs/sets summing to target — maps for pairs, backtracking for combinations |
| Fibonacci → Climb Stairs | Same recursive pattern applied to different contexts |
| Group Anagrams → Combinations | Both use grouping — sorted strings vs selected elements |

---

## ✅ Week 3 Progress Checklist

- [x] Day 15: Hash maps fundamentals — frequency, duplicates, two sum, group anagrams
- [x] Day 16: Advanced hashing — consecutive sequences, subarray sum, first repeating
- [x] Day 17: Recursion basics — call stack, mathematical recursion, digit problems
- [x] Day 18: Recursion patterns — include/exclude, divide & conquer, sequence patterns
- [x] Day 19: Backtracking — subsets, permutations, combinations, combination sum
- [x] Day 20: Combination problems — n choose k, reuse vs non-reuse, duplicate handling
- [x] Day 21: Comprehensive revision — all three paradigms with mixed practice

---

*This week transformed my thinking — from linear iteration to recursive decomposition and systematic exploration. Hashing taught me to trade space for time, recursion taught me to think in smaller problems, and backtracking taught me to explore systematically while learning from dead ends.*