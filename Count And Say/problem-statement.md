## 📘 Problem: Generate the Look-and-Say Sequence

The **Look-and-Say Sequence** is a series of numbers where each term is created by describing the digits of the previous term.

The sequence starts with:

```
1
11
21
1211
111221
312211
...
```

Each term is formed by reading the previous term from left to right and counting consecutive digits.

👉 Example:

* `"21"` is read as **“one 2, one 1”** → `"1211"`
* `"111221"` is read as **“three 1s, two 2s, one 1”** → `"312211"`

---

### 🧩 Your Task

Given an integer **n**, return the **n-th term** of the Look-and-Say sequence as a string.

---

### 📥 Input

* A single integer `n`.

### 📤 Output

* A string representing the `n`-th term of the sequence.

---

### 🔒 Constraints

* `1 ≤ n ≤ 30`
* The result may be large, so return it as a **string**, not an integer.

---

### ✅ Examples

**Example 1**

```
Input: n = 1
Output: "1"
```

**Example 2**

```
Input: n = 4
Output: "1211"
```

**Example 3**

```
Input: n = 5
Output: "111221"
```

---

### 💡 Notes

* Start from `"1"` as the first term.
* Read digits in groups of consecutive identical numbers.
* Append `count + digit` while building the next term.