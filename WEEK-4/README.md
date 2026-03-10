# Week 4: Searching & Sorting

## 📌 Overview

Week 4 focused on **core searching and sorting algorithms**, which form the backbone of many data structure and algorithm problems. The week started with **basic search techniques**, progressed through **binary search variations**, and then moved into **fundamental and advanced sorting algorithms** such as Bubble Sort, Selection Sort, Insertion Sort, Merge Sort, and Quick Sort.

Later in the week, I applied these concepts to **sorting-based and mixed algorithmic problems**, using techniques like **two pointers, interval merging, and binary search optimizations**.

This week strengthened my understanding of **array manipulation, algorithm efficiency, and divide-and-conquer strategies**, which are essential for solving many coding interview problems efficiently.

---

## 📚 Topics Covered Day-Wise

### [Day 22: Linear & Binary Search](./day22/readme.md)
- **Linear Search Fundamentals:** Sequentially checking elements until target found
- **Binary Search (Iterative & Recursive):** Efficient searching using divide-and-conquer
- **Last Occurrence in Sorted Arrays:** Storing index while continuing search to locate duplicates

**Key Insight:** Binary search dramatically improves efficiency from **O(n) to O(log n)** when the array is sorted

**Problems Practiced:** Linear search, first/last occurrence (linear), binary search iterative, binary search recursive, last occurrence (binary search)

---

### [Day 23: Binary Search Variations](./day23/readme.md)
- **First Occurrence in Sorted Array:** Leftmost target using modified binary search
- **Last Occurrence in Sorted Array:** Rightmost target with boundary adjustment
- **Count Occurrences using Binary Search:** First-last occurrence difference + 1
- **Lower Bound Search:** First element ≥ target
- **Upper Bound Search:** First element > target

**Key Insight:** Binary search can be adapted to solve many problems involving **boundaries and duplicates**, not just element searching

**Problems Practiced:** First occurrence, last occurrence, count occurrences, lower bound, upper bound

---

### [Day 24: Sorting Basics](./day24/readme.md)
- **Bubble Sort:** Repeated adjacent swaps until array sorted
- **Selection Sort:** Select minimum and place in correct position
- **Insertion Sort:** Build sorted array by inserting elements into correct positions

**Key Insight:** Simple sorting algorithms are useful for **learning algorithm behavior**, though inefficient for large datasets

**Problems Practiced:** Bubble sort, selection sort, insertion sort

---

### [Day 25: Merge Sort & Quick Sort](./day25/readme.md)
- **Merge Sort:** Divide array into halves recursively, merge sorted halves
- **Quick Sort:** Select pivot, partition, recursively sort partitions

**Key Insight:** Advanced sorting algorithms improve performance from **O(n²) to O(n log n)** using divide-and-conquer

**Problems Practiced:** Merge sort implementation, quick sort implementation

---

### [Day 26: Sorting-Based Problems](./day26/readme.md)
- **Two Sum (Sorting + Two Pointers):** Sort array, use left/right pointers
- **Contains Duplicate:** Sort and check adjacent elements
- **Merge Intervals:** Sort by start time, merge overlapping intervals
- **Intersection of Two Arrays:** Sort + two pointers for common elements
- **Sort Colors (Dutch National Flag):** Three-way partitioning with three pointers

**Key Insight:** Sorting often simplifies problems by enabling **two-pointer traversal and structured comparisons**

**Problems Practiced:** Two sum, contains duplicate, merge intervals, array intersection, Dutch national flag problem

---

### [Day 27: Searching & Sorting Revision](./day27/readme.md)
- **Searching Review:** Linear search, binary search, boundary variations
- **Sorting Review:** Bubble, selection, insertion, merge, quick sort
- **Problem Strategy Review:** When to apply each searching/sorting technique

**Key Insight:** Revision helps improve **pattern recognition and implementation confidence**

**Problems Practiced:** Linear search, binary search variations, all sorting algorithms implementation review

---

### [Day 28: Mixed Practice & Mock Problems](./day28/readme.md)
- **Search Insert Position:** Binary search for insertion index
- **First and Last Position in Sorted Array:** Combined binary search boundaries
- **Find Peak Element:** Binary search on unsorted array (local comparison)
- **Move Zeroes:** Two-pointer technique for in-place array modification

**Key Insight:** Many interview problems require **combining searching logic with array manipulation patterns**

**Problems Practiced:** Search insert position, find first/last occurrence, peak element, move zeroes

---

## 🎯 Key Techniques Mastered

