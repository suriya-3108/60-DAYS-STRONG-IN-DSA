# Day 8 DSA Practice — Arrays & Strings

Today I focused on **array traversal, insertion/deletion, rotations, and combined logic problems**, including **in-place manipulations, moving zeros, even/odd partitioning, maximum/minimum calculations, and frequency counting**. This helped improve my **problem-solving skills, logic building, edge case handling, and preparation for coding interviews**.

---

## 1️⃣ Array Traversal & Basic Operations

- **Reverse an Array** — Traverse from end to start to reverse elements  
  *Example:* `[1, 2, 3, 4, 5]` → `[5, 4, 3, 2, 1]`

- **Left Rotate by k (Shift Method)** — Move first element to end repeatedly  
  *Example:* `[1, 2, 3, 4, 5]`, k=2 → `[3, 4, 5, 1, 2]`

- **Move Zeros to End** — Two-pointer / swap method to push zeros while preserving order  
  *Example:* `[0, 1, 0, 3, 12]` → `[1, 3, 12, 0, 0]`

---

## 2️⃣ Array Manipulation & Two-Pointer Thinking

- **Stable Even-Odd Partition** — Move even numbers to front, odd numbers after, preserving order  
  *Example:* `[1, 2, 3, 4, 5, 6]` → `[2, 4, 6, 1, 3, 5]`

- **Maximum Product of Two Elements** — Track largest and second largest in single pass  
  *Example:* `[3, 4, 5, 2]` → `20`

- **Find Minimum and Maximum in Single Pass** — Track min and max independently while traversing  
  *Example:* `[3, 1, 5, 2, 4]` → `Min=1, Max=5`

- **Remove All Occurrences of a Value (In-place)** — Shift non-target elements forward  
  *Example:* `[3, 2, 2, 3, 4]`, val=2 → `[3, 3, 4]`

---

## 3️⃣ Combined / Logic Skills

- **In-Place Array Manipulation** — Practiced shifting, rotation, and removal without extra array
- **Frequency Counting** — Applied array or dictionary for counting numbers efficiently
- **Edge Case Thinking** — Considered empty arrays, all zeros, duplicates, single-element arrays
- **Order Preservation** — Ensured original sequence when needed (stable even-odd, remove element)
- **Optimal vs Brute Force** — Learned O(n) solutions for rotations, max product, and min/max problems

---

## ✅ Key Skills Practiced

- **Array Basics** — Traversal, indexing, insertion, deletion
- **Two-Pointer / Partitioning Patterns** — Moving zeros, even/odd, stable reordering
- **Extreme Values** — Maximum, second maximum, minimum, maximum in one pass
- **Rotations** — Left/right shift, reversal algorithm for O(n) rotations
- **Frequency Counting** — Using dictionaries or in-place array modification
- **Problem-Solving Patterns** — Nested loops, conditional logic, pointer tracking, order maintenance
- **Optimization Awareness** — Time complexity O(n), space efficiency O(1)–O(n)

---

This practice consolidated **Day 8 concepts** and strengthened **array traversal, insertion/deletion, rotations, extreme value tracking, in-place manipulations, and frequency counting**, building a solid foundation for **more advanced array/string problems and two-pointer techniques** in the coming days.