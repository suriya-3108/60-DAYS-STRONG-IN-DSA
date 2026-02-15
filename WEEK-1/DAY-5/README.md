# Day 5: Time & Space Complexity – Big O Analysis

## Overview
Today I learned about **algorithm efficiency** through Big O notation - a mathematical way to describe how the runtime and memory requirements of an algorithm grow as the input size increases. Understanding complexity analysis is crucial for writing scalable and optimized code.

---

## Table of Contents
1. [What is Big O Notation?](#what-is-big-o-notation)
2. [Why Complexity Analysis Matters](#why-complexity-analysis-matters)
3. [Common Time Complexities](#common-time-complexities)
4. [Space Complexity](#space-complexity)
5. [Rules of Big O](#rules-of-big-o)
6. [Examples with Code](#examples-with-code)
7. [Visual Comparison](#visual-comparison)
8. [Key Takeaways](#key-takeaways)

---

## What is Big O Notation?

**Big O notation** describes the upper bound of an algorithm's growth rate. It answers the question: *"How does the algorithm's performance scale as the input gets arbitrarily large?"*

- **O** stands for "Order of"
- Focuses on the **worst-case scenario**
- Ignores constants and lower-order terms
- Measures **time complexity** (runtime) or **space complexity** (memory)

---

## Why Complexity Analysis Matters

| Scenario | Without Optimization | With Optimization |
|----------|---------------------|-------------------|
| Search in 1 million items | Linear: ~1M steps | Binary: ~20 steps |
| Sort 1 million records | Bubble: ~1 trillion ops | Quick: ~20M ops |
| Handle 10k concurrent users | May crash | Smooth operation |

**Bottom line:** The difference between O(n²) and O(n log n) can mean seconds vs. hours!

---

## Common Time Complexities

| Notation | Name | Description | Example |
|----------|------|-------------|---------|
| **O(1)** | Constant | Always takes the same time | Array access by index |
| **O(log n)** | Logarithmic | Cuts problem in half each time | Binary search |
| **O(n)** | Linear | Scales linearly with input | Simple loop |
| **O(n log n)** | Linearithmic | Divide and conquer | Merge sort, Quick sort |
| **O(n²)** | Quadratic | Nested loops | Bubble sort, nested iterations |
| **O(2ⁿ)** | Exponential | Recursive doubling | Fibonacci (naive) |
| **O(n!)** | Factorial | Extremely slow | Permutations |

**Growth Rate Visual:**
```
O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ) < O(n!)
```

---

## Space Complexity

Measures **additional memory** an algorithm needs relative to input size.

### Examples:
- **O(1)**: Using a few variables regardless of input
- **O(n)**: Creating an array of size n
- **O(n²)**: Creating a 2D matrix n×n

### Trade-off:
Sometimes we can trade space for time (caching/memoization) or time for space (in-place algorithms).

---

## Rules of Big O

### 1. **Drop Constants**
```
O(2n) → O(n)
O(100) → O(1)
O(n²/2) → O(n²)
```

### 2. **Drop Non-Dominant Terms**
```
O(n² + n) → O(n²)
O(n + log n) → O(n)
O(n! + n²) → O(n!)
```

### 3. **Different Inputs → Different Variables**
```python
# O(a + b) - not O(n)!
for item in listA:    # O(a)
    print(item)
for item in listB:    # O(b)
    print(item)
```

### 4. **Loops**
- Single loop: O(n)
- Nested loops: O(n × m)
- Consecutive loops: O(n + m) → O(n) if same input

---

## Examples with Code

### O(1) - Constant Time
```python
def get_first_element(arr):
    return arr[0] if arr else None

def is_even(num):
    return num % 2 == 0
```

### O(n) - Linear Time
```python
def find_max(arr):
    max_val = arr[0]
    for num in arr:        # n iterations
        if num > max_val:
            max_val = num
    return max_val

def sum_array(arr):
    total = 0
    for num in arr:        # n iterations
        total += num
    return total
```

### O(n²) - Quadratic Time
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):          # n times
        for j in range(0, n-i-1): # n times
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def print_pairs(arr):
    for i in range(len(arr)):    # n times
        for j in range(len(arr)): # n times
            print(arr[i], arr[j])
```

### O(log n) - Logarithmic Time
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:          # log n iterations
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

### O(n log n) - Linearithmic Time
```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])   # recursively divide
    right = merge_sort(arr[mid:])  # O(log n) levels
    
    return merge(left, right)      # merging takes O(n)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

### Space Complexity Examples
```python
# O(1) space - only uses a few variables
def sum_array(arr):
    total = 0
    for num in arr:
        total += num
    return total

# O(n) space - creates new array of size n
def double_array(arr):
    result = []
    for num in arr:
        result.append(num * 2)
    return result

# O(n²) space - creates 2D matrix
def create_matrix(n):
    matrix = [[0] * n for _ in range(n)]
    return matrix
```

---

## Visual Comparison

```
Input Size (n) | O(1) | O(log n) | O(n) | O(n log n) | O(n²) | O(2ⁿ)
---------------|------|----------|------|------------|-------|-------
10             | 1    | 3        | 10   | 33         | 100   | 1024
100            | 1    | 7        | 100  | 664        | 10K   | 1.27e30
1,000          | 1    | 10       | 1K   | 9,966      | 1M    | insane
1,000,000      | 1    | 20       | 1M   | 19.9M      | 1T    | impossible
```

**Graphical Representation (conceptual):**
```
Time
  ↑
  |                          ↗ O(n!)
  |                       ↗
  |                    ↗    O(2ⁿ)
  |                 ↗
  |              ↗        O(n²)
  |           ↗
  |        ↗            O(n log n)
  |     ↗
  |  ↗                 O(n)
  |↗
  |_____________________________→ Input Size
  0(1)  O(log n)
```

---

## Key Takeaways

1. **Big O describes growth rate**, not actual speed
2. **Always consider worst-case** unless specified otherwise
3. **Space-time tradeoff** is real - sometimes using more memory makes things faster
4. **Different inputs need different variables** (O(a + b) not always O(n))
5. **Constants don't matter** for large inputs
6. **Practice identifying patterns**:
   - Single loop → O(n)
   - Nested loops → O(n²)
   - Halving the input → O(log n)
   - Divide and conquer → O(n log n)
   - Recursion with multiple calls → often exponential

---

## Practice Problems to Try

1. Find the complexity of summing all elements in a 2D array
2. Compare linear search vs binary search on sorted data
3. Analyze a recursive Fibonacci implementation
4. Determine space complexity of reversing an array in-place vs. creating a new array
5. Calculate complexity of finding duplicates in an array (naive vs. hash set approach)

---

## Resources for Further Learning

- [Big-O Cheat Sheet](https://www.bigocheatsheet.com/)
- [Khan Academy - Algorithms](https://www.khanacademy.org/computing/computer-science/algorithms)
- [MIT OpenCourseWare - Introduction to Algorithms](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/)

---

**"Premature optimization is the root of all evil" - but knowing complexity helps you optimize when it matters!**