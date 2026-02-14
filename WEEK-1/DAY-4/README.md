# Day 4 DSA Practice — Advanced Python: List/Dict Comprehensions & Collections Module

Today I focused on strengthening my **Python DSA fundamentals** by practicing **advanced Python concepts**, including **list and dictionary comprehensions** and the **collections module**. This helped improve my **problem-solving skills, code efficiency, and logic building**.

---

## 1️⃣ List Comprehensions

* **Basic List Comprehension** — Create a new list from an existing iterable  
  *Example:* `[x**2 for x in range(6)]` → `[0, 1, 4, 9, 16, 25]`

* **Conditional List Comprehension** — Filter elements with `if`  
  *Example:* `[x**2 for x in range(6) if x % 2 == 0]` → `[0, 4, 16]`

* **Conditional List Comprehension with if-else** — Apply different operations based on a condition  
  *Example:* `[x**2 if x % 2 == 0 else x**3 for x in range(1, 6)]` → `[1, 4, 27, 16, 125]`

* **Nested List Comprehension** — Generate a 2D list  
  *Example:* `[[x*2 for x in row] for row in [[1,2],[3,4]]]` → `[[2,4],[6,8]]`

* **Flattening 2D Lists** — Convert a 2D list into a 1D list  
  *Example:* `[num for row in [[1,2],[3,4]] for num in row]` → `[1,2,3,4]`

---

## 2️⃣ Dictionary Comprehensions

* **Basic Dictionary Comprehension** — Map keys to values  
  *Example:* `{x: x**2 for x in range(1, 6)}` → `{1:1, 2:4, 3:9, 4:16, 5:25}`

* **Conditional Dictionary Comprehension** — Include only key-value pairs that meet a condition  
  *Example:* `{x: x**2 for x in range(1, 6) if x % 2 == 0}` → `{2:4, 4:16}`

* **Swapping Keys & Values** — Reverse keys and values  
  *Example:* `{v: k for k, v in {'a':1, 'b':2}.items()}` → `{1:'a', 2:'b'}`

* **Filtering Dictionaries** — Keep only entries that meet a condition  
  *Example:* `{k: v for k, v in {'a':10, 'b':5}.items() if v > 5}` → `{'a':10}`

* **Creating Dictionary from Lists** — Combine two lists into a dictionary  
  *Example:* `{k: v for k, v in zip(['a','b'], [1,2])}` → `{'a':1, 'b':2}`

---

## 3️⃣ Collections Module

### **3.1 Counter**

* Count frequency of elements in an iterable  
  *Example:* `Counter('banana')` → `{'a':3, 'n':2, 'b':1}`

* Find most common elements and perform **anagram checks**  
  *Example:* `Counter('listen') == Counter('silent')` → `True`

---

### **3.2 defaultdict**

* Dictionary with default values; avoids `KeyError`  
* Useful for **grouping items** or **counting frequencies**  
  *Example:*
  ```python
  from collections import defaultdict

  words = ["apple", "banana", "avocado"]
  grouped = defaultdict(list)

  for w in words:
      grouped[w[0]].append(w)
  # Output: {'a': ['apple', 'avocado'], 'b': ['banana']}
  ```

---

### **3.3 deque**

* Double-ended queue, fast add/remove from both ends  
* Methods: `append`, `appendleft`, `pop`, `popleft`  
* Useful for queue implementation or sliding window problems  
  *Example:*
  ```python
  from collections import deque
  dq = deque()
  dq.append(1)
  dq.appendleft(2)
  dq.pop()      # removes 1
  dq.popleft()  # removes 2
  ```

---

### **3.4 OrderedDict**

* Dictionary that preserves insertion order  
* Useful when order matters (e.g., logs, reports)  
  *Example:*
  ```python
  from collections import OrderedDict
  data = {'apple': 3, 'banana': 2, 'cherry': 5}
  ordered_data = OrderedDict(data)
  ordered_data['date'] = 4
  print(ordered_data)
  # Output: OrderedDict([('apple',3),('banana',2),('cherry',5),('date',4)])
  ```

---

## ✅ Key Skills Practiced

* **List Comprehensions** — Basic, conditional, nested, flattening  
* **Dictionary Comprehensions** — Conditional, swapping keys & values, filtering, creating from lists  
* **Collections Module** — Counter, defaultdict, deque, OrderedDict  
* **Problem-Solving Patterns** — Frequency counting, grouping, queue operations, preserving order  
* **Python Efficiency** — Reduce loops, avoid KeyErrors, maintain insertion order

---

This practice covers all advanced Python operations useful for DSA, forming a strong foundation for efficient coding, frequency-based problems, and queue/stack-based algorithms.