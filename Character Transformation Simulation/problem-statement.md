## 📘 Problem: Character Transformation Simulation

You are given a lowercase alphabetic string `s` and an integer `k`.
Your task is to transform each character based on the following rules:

### 🔄 Transformation Rules

1. **If the character is a consonant**
   → Replace it with the character that is `k` positions **forward** in the alphabet.

2. **If the character is a vowel** (`a, e, i, o, u`)
   → Replace it with the character that is `k` positions **backward** in the alphabet.

3. The alphabet is **circular**:

   * Moving forward from `z` wraps to `a`.
   * Moving backward from `a` wraps to `z`.

---

### 🧩 Your Task

Given a string `s` and an integer `k`, return the transformed string after applying the rules to every character.

---

### 📥 Input

* A string `s` consisting only of lowercase English letters.
* An integer `k`.

---

### 📤 Output

* Return the transformed string.

---

### 🔒 Constraints

* `1 ≤ length of s ≤ 10^5`
* `0 ≤ k ≤ 10^9`
* Use efficient modular arithmetic to avoid unnecessary loops.

---

### ✅ Examples

**Example 1**

```
Input: s = "abc", k = 2
Output: "yac"

Explanation:
a → vowel → move back 2 → y
b → consonant → move forward 2 → d
c → consonant → move forward 2 → e
Result: "yde"
```

**Example 2**

```
Input: s = "zoo", k = 1
Output: "ann"
```

**Example 3**

```
Input: s = "aei", k = 3
Output: "xbf"
```

---

### ⚠️ Edge Cases

* Very large values of `k` (use `k % 26`).
* All vowels or all consonants.
* Wrap-around cases like `'a'` moving backward or `'z'` moving forward.
* Single character strings.