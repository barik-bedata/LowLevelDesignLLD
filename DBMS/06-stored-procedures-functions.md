## 9. Transactions, ACID Properties, Locks, Views & Triggers

### A. ACID Properties
* **Atomicity (A - অখণ্ডতা):** "All or Nothing"। ট্রানজেকশনের ভেতরের সবগুলো কাজ সফল হতে হবে, অথবা যেকোনো একটি কাজ ফেইল করলে পুরো ট্রানজেকশনটিই বাতিল বা রোলব্যাক (Rollback) হবে।
* **Consistency (C - ধারাবাহিকতা বা বৈধতা):** ট্রানজেকশনের আগে এবং পরে ডেটাবেসের সমস্ত রুলস ঠিক থাকতে হবে। অর্থাৎ Primary Key, Foreign Key, Check Constraints, ডাটা টাইপ, Max/Min limit বা ব্যালেন্স নেগেটিভ না হওয়া—এই সব লজিক মেইনটেইন হতে হবে। যদি কোনো রুল ভঙ্গ হয়, তবে ট্রানজেকশন বাতিল হবে। 
* **Isolation (I - বিচ্ছিন্নতা):** একাধিক ট্রানজেকশন একসাথে (Concurrent) চললেও তারা একে অপরের কাজ দেখতে পাবে না বা একে অপরের কাজে বাধা দেবে না। প্রতিটি ট্রানজেকশন এমনভাবে চলবে যেন সে একাই সিস্টেমে কাজ করছে।
* **Durability (D - স্থায়িত্ব):** ট্রানজেকশন একবার সফলভাবে 'Commit' হয়ে গেলে, এরপর কারেন্ট চলে গেলেও বা সিস্টেম ক্র্যাশ করলেও ডেটা সেভ থাকবে (Redo logs এর মাধ্যমে)।

### B. Transaction Isolation Levels & Concurrency Anomalies

| Isolation Level | Dirty Read | Non-Repeatable Read | Phantom Read |
| :--- | :---: | :---: | :---: |
| **Read Uncommitted** | ❌ Allowed | ❌ Allowed | ❌ Allowed |
| **Read Committed** (Default PostgreSQL) | ✅ Prevented | ❌ Allowed | ❌ Allowed |
| **Repeatable Read** (Default MySQL InnoDB) | ✅ Prevented | ✅ Prevented | ❌ Allowed |
| **Serializable** | ✅ Prevented | ✅ Prevented | ✅ Prevented |

* **Dirty Read:** Reading uncommitted changes made by another transaction that later rolls back.
* **Non-Repeatable Read:** Reading the same row twice gets different values because another transaction modified & committed it.
* **Phantom Read:** Re-executing a query returns new "phantom" rows inserted by a committed concurrent transaction.

---

### C. Database Locks & Concurrency Control
* **Shared Lock (S-Lock):** Used for Read operations. Multiple transactions can hold S-Locks concurrently.
* **Exclusive Lock (X-Lock):** Used for Write operations (`UPDATE`/`DELETE`). Only one transaction can hold an X-Lock.
* **Pessimistic Locking:** Locks resources proactively before reading/writing (`SELECT ... FOR UPDATE`).
* **Optimistic Locking:** Does not lock rows during read. Verifies version/timestamp on update (`WHERE id = 1 AND version = 5`).

---

### D. Views vs Materialized Views

| Feature | Standard View | Materialized View |
| :--- | :--- | :--- |
| **Storage** | Virtual query representation (Zero disk storage) | Physically persisted table on disk |
| **Performance** | Executes underlying query on **every call** | Blazing fast (Reads pre-computed disk data) |
| **Data Freshness** | Always real-time fresh | Stale until refreshed explicitly (`REFRESH MATERIALIZED VIEW`) |

---

## 10. Stored Procedures vs Functions

| Feature | Stored Procedure | User-Defined Function (UDF) |
| :--- | :--- | :--- |
| **Return Value** | Optional (Can return 0, 1, or multiple parameters) | **Mandatory** (Must return a single scalar or table) |
| **DML Statements** | Allowed (`INSERT`, `UPDATE`, `DELETE`) | **Not Allowed** (Read-only operations) |
| **Execution** | Called using `CALL procedure_name()` or `EXEC` | Used directly in SQL queries (`SELECT dbo.MyFunc()`) |
| **Transaction Control** | Can manage transactions (`COMMIT`, `ROLLBACK`) | Cannot execute transaction control statements |

---