### Searching Techniques
- ✅ **Linear Search:** Sequential scanning for unsorted arrays
- ✅ **Binary Search:** Divide-and-conquer search for sorted arrays
- ✅ **Binary Search Variations:** Boundary search patterns (first/last, lower/upper bound)
- ✅ **Efficient Index Searching:** Handling duplicates and insertion positions

---

### Sorting Techniques
- ✅ **Basic Sorting Algorithms:** Bubble, Selection, Insertion
- ✅ **Advanced Sorting Algorithms:** Merge Sort and Quick Sort
- ✅ **Divide & Conquer Strategy:** Breaking large problems into smaller subproblems
- ✅ **Comparing Algorithm Efficiency:** O(n²) vs O(n log n)

---

### Array Manipulation Patterns
- ✅ **Two-Pointer Technique:** Efficient traversal from both directions
- ✅ **Interval Merging:** Handling overlapping ranges after sorting
- ✅ **Dutch National Flag:** Three-way partitioning for categorical sorting
- ✅ **In-place Array Modification:** Minimizing extra space usage

---

### Optimization Skills
- ✅ **Reducing Search Time:** O(n) → O(log n) with binary search
- ✅ **Efficient Sorting:** Using divide-and-conquer algorithms
- ✅ **Pointer Manipulation:** Improving array traversal efficiency
- ✅ **Handling Edge Cases:** Duplicates, boundaries, empty arrays, single elements

---

## 📊 Complexity Patterns Summary

| Technique | Time Complexity | Space Complexity | Use Case |
|-----------|-----------------|------------------|----------|
| Linear Search | O(n) | O(1) | Searching unsorted arrays |
| Binary Search | O(log n) | O(1) | Searching sorted arrays |
| Bubble / Selection Sort | O(n²) | O(1) | Basic sorting practice |
| Insertion Sort | O(n²) | O(1) | Small or nearly sorted arrays |
| Merge Sort | O(n log n) | O(n) | Stable sorting for large data |
| Quick Sort | O(n log n) avg | O(log n) | Fast practical sorting |
| Two Pointer Technique | O(n) | O(1) | Array manipulation on sorted arrays |
| Interval Merging | O(n log n) | O(n) | Overlapping range problems |
| Dutch National Flag | O(n) | O(1) | Three-way categorical sorting |

---

## 💡 Key Takeaways

1. **Binary search reduces search time dramatically** when arrays are sorted
2. **Sorting algorithms differ significantly in efficiency** — advanced algorithms reach O(n log n)
3. **Divide-and-conquer strategies** power efficient algorithms like merge sort and quick sort
4. **Two-pointer techniques simplify many array problems** by reducing nested loops to O(n)
5. **Sorting often transforms complex problems** into simpler linear comparisons
6. **Handling boundaries and edge cases is critical** when implementing binary search variations
7. **Algorithm choice matters** — selecting the right technique significantly improves performance
8. **Mixed practice improves pattern recognition** for identifying the best approach
9. **Dutch National Flag pattern** solves categorical sorting in single pass
10. **Search + sort combinations** appear frequently in interview problems

---

## 🔗 Connections Between Topics

| Topic Connection | Why It Matters |
|------------------|----------------|
| Linear Search → Binary Search | Shows how sorted data enables faster searching |
| Binary Search → Boundary Problems | Enables finding first/last positions and insertion points |
| Sorting → Two Pointers | Sorted arrays enable efficient pointer traversal |
| Merge Sort → Divide & Conquer | Demonstrates recursive problem decomposition |
| Quick Sort → Partitioning | Shows how pivot-based logic organizes arrays |
| Sorting → Interval Problems | Sorted intervals simplify overlap detection |
| Two Pointers → Dutch National Flag | Both use multiple pointers for efficient traversal |
| Binary Search → Search Insert Position | Binary search adapts to find insertion indices |

---

## ✅ Week 4 Progress Checklist

- [x] Day 22: Linear and binary search fundamentals
- [x] Day 23: Binary search variations and boundary searches
- [x] Day 24: Basic sorting algorithms (bubble, selection, insertion)
- [x] Day 25: Advanced sorting (merge sort, quick sort)
- [x] Day 26: Sorting-based problem solving
- [x] Day 27: Comprehensive revision of searching and sorting
- [x] Day 28: Mixed practice and mock interview problems

---

*This week strengthened my foundation in **searching and sorting algorithms**, improving my ability to choose the right algorithm based on input constraints and problem requirements. Binary search taught me to leverage sorted data for logarithmic time, while sorting algorithms revealed how divide-and-conquer transforms O(n²) into O(n log n). These techniques are fundamental for solving many array-based coding interview questions efficiently.*