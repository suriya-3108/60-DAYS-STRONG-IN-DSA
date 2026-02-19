# Day 9 DSA Practice — Two-Pointer Technique

Today I focused on **two-pointer problems on arrays and strings**, including **finding pairs in sorted and unsorted arrays, removing duplicates, moving zeros, and squared sorted arrays**. This helped improve my **problem-solving skills, logic building, edge case handling, and preparation for coding interviews**.

---

## 1️⃣ Two Sum (Sorted Array)

- **Problem:** Given a sorted array and a target, find the indices of two numbers that sum to the target.
- **Logic:** Use **two pointers** (`left` and `right`) starting at the ends, move the pointer pointing to the smaller number if sum < target, larger number if sum > target.
- **Example:** `[1, 2, 3, 4, 6]`, target=6 → indices `[1, 3]` (2+4=6)

---

## 2️⃣ Pair with Given Sum (Unsorted Array)

- **Problem:** Given an unsorted array and a target sum, check if any pair exists whose sum equals the target.
- **Logic:** First sort the array → then use **two-pointer approach** to find pair summing to target.
- **Example:** `[8, 7, 2, 5, 3, 1]`, target=10 → `True` (pairs: 8+2 or 7+3)

---

## 3️⃣ Remove Duplicates from Sorted Array

- **Problem:** Given a sorted array, remove duplicates in-place and return the new length.
- **Logic:** Use two pointers (`slow` and `fast`) to overwrite duplicates.
- **Example:** `[1, 1, 2, 2, 3, 4, 4]` → `[1, 2, 3, 4]` (length=4)

---

## 4️⃣ Move Zeros to End

- **Problem:** Move all zeros in an array to the end while keeping the order of non-zero elements.
- **Logic:** Two-pointer swap; push non-zero elements forward.
- **Example:** `[0, 1, 0, 3, 12]` → `[1, 3, 12, 0, 0]`

---

## 5️⃣ Squared Sorted Array

- **Problem:** Given a sorted array (may have negative numbers), return a new array of squares sorted in non-decreasing order.
- **Logic:** Compare absolute values from both ends, fill a result array from back using two pointers.
- **Example:** `[-4, -1, 0, 3, 10]` → `[0, 1, 9, 16, 100]`

---

## 6️⃣ Remove Specific Element In-Place

- **Problem:** Remove all occurrences of a specific value in an array in-place and return the new length.
- **Logic:** Use a slow pointer to overwrite target values while scanning array with fast pointer.
- **Example:** `[0, 1, 2, 2, 3, 0, 4, 2]`, val=2 → `[0, 1, 3, 0, 4]` (length=5)

---

## 7️⃣ Reverse Words in a String

- **Problem:** Given a string with words separated by spaces, reverse the order of words.
- **Logic:** Split the string into words, use two pointers to reverse the order, and join back into a string.
- **Example:** `"  hello   world  "` → `"world hello"`

---

## 8️⃣ Palindrome Check

- **Problem:** Given a string, check if it reads the same forwards and backwards (ignoring spaces and punctuation).
- **Logic:** Use two pointers (`left` and `right`) starting at both ends, compare characters and move inward until pointers meet.
- **Example:** `"racecar"` → `True`, `"A man a plan a canal Panama"` → `True`, `"hello"` → `False`

---

## ✅ Key Skills Practiced

- **Two-Pointer Technique** — left/right scanning, slow/fast pointer usage
- **In-Place Array Modification** — removing duplicates, removing elements, moving zeros
- **Array Traversal & Logic** — pair sum, squared array, index tracking
- **String Manipulation** — reversing words, palindrome checking, handling spaces and punctuation
- **Edge Case Handling** — empty arrays, multiple duplicates, multiple spaces, mixed case strings
- **Optimization Awareness** — O(n) scanning, O(1) extra space where possible

---

This practice consolidated **Day 9 concepts** and strengthened **two-pointer logic, in-place array/string manipulations, pair finding, palindrome checking, and edge case handling**, preparing me for **more advanced array/string problems** in upcoming DSA practice.