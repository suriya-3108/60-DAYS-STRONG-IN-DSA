# Week 1: Python DSA Fundamentals

## 📌 Overview

Week 1 focused on building a **strong foundation in Python programming** and **essential DSA concepts**. Starting from Python basics, I progressed through data structures (lists, tuples, strings, dictionaries, sets), advanced Python features, complexity analysis, and finally consolidated everything through revision and problem-solving.

This week established the **core fundamentals** needed for tackling more complex DSA topics ahead.

---

## 📚 Topics Covered Day-Wise

### [Day 1: Python Basics](./day1/readme.md)
- Variables, data types, and basic operations
- Loops: `for` and `while`
- Conditional statements: `if`, `elif`, `else`
- Functions: definition, calling, return values
- Basic math operations and logic building

**Problems Practiced:** Numbers divisible by 3 and 5, prime check, second largest number, reverse a number, factorial, sum of digits, Armstrong number, Fibonacci sequence, sum of even/odd digits, count digits

---

### [Day 2: Lists, Tuples, Strings & Slicing](./day2/readme.md)
- **Lists:** Sum of elements, count even/odd numbers, find largest element, reverse a list, remove duplicates, rotate list right by 1, second largest element, merge two lists & remove duplicates, frequency of elements
- **Tuples:** Access elements, count occurrence, find index, tuple → list → modify → tuple conversion
- **Strings:** Count vowels and consonants, palindrome check, reverse string, first half & second half, swap first & last characters, replace vowels with `*`, remove duplicate characters, characters at even/odd index, word count

---

### [Day 3: Dictionaries & Sets](./day3/readme.md)
- **Dictionaries:** Character frequency in a string, most frequent number in a list, first non-repeating character, anagram check using dictionaries
- **Sets:** Find all duplicates in a list, first duplicate element, lookup optimization with set membership
- **Combined Problems:** Handling case and spaces, order preservation, frequency comparison

---

### [Day 4: Advanced Python — Comprehensions & Collections](./day4/readme.md)
- **List Comprehensions:** Basic, conditional, if-else, nested, flattening 2D lists
- **Dictionary Comprehensions:** Basic, conditional, swapping keys & values, filtering, creating dictionary from lists
- **Collections Module:**
  - `Counter` — Frequency counting, most common elements, anagram checks
  - `defaultdict` — Grouping items, avoiding KeyError
  - `deque` — Double-ended queue operations (append, appendleft, pop, popleft)
  - `OrderedDict` — Preserving insertion order

---

### [Day 5: Time & Space Complexity — Big O Analysis](./day5/readme.md)
- **What is Big O Notation?** — Describing algorithm growth rate
- **Why Complexity Analysis Matters** — Scalability and performance
- **Common Time Complexities:** O(1), O(log n), O(n), O(n log n), O(n²), O(2ⁿ), O(n!)
- **Space Complexity:** Measuring additional memory usage
- **Rules of Big O:** Drop constants, drop non-dominant terms, different inputs → different variables
- **Code Examples:** O(1), O(n), O(n²), O(log n), O(n log n) implementations
- **Space Complexity Examples:** O(1), O(n), O(n²) space usage

---

### [Day 6: Easy Problems on Arrays & Strings](./day6/readme.md)
- **Arrays/Lists:** Second largest element, move zeros to end, sum of all elements, sum of even numbers, find all duplicates in a list
- **Strings:** Character frequency in a string, check anagram, longest word in a list, count vowels in list of strings
- **Combined Skills:** Looping + conditionals, in-place array manipulation, frequency counting, edge case thinking

---

### [Day 7: Revision & Re-solving Problems](./day7/readme.md)
- **Python Basics Recap:** Sum of all elements, sum of even numbers, check even or odd, find maximum number, palindrome check (without slicing)
- **Lists/Arrays Recap:** Second largest element, move zeros to end, find maximum repeated element, find all duplicates, check common elements between two lists
- **Strings Recap:** Character frequency, first non-repeating character, check anagram, count vowels, reverse words in a sentence
- **Reinforced Concepts:** Looping + conditionals, in-place manipulation, frequency counting, edge case handling, order preservation

---

## 🎯 Key Skills Acquired

### Programming Fundamentals
- ✅ Python syntax and basic operations
- ✅ Loop constructs (`for`, `while`) and conditionals
- ✅ Function definition and reuse
- ✅ Input/output handling

### Data Structures
- ✅ **Lists:** Creation, traversal, modification, in-place operations, indexing
- ✅ **Tuples:** Immutable sequences, access methods, count and index operations
- ✅ **Strings:** Manipulation, slicing, character-level operations, word processing
- ✅ **Dictionaries:** Key-value mapping, frequency counting, dictionary comparison
- ✅ **Sets:** Uniqueness, membership testing, duplicate detection, set operations

### Advanced Python
- ✅ **List Comprehensions:** Basic, conditional, nested, flattening
- ✅ **Dictionary Comprehensions:** Conditional, key-value swapping, filtering
- ✅ **Collections Module:** Counter, defaultdict, deque, OrderedDict
- ✅ **Efficient coding patterns** — reducing loops, avoiding KeyError

### Algorithm Analysis
- ✅ **Big O notation** understanding and application
- ✅ **Time complexity** identification for different algorithms
- ✅ **Space complexity** awareness and measurement
- ✅ **Optimization mindset** — trading space for time when beneficial

### Problem-Solving
- ✅ **Pattern recognition:** Frequency counting, two-pointer technique, in-place modification
- ✅ **Edge case handling:** Empty inputs, duplicates, single elements, all zeros
- ✅ **Order preservation** techniques for maintaining sequence
- ✅ **Logic building** through varied problem types

---

## 📊 Complexity Summary Table

| Operation Type | Time Complexity | Space Complexity | Example |
|----------------|-----------------|------------------|---------|
| Access by index | O(1) | O(1) | `arr[i]` |
| Simple loop | O(n) | O(1) | Sum of array |
| Nested loops | O(n²) | O(1) | Bubble sort, print pairs |
| Binary search | O(log n) | O(1) | Search in sorted array |
| Merge sort | O(n log n) | O(n) | Divide & conquer sort |
| Dictionary lookup | O(1) average | O(n) | Hash table operations |
| Set membership | O(1) average | O(n) | Duplicate detection |
| String reversal | O(n) | O(1) or O(n) | In-place possible |
| List comprehension | O(n) | O(n) | Creating new list |

---

## 💡 Key Takeaways

1. **Foundations matter** — Strong Python basics make DSA learning smoother and more effective
2. **Practice consistently** — Each day builds upon previous concepts, creating a solid learning spiral
3. **Understand complexity** — Big O helps write efficient, scalable code that performs well with large inputs
4. **Edge cases are important** — Robust code handles all inputs, not just the happy path
5. **Revision solidifies learning** — Re-solving problems reinforces concepts and reveals gaps in understanding
6. **Python's built-in features** — Comprehensions and collections module enable concise, efficient, and readable code
7. **In-place operations** — Save space when possible, but know the trade-offs with readability and complexity
8. **Frequency counting pattern** — Dictionaries are powerful tools for counting and tracking occurrences
9. **Practice with examples** — Working through concrete examples helps internalize abstract concepts

---

## ✅ Week 1 Progress Checklist

- [x] Day 1: Python basics and fundamental programs completed
- [x] Day 2: Lists, tuples, strings operations practiced thoroughly
- [x] Day 3: Dictionaries and sets for frequency problems mastered
- [x] Day 4: Comprehensions and collections module understood and applied
- [x] Day 5: Big O analysis fundamentals clear with examples
- [x] Day 6: Array and string problems solved with various techniques
- [x] Day 7: All concepts revised and reinforced through re-solving

---

*This week established the essential foundation for DSA journey — mastering Python fundamentals, data structures, complexity analysis, and problem-solving patterns.*