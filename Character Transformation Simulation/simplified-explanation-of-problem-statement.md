This problem is just about **shifting letters** in the alphabet.

---

# 🔎 What you need to do

You are given:

```
a string s
a number k
```

For **every character** in the string:

* check if it is a **vowel**
* or a **consonant**
* then move it in the alphabet.

---

# 🧱 Rule 1 — Consonants

If the letter is a consonant:

```
move forward by k positions
```

Example:

```
b + 2 → d
c + 2 → e
```

Alphabet goes like:

```
a b c d e f g ... z
```

So moving forward means going right.

---

# 🧱 Rule 2 — Vowels

Vowels are:

```
a e i o u
```

If letter is a vowel:

```
move backward by k positions
```

Example:

```
a - 2 → y
e - 2 → c
```

Moving backward means going left.

---

# 🔁 Rule 3 — Circular Alphabet

Alphabet is like a circle.

So:

```
z + 1 → a
a - 1 → z
```

You never go outside a–z.

---

# 🎯 Example (super simple)

## Input

```
s = "abc"
k = 2
```

Check each letter:

### 1️⃣ a

* vowel
* move back 2

```
a → y
```

---

### 2️⃣ b

* consonant
* move forward 2

```
b → d
```

---

### 3️⃣ c

* consonant
* move forward 2

```
c → e
```

Final:

```
yde
```

---

# ⚠️ Why they say use `k % 26`

Alphabet has only **26 letters**.

So moving 28 steps is same as:

```
28 % 26 = 2
```

This avoids huge loops when k is very big like `10^9`.

---

# 🧠 Simple Formula Meaning

They gave this hint:

```
newChar = 'a' + ((char - 'a' ± k) mod 26)
```

What it means in easy words:

1. Convert letter to number:

```
'a' → 0
'b' → 1
'c' → 2
...
```

2. Add or subtract `k`

3. Keep it inside 0–25 using `% 26`

4. Convert back to letter.

---

# ✅ Super Short Summary

For each letter:

```
if vowel      → shift backward
if consonant  → shift forward
```

Always:

```
use circular alphabet
use k % 26
```