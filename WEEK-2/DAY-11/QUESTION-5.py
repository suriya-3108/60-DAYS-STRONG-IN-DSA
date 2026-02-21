"""## Question: Prefix Sum Concept

Consider the following Python code that uses the **Prefix Sum** technique to answer range sum queries efficiently.

### Code

```python
arr = [2, 4, 6, 8, 10]

# Step 1: Build prefix sum array
prefix = [0] * len(arr)
prefix[0] = arr[0]

for i in range(1, len(arr)):
    prefix[i] = prefix[i - 1] + arr[i]

# Step 2: Find sum of subarray from index l to r
l = 1
r = 3

if l == 0:
    answer = prefix[r]
else:
    answer = prefix[r] - prefix[l - 1]

print(answer)
```

---

## Theory Questions & Answers

### 1)Why is `prefix[0]` initialized with `arr[0]`?**

**Answer:**
`prefix[0]` represents the sum of elements from index `0` to `0`.
So it must be equal to the first element of the array.
This initialization allows the loop to correctly build cumulative sums.

---

### 2)What does `prefix[i - 1]` represent in the loop?**

**Answer:**
`prefix[i - 1]` stores the **sum of all elements before index `i`**.
By adding `arr[i]` to it, we get the total sum from index `0` to `i`.

---

### 3)Why do we check `if l == 0` before calculating the subarray sum?**

**Answer:**
When `l == 0`, the required sum is already stored in `prefix[r]`.
Accessing `prefix[l - 1]` would cause an **index error**, so this condition avoids it.

---

### 4)Why is the formula `prefix[r] - prefix[l - 1]` used?**

**Answer:**

* `prefix[r]` → sum from index `0` to `r`
* `prefix[l - 1]` → sum from index `0` to `l-1`

Subtracting removes unwanted elements and gives the sum from `l` to `r`.

---

### 5)What is the time complexity of this approach?**

**Answer:**

* Building prefix array: **O(n)**
* Each range sum query: **O(1)**

So overall, it is **much faster than O(n²)** for multiple queries.

"""