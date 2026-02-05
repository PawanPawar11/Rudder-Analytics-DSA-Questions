## 📘 Problem: Custom String Compression & Expansion

You are given a **compressed string** that represents repeated characters or nested patterns. Your task is to **decode** the string and return its expanded form.

The compression rules are:

1. A character followed by a number means the character repeats that many times.

   * Example: `a3b2c1` → `"aaabbc"`

2. Brackets `[]` indicate nested patterns where the number before `[` repeats the entire substring inside.

   * Example: `a2[b3[c]]` → `"abcccbccc"`

---

### 🧩 Your Task

Given a string `s`, return the fully expanded string after applying all repetition rules.

---

### 📥 Input

* A string `s` containing:

  * lowercase letters `a–z`
  * digits `0–9`
  * square brackets `[` and `]`

---

### 📤 Output

* Return the decoded (expanded) string.

---

### 🔒 Constraints

* `0 ≤ length of s ≤ 10^5`
* Numbers may contain multiple digits (e.g., `a10`)
* The output size will not exceed reasonable memory limits.

---

### ✅ Examples

**Example 1**

```
Input: s = "a3b2c1"
Output: "aaabbc"
```

**Example 2**

```
Input: s = "a10"
Output: "aaaaaaaaaa"
```

**Example 3**

```
Input: s = "a2[b3[c]]"
Output: "abcccbccc"
```

**Example 4**

```
Input: s = ""
Output: ""
```

---

### ⚠️ Edge Cases to Consider

* Empty string input.
* Single characters without numbers.
* Numbers with more than one digit (`a12`).
* Deeply nested bracket expressions.
* Mixed plain characters and nested patterns.

---

### 💡 Hints (Interview Style)

* Use a **stack** to manage nested decoding.
* Track current string and current number separately.
* Convert digit characters into integers carefully.