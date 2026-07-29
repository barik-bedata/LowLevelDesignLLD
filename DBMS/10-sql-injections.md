## 16. SQL Injection (SQLi) & Security

### SQL Injection কী?
SQL Injection বা SQLi হলো ডেটাবেসের অন্যতম ভয়াবহ এবং কমন একটি হ্যাকিং মেথড। সহজ ভাষায়: ইউজার ইনপুটের (যেমন: লগিন ফর্ম বা সার্চ বক্স) মাধ্যমে হ্যাকাররা যদি আপনার অ্যাপ্লিকেশনে নিজেদের লেখা ক্ষতিকর (Malicious) SQL কোড ঢুকিয়ে (Inject) দেয় এবং ডেটাবেস যদি সেটাকে নিজের কোড মনে করে রান করে ফেলে, তাকেই SQL Injection বলে।

এর ফলে হ্যাকাররা বিনা পাসওয়ার্ডে সিস্টেমে ঢুকে যেতে পারে, ইউজারের ডেটা চুরি করতে পারে অথবা পুরো ডেটাবেস ডিলিট করে দিতে পারে!

### হ্যাকিং কীভাবে হয়? (Vulnerable Code & String Concatenation)
ধরি, আমাদের একটি লগিন সিস্টেম আছে। আমরা ইউজারের ইনপুট সরাসরি SQL স্ট্রিংয়ের সাথে যুক্ত (Concatenate) করে দিচ্ছি:

```python
# ❌ DANGEROUS CODE (DO NOT USE)
username_input = "admin' OR '1'='1"  # হ্যাকারের দেওয়া ইনপুট!
query = "SELECT * FROM Users WHERE username = '" + username_input + "' AND password = 'xxx'"
```

**লজিক (কেন হ্যাক হলো):** 
হ্যাকার ইউজারনেম ফিল্ডে লিখল: `admin' OR '1'='1`। 
ফলে আমাদের ডেটাবেসে যে কোডটি রান হবে তা দেখতে এমন হবে:
`SELECT * FROM Users WHERE username = 'admin' OR '1'='1' AND password = 'xxx'`

খেয়াল করুন, হ্যাকার একটি সিঙ্গেল কোটেশন `'` দিয়ে `username` স্ট্রিংটি ক্লোজ করে দিয়েছে এবং তারপর `OR '1'='1'` লিখেছে। ডেটাবেস দেখবে "username কি admin? না হলে সমস্যা নেই, 1 কি 1 এর সমান? হ্যাঁ!" যেহেতু `1=1` সবসময়ই সত্য (True), তাই `OR` লজিকের কারণে ডেটাবেস পাসওয়ার্ড চেক না করেই হ্যাকারকে অ্যাডমিন প্যানেলে লগিন করিয়ে দেবে!

### Prevention (বাঁচার উপায়)

**১. Parameterized Queries / Prepared Statements:** 
SQL Injection ঠেকানোর একমাত্র এবং সবচেয়ে কার্যকরী উপায় হলো Parameterized Query ব্যবহার করা। এখানে কোড এবং ডেটা (ইনপুট) আলাদা করে ডেটাবেসে পাঠানো হয়।

```python
# ✅ SECURE CODE (Prepared Statement)
username_input = "admin' OR '1'='1" 
# ডেটাবেস এই পুরো লাইনটাকে একটা সাধারণ টেক্সট (String) হিসেবে নেবে, কোড হিসেবে নয়!
cursor.execute("SELECT * FROM Users WHERE username = %s AND password = %s", (username_input, pass_input))
```
এখানে ডেটাবেস জানে যে `%s` এর জায়গায় যা-ই আসুক না কেন, তা হলো ডেটা, কোড নয়। তাই হ্যাকার যদি `OR '1'='1'` লিখেও দেয়, ডেটাবেস সেটাকে রান করবে না; বরং সে এমন একজন ইউজারকে খুঁজবে যার আসল ইউজারনেমই হলো `admin' OR '1'='1` (যা অবশ্যই খুঁজে পাবে না)।

**২. ORM ব্যবহার করা (Use Object-Relational Mapping):** 
আধুনিক ORM গুলো (যেমন: Prisma, Hibernate, Mongoose, Django ORM, EF Core) বাই-ডিফল্ট Parameterized Query ব্যবহার করে। তাই র-কোয়েরির (Raw Query) বদলে ORM ব্যবহার করলে SQL Injection-এর ভয় অনেকটাই কমে যায়।

**৩. Principle of Least Privilege (ন্যূনতম অধিকার নীতি):** 
অ্যাপ্লিকেশনের ডেটাবেস ইউজারকে শুধু ততটুকুই পারমিশন দিন যতটুকু তার দরকার। একটি সাধারণ ওয়েব অ্যাপ্লিকেশনের ডেটাবেস ইউজারের পুরো টেবিল `DROP` বা `TRUNCATE` করার পারমিশন কোনোভাবেই থাকা উচিত নয়।

---

## 17. WellDev Interview Questions & Past Year Insights

WellDev (and top tech companies in Bangladesh like Brain Station 23, Enosis, Thermax) evaluate DBMS concepts heavily in both online written screening tests and live technical interviews.

### 📝 Frequently Asked Theory Questions:
1. **Explain the difference between `TRUNCATE`, `DROP`, and `DELETE`.**
2. **What is the N+1 query problem? How do you diagnose and fix it in your preferred ORM?**
3. **Compare Clustered vs Non-Clustered Indexes.**
4. **Explain ACID properties with a real-world bank transfer example.**
5. **What are the SQL Transaction Isolation levels? Explain Dirty Read vs Phantom Read.**
6. **When would you choose NoSQL over a Relational SQL database?**
7. **Explain Boyce-Codd Normal Form (BCNF) with an example.**

---

### 💻 Frequently Asked SQL Coding Problems:
1. **Find N-th highest salary** using Window Functions and Subqueries.
2. **Find duplicate records** and delete all except the latest entry.
3. **Find employees earning more than their direct managers** (Self Join).
4. **Department Highest Salary:** Write a query to find employees who have the highest salary in each department.
5. **Consecutive Numbers:** Find all numbers that appear at least three times consecutively in a table.

---
*Created for LowLevelDesignLLD Study Repository.*
