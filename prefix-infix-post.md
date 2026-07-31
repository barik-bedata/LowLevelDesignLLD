# Expression Conversion Guide: Infix, Prefix & Postfix
*(ইনফিক্স, প্রিফিক্স ও পোস্টফিক্স রূপান্তরের সম্পূর্ণ বাংলায় গাইড ও চিট শিট)*

---

## 📌 সূচিপত্র (Table of Contents)
1. [মূল পরিচিতি ও অপারেটরের ক্ষমতা (Precedence Rules)](#১-মূল-পরিচিতি-ও-অপারেটরের-ক্ষমতা)
2. [Infix to Postfix Conversion](#২-infix-to-postfix-conversion)
3. [Infix to Prefix Conversion](#৩-infix-to-prefix-conversion)
4. [Postfix to Infix Conversion](#৪-postfix-to-infix-conversion)
5. [Postfix to Prefix Conversion](#৫-postfix-to-prefix-conversion)
6. [Prefix to Infix Conversion](#৬-prefix-to-infix-conversion)
7. [Prefix to Postfix Conversion](#৭-prefix-to-postfix-conversion)
8. [গাণিতিক প্রমাণ ও ভ্যালিডেশন (Verification Test)](#৮-গাণিতিক-প্রমাণ-ও-ভ্যালিডেশন)
9. [ফাইনাল চিট শিট (Ultimate Cheat Sheet)](#৯-ফাইনাল-চিট-শিট)

---

## ১. মূল পরিচিতি ও অপারেটরের ক্ষমতা

### ৩টি ফরমেটের সংজ্ঞাগত পার্থক্য:
* **Infix (ইনফিক্স):** অপারেটরটি অপের্যান্ডগুলোর **মাঝে** থাকে। উদাহরণ: `A + B`
* **Prefix (প্রিফিক্স / Polish Notation):** অপারেটরটি অপের্যান্ডগুলোর **সামনে** থাকে। উদাহরণ: `+ A B`
* **Postfix (পোস্টফিক্স / Reverse Polish Notation):** অপারেটরটি অপের্যান্ডগুলোর **শেষে** থাকে। উদাহরণ: `A B +`

### 🔑 Operator Precedence & Associativity Table:

| Operator | নাম / কাজ | Precedence (ক্ষমতা) | Associativity (দিক) |
| :---: | :---: | :---: | :---: |
| **`^`** বা **`$`** | Power / Exponentiation | ১ম (সবচেয়ে বেশি) | Right to Left |
| **`*`** , **`/`** | গুণ, ভাগ | ২য় | Left to Right |
| **`+`** , **`-`** | যোগ, বিয়োগ | ৩য় (সবচেয়ে কম) | Left to Right |

---

## ২. Infix to Postfix Conversion

### 📜 কাজের নিয়ম (Left to Right Scan):
1. **Operand (A, B, C...) পেলে:** সরাসরি **Output**-এ যাবে।
2. **ফার্স্ট ব্র্যাকেট `(` পেলে:** সরাসরি **Stack**-এ Push করো।
3. **ক্লোজিং ব্র্যাকেট `)` পেলে:** Stack থেকে একের পর এক Pop করে Output-এ পাঠাও যতক্ষণ না `(` পাওয়া যায়। `(` টাকে বাদ দিয়ে দাও।
4. **Operator পেলে:** 
   - স্ট্যাকে বসে থাকা অপারেটরের ক্ষমতা যদি চলতি অপারেটরের **সমান বা বেশি** হয় ➔ স্ট্যাকের টপকে Pop করে Output-এ পাঠাও। 
   - তারপর চলতি অপারেটরটিকে Stack-এ Push করো।
5. **Expression শেষ হলে:** Stack এর সব অপারেটর Pop করে Output-এ পাঠাও।

---

### 📝 উদাহরণ (Infix ➔ Postfix):
**Expression:** `A + B * (C - D) / E`

#### ধাপে ধাপে টেবিল ট্রেসিং:

| Symbol / Token | Stack State | Output (Postfix) | ব্যাখ্যা / বিবরণ |
| :---: | :--- | :--- | :--- |
| **`A`** | `খালি` | `A` | Operand ➔ Output |
| **`+`** | `+` | `A` | Operator ➔ Stack |
| **`B`** | `+` | `A B` | Operand ➔ Output |
| **`*`** | `+ *` | `A B` | `*` > `+` ➔ Push |
| **`(`** | `+ * (` | `A B` | ব্র্যাকেট ➔ Push |
| **`C`** | `+ * (` | `A B C` | Operand ➔ Output |
| **`-`** | `+ * ( -` | `A B C` | Operator ➔ Push |
| **`D`** | `+ * ( -` | `A B C D` | Operand ➔ Output |
| **`)`** | `+ *` | `A B C D -` | `(` পর্যন্ত Pop হয়ে `-` Output-এ গেল |
| **`/`** | `+ /` | `A B C D - *` | `/` এবং `*` সমান ক্ষমতার। তাই `*` Pop হলো, `/` Push হলো |
| **`E`** | `+ /` | `A B C D - * E` | Operand ➔ Output |
| **End** | `খালি` | **`A B C D - * E / +`** | ইনপুট শেষ ➔ Stack-এর বাকি সব Pop হলো |

✅ **চূড়ান্ত Postfix উত্তর:** `A B C D - * E / +`

---

## ৩. Infix to Prefix Conversion

Infix থেকে Prefix করার সবচেয়ে সহজ ও নির্ভরযোগ্য নিয়ম হলো **Reverse Method (৩ ধাপের পদ্ধতি)**।

### 📜 ৩টি সহজ ধাপ:
1. **ধাপ ১:** মূল Expression-টিকে উল্টে (Reverse) নাও। *(Note: `(` হয়ে যাবে `)` এবং `)` হয়ে যাবে `(`)।*
2. **ধাপ ২:** উল্টানো Expression-টির ওপর **Postfix নিয়ম** প্রয়োগ করো।
   - **বিশেষ নিয়ম:** সমান ক্ষমতার অপারেটর স্ট্যাকে আসলে **Pop হবে না, Push হবে**। অর্থাৎ শুধুমাত্র স্ট্যাকে কঠোরভাবে বেশি (Strictly Greater) ক্ষমতার অপারেটর থাকলেই কেবল Pop হবে।
3. **ধাপ ৩:** প্রাপ্ত Output-টিকে আবার উল্টে (Reverse) দাও।

---

### 📝 উদাহরণ (Infix ➔ Prefix):
**Infix Expression:** `A + B * (C - D) / E`

#### 🔹 ধাপ ১: উল্টানো Expression (Reverse Infix)
`E / (D - C) * B + A`

#### 🔹 ধাপ ২: `E / (D - C) * B + A` এর Postfix বের করা

| Symbol | Stack State | Output | ব্যাখ্যা / বিবরণ |
| :---: | :--- | :--- | :--- |
| **`E`** | `খালি` | `E` | Operand ➔ Output |
| **`/`** | `/` | `E` | Operator ➔ Stack |
| **`(`** | `/ (` | `E` | ব্র্যাকেট ➔ Push |
| **`D`** | `/ (` | `E D` | Operand ➔ Output |
| **`-`** | `/ ( -` | `E D` | Operator ➔ Push |
| **`C`** | `/ ( -` | `E D C` | Operand ➔ Output |
| **`)`** | `/` | `E D C -` | `)` পাওয়া গেছে ➔ `-` Pop হলো |
| **`*`** | `/ *` | `E D C -` | `*` ও `/` সমান ক্ষমতা, Prefix এর উল্টানো নিয়মে Pop হবে না ➔ Push |
| **`B`** | `/ *` | `E D C - B` | Operand ➔ Output |
| **`+`** | `+` | `E D C - B * /` | `+` এর চেয়ে `*` ও `/` দুটিই বড় ➔ দুটিই Pop হলো |
| **`A`** | `+` | `E D C - B * / A` | Operand ➔ Output |
| **End** | `খালি` | `E D C - B * / A +` | Stack-এর বাকি `+` Pop হলো |

#### 🔹 ধাপ ৩: Output-কে আবার উল্টানো (Final Reverse)
ধাপ ২ এর Output: `E D C - B * / A +`  
আবার উল্টালে পাই: **`+ A / * B - C D E`**

✅ **চূড়ান্ত Prefix উত্তর:** `+ A / * B - C D E`

---

## ৪. Postfix to Infix Conversion

### 📜 মূল নিয়ম (Scan: বাম থেকে ডানে ➔):
1. **Operand পেলে:** স্ট্যাকে Push করো।
2. **Operator পেলে:** স্ট্যাক থেকে ২টি উপাদান Pop করো:
   - ২য় বের হওয়া উপাদান = **`op1`**
   - ১ম বের হওয়া উপাদান = **`op2`**
   - এদের মাঝে অপারেটর বসিয়ে ব্র্যাকেটে আঁকো: **`(op1 Operator op2)`**
   - নতুন তৈরি হওয়া অংশটিকে আবার স্ট্যাকে Push করো।
3. লাইন শেষ হলে স্ট্যাকে থাকা অংশটিই **Infix**!

---

### 📝 উদাহরণ (Postfix ➔ Infix):
**Postfix Expression:** `A B C * + D E / -`

| Token | Stack State | বিবরণ / কাজ |
| :---: | :--- | :--- |
| **`A`** | `A` | Operand ➔ Push |
| **`B`** | `A`, `B` | Operand ➔ Push |
| **`C`** | `A`, `B`, `C` | Operand ➔ Push |
| **`*`** | `A`, **`(B * C)`** | Pop `C` & `B`. হলো `(B * C)` ➔ Push |
| **`+`** | **`(A + (B * C))`** | Pop `(B * C)` & `A`. হলো `(A + (B * C))` ➔ Push |
| **`D`** | `(A + (B * C))`, `D` | Operand ➔ Push |
| **`E`** | `(A + (B * C))`, `D`, `E` | Operand ➔ Push |
| **`/`** | `(A + (B * C))`, **`(D / E)`** | Pop `E` & `D`. হলো `(D / E)` ➔ Push |
| **`-`** | **`((A + (B * C)) - (D / E))`** | Pop `(D / E)` & `(A + (B * C))`. হলো `((A + (B * C)) - (D / E))` |

✅ **চূড়ান্ত Infix উত্তর:** `(A + (B * C)) - (D / E)`

---

## ৫. Postfix to Prefix Conversion

### 📜 মূল নিয়ম (Scan: বাম থেকে ডানে ➔):
1. **Operand পেলে:** স্ট্যাকে Push করো।
2. **Operator পেলে:** স্ট্যাক থেকে ২টি উপাদান Pop করো:
   - ২য় বের হওয়া উপাদান = **`op1`**
   - ১ম বের হওয়া উপাদান = **`op2`**
   - ব্র্যাকেট ছাড়া অপারেটরকে সবার সামনে বসাও: **`Operator op1 op2`**
   - এটাকে আবার স্ট্যাকে Push করো।
3. লাইন শেষ হলে স্ট্যাকে থাকা ফলটিই **Prefix**!

---

### 📝 উদাহরণ (Postfix ➔ Prefix):
**Postfix Expression:** `A B C * + D E / -`

| Token | Stack State | বিবরণ / কাজ |
| :---: | :--- | :--- |
| **`A`** | `A` | Operand ➔ Push |
| **`B`** | `A`, `B` | Operand ➔ Push |
| **`C`** | `A`, `B`, `C` | Operand ➔ Push |
| **`*`** | `A`, **`* B C`** | Pop `C` & `B`. তৈরি হলো `* B C` ➔ Push |
| **`+`** | **`+ A * B C`** | Pop `* B C` & `A`. তৈরি হলো `+ A * B C` ➔ Push |
| **`D`** | `+ A * B C`, `D` | Operand ➔ Push |
| **`E`** | `+ A * B C`, `D`, `E` | Operand ➔ Push |
| **`/`** | `+ A * B C`, **`/ D E`** | Pop `E` & `D`. তৈরি হলো `/ D E` ➔ Push |
| **`-`** | **`- + A * B C / D E`** | Pop `/ D E` & `+ A * B C`. তৈরি হলো `- + A * B C / D E` |

✅ **চূড়ান্ত Prefix উত্তর:** `- + A * B C / D E`

---

## ৬. Prefix to Infix Conversion

> ⚠️ **বিশেষ নিয়ম:** Prefix থেকে রূপান্তর করার সময় সবসময় **ডান থেকে বামে (Right to Left ⬅️)** স্ক্যান করতে হয়।

### 📜 মূল নিয়ম (Scan: ডান থেকে বামে ⬅️):
1. **Operand পেলে:** স্ট্যাকে Push করো।
2. **Operator পেলে:** স্ট্যাক থেকে ২টি উপাদান Pop করো:
   - ১ম বের হওয়া উপাদান = **`op1`**
   - ২য় বের হওয়া উপাদান = **`op2`**
   - এদের মাঝে অপারেটর বসিয়ে ব্র্যাকেটে আঁকো: **`(op1 Operator op2)`**
   - নতুন অংশটিকে আবার স্ট্যাকে Push করো।
3. শেষ পর্যন্ত স্ট্যাকে যা থাকবে সেটাই **Infix**!

---

### 📝 উদাহরণ (Prefix ➔ Infix):
**Prefix Expression:** `- + A * B C / D E`

| Token (ডান থেকে বামে) | Stack State | বিবরণ / কাজ |
| :---: | :--- | :--- |
| **`E`** | `E` | Operand ➔ Push |
| **`D`** | `E`, `D` | Operand ➔ Push |
| **`/`** | **`(D / E)`** | Pop 1st=`D` (`op1`), 2nd=`E` (`op2`). হলো `(D / E)` ➔ Push |
| **`C`** | `(D / E)`, `C` | Operand ➔ Push |
| **`B`** | `(D / E)`, `C`, `B` | Operand ➔ Push |
| **`*`** | `(D / E)`, **`(B * C)`** | Pop 1st=`B`, 2nd=`C`. হলো `(B * C)` ➔ Push |
| **`A`** | `(D / E)`, `(B * C)`, `A` | Operand ➔ Push |
| **`+`** | `(D / E)`, **`(A + (B * C))`** | Pop 1st=`A`, 2nd=`(B * C)`. হলো `(A + (B * C))` ➔ Push |
| **`-`** | **`((A + (B * C)) - (D / E))`** | Pop 1st=`(A + (B * C))`, 2nd=`(D / E)`. হলো `((A + (B * C)) - (D / E))` |

✅ **চূড়ান্ত Infix উত্তর:** `(A + (B * C)) - (D / E)`

---

## ৭. Prefix to Postfix Conversion

### 📜 মূল নিয়ম (Scan: ডান থেকে বামে ⬅️):
1. **Operand পেলে:** স্ট্যাকে Push করো।
2. **Operator পেলে:** স্ট্যাক থেকে ২টি উপাদান Pop করো:
   - ১ম বের হওয়া উপাদান = **`op1`**
   - ২য় বের হওয়া উপাদান = **`op2`**
   - ব্র্যাকেট ছাড়া অপারেটরটিকে শেষে বসাও: **`op1 op2 Operator`**
   - এটাকে আবার স্ট্যাকে Push করো।
3. শেষ পর্যন্ত স্ট্যাকে যা থাকবে সেটাই **Postfix**!

---

### 📝 উদাহরণ (Prefix ➔ Postfix):
**Prefix Expression:** `- + A * B C / D E`

| Token (ডান থেকে বামে) | Stack State | বিবরণ / কাজ |
| :---: | :--- | :--- |
| **`E`** | `E` | Operand ➔ Push |
| **`D`** | `E`, `D` | Operand ➔ Push |
| **`/`** | **`D E /`** | Pop 1st=`D`, 2nd=`E`. তৈরি হলো `D E /` ➔ Push |
| **`C`** | `D E /`, `C` | Operand ➔ Push |
| **`B`** | `D E /`, `C`, `B` | Operand ➔ Push |
| **`*`** | `D E /`, **`B C *`** | Pop 1st=`B`, 2nd=`C`. তৈরি হলো `B C *` ➔ Push |
| **`A`** | `D E /`, `B C *`, `A` | Operand ➔ Push |
| **`+`** | `D E /`, **`A B C * +`** | Pop 1st=`A`, 2nd=`B C *`. তৈরি হলো `A B C * +` ➔ Push |
| **`-`** | **`A B C * + D E / -`** | Pop 1st=`A B C * +`, 2nd=`D E /`. তৈরি হলো `A B C * + D E / -` |

✅ **চূড়ান্ত Postfix উত্তর:** `A B C * + D E / -`

---

## ৮. গাণিতিক প্রমাণ ও ভ্যালিডেশন

আমরা একই উদাহরণ সব জায়গায় ব্যবহার করেছি:
* **Infix:** `A + B * C - D / E`
* **Postfix:** `A B C * + D E / -`
* **Prefix:** `- + A * B C / D E`

ধরি, `A = 2`, `B = 3`, `C = 4`, `D = 10`, `E = 2`

1. **Infix Evaluation:**  
   `2 + 3 * 4 - 10 / 2`  
   ➔ `2 + 12 - 5`  
   ➔ `14 - 5`  
   ➔ **`9`**

2. **Postfix Evaluation (`2 3 4 * + 10 2 / -`):**  
   - `3 4 *` = 12 ➔ `2 12 + 10 2 / -`  
   - `2 12 +` = 14 ➔ `14 10 2 / -`  
   - `10 2 /` = 5 ➔ `14 5 -`  
   - `14 5 -` = **`9`** *(প্রমাণিত)*

3. **Prefix Evaluation (`- + 2 * 3 4 / 10 2`):**  
   - `* 3 4` = 12 ➔ `- + 2 12 / 10 2`  
   - `+ 2 12` = 14 ➔ `- 14 / 10 2`  
   - `/ 10 2` = 5 ➔ `- 14 5`  
   - `- 14 5` = **`9`** *(প্রমাণিত)*

---

## ৯. ফাইনাল চিট শিট (Ultimate Cheat Sheet)

### 🚀 স্ট্যাক পপিং রুলস (Infix থেকে Convert করার সময়):
- **Infix to Postfix:** স্ট্যাকে সমান বা বেশি ক্ষমতার অপারেটর থাকলে Pop হবে (`>=`)
- **Infix to Prefix (3-Step Method):** স্ট্যাকে শুধুমাত্র কঠোরভাবে বেশি ক্ষমতার অপারেটর থাকলে Pop হবে (`>`)

---

### 🚀 ৪টি শর্টকাট রিভার্স রূপান্তর চিট শিট:

| রূপান্তর (Conversion) | স্ক্যান দিক (Direction) | ১ম Pop উপাদান | ২য় Pop উপাদান | তৈরি করা ফরম্যাট (Format) |
| :--- | :---: | :---: | :---: | :---: |
| **Postfix ➔ Infix** | বাম ➔ ডান | `op2` | `op1` | `(op1 Operator op2)` |
| **Postfix ➔ Prefix** | বাম ➔ ডান | `op2` | `op1` | `Operator op1 op2` |
| **Prefix ➔ Infix** | **ডান ➔ বাম** ⬅️ | `op1` | `op2` | `(op1 Operator op2)` |
| **Prefix ➔ Postfix** | **ডান ➔ বাম** ⬅️ | `op1` | `op2` | `op1 op2 Operator` |

---
*গাইডটি সফলভাবে তৈরি করা হয়েছে।*
