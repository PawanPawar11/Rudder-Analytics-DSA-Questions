This problem is just about **expanding a coded string**.

You read the string and **repeat characters or groups** based on numbers.

---

# 🔎 Rule 1 — Character + Number

If a letter has a number after it:

```
letter + number  → repeat the letter
```

### Example

```
a3b2c1
```

Break it:

* a3 → aaa
* b2 → bb
* c1 → c

Final result:

```
aaabbc
```

👉 So numbers tell **how many times** to repeat the previous letter.

---

# 🔎 Rule 2 — Number + [ ... ] (Groups)

If you see:

```
number[ something ]
```

It means:

👉 Repeat **everything inside brackets** that many times.

---

### Example

```
a2[b3[c]]
```

Let’s go step by step.

---

### Step 1 — Solve the inner part first

```
b3[c]
```

Inside:

```
c → repeated 3 times → ccc
```

So it becomes:

```
bccc
```

---

### Step 2 — Apply outer number

```
2[bccc]
```

Repeat whole thing twice:

```
bcccbccc
```

---

### Step 3 — Add starting letter

Original string started with `a`:

```
a + bcccbccc
```

Final answer:

```
abcccbccc
```

---

# 🧱 What you basically need to do

While reading the string:

### 1️⃣ If you see a letter

Just add it to result.

---

### 2️⃣ If you see a number after a letter

Repeat that letter.

Example:

```
a10 → aaaaaaaaaa
```

(Number can have many digits.)

---

### 3️⃣ If you see brackets `[ ]`

It means:

* Save current progress
* Decode inside first
* Repeat that whole part

👉 Nested brackets mean **decode from inside out**.


