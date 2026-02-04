## 🔎 What is “Look-and-Say” actually?

It’s just a **number pattern** where you:

👉 **Look** at the previous number
👉 **Say** what you see (count + digit)
👉 That spoken result becomes the next number.

So you are not doing math — you are just **describing digits**.

---

## 🧱 Step-by-step idea

Start with:

```
1
```

Now keep describing it.

---

### ✅ Step 1 → `"1"`

What do you see?

* one **1**

So you say:

```
11
```

👉 “one 1” → `11`

---

### ✅ Step 2 → `"11"`

What do you see?

* two **1s**

So you say:

```
21
```

👉 “two 1s” → `21`

---

### ✅ Step 3 → `"21"`

Break into groups:

* one **2**
* one **1**

So you say:

```
1211
```

👉 “one 2, one 1” → `1211`

---

### ✅ Step 4 → `"1211"`

Group same digits:

* one **1**
* one **2**
* two **1s**

So:

```
111221
```

---

## 📌 Main rule (very important)

When building the next term:

```
[count of same digits] + [digit itself]
```

Example:

```
111221
```

Groups:

```
111   → three 1s   → 31
22    → two 2s     → 22
1     → one 1      → 11
```

Join them:

```
312211
```

---

## 🎯 What the question is asking

You will get a number `n`.

You must:

1. Start from `"1"`
2. Generate next term again and again
3. Stop when you reach the **n-th term**
4. Return it as a **string**

---

## ❓ Why string and not number?

Because terms become very long like:

```
111221312211...
```

These are **digit patterns**, not actual numbers for calculation.

---

## 🧠 Super short summary

👉 Start with `"1"`
👉 Repeat n-1 times:

* Read previous term
* Count same digits
* Build new string using `count + digit`