# 🗄️ Comprehensive DBMS & SQL Guide for Software Engineers & Interviews

> **Target Audience:** Software Engineers, Tech Interviewees (WellDev, Brain Station 23, Enosis, etc.), and System Designers.  
> **Source Material:** DBMS Theory & System Design Bangla Notebook.

---

## 📋 Table of Contents
1. [Classification of SQL Commands (DDL, DML, DQL, DCL, TCL)](#1-classification-of-sql-commands)
2. [DROP vs TRUNCATE vs DELETE](#2-drop-vs-truncate-vs-delete)
3. [Cascading Operations in SQL](#3-cascading-operations-in-sql)
4. [Keys & Indexing Deep Dive](#4-keys--indexing-deep-dive)
5. [Normalization & Denormalization](#5-normalization--denormalization)
6. [SQL Query Execution Order](#6-sql-query-execution-order)
7. [SQL Joins & Execution Strategies](#7-sql-joins--execution-strategies)
8. [SQL Top Problem Solving (Nth Highest Salary & More)](#8-sql-top-problem-solving)
9. [Transactions, ACID Properties, Locks, Views & Triggers](#9-transactions-acid-properties-locks-views--triggers)
10. [Stored Procedures vs Functions](#10-stored-procedures-vs-functions)
11. [ER Diagrams & Relationship Modeling](#11-er-diagrams--relationship-modeling)
12. [Distributed DBMS: Sharding, Connection Pool & ORM](#12-distributed-dbms-sharding-connection-pool--orm)
13. [N+1 Query Problem & Solutions](#13-n1-query-problem--solutions)
14. [CAP & PACELC Theorems](#14-cap--pacelc-theorems)
15. [When to Use SQL vs NoSQL](#15-when-to-use-sql-vs-nosql)
16. [SQL Injection (SQLi) & Security](#16-sql-injection-sqli--security)
17. [WellDev Interview Questions & Past Year Insights](#17-welldev-interview-questions--past-year-insights)

---

## 1. Classification of SQL Commands

SQL commands are categorized based on their functional purpose within the Database Management System (DBMS).

```
                            ┌────────────────────────────────────────┐
                            │              SQL Commands              │
                            └───────────────────┬────────────────────┘
                                                │
       ┌───────────────┬────────────────┬───────┴────────┬────────────────┐
┌──────▼──────┐ ┌──────▼──────┐  ┌──────▼──────┐  ┌──────▼──────┐  ┌──────▼──────┐
│     DDL     │ │     DML     │  │     DQL     │  │     DCL     │  │     TCL     │
│ (Definition)│ │(Manipulation)│ │   (Query)   │  │  (Control)  │  │(Transaction)│
└─────────────┘ └─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘
```

### A. DDL (Data Definition Language)
* **Purpose:** Modifies the **structure/schema** of database objects (tables, indexes, views, schemas).
* **Auto-Commit:** Yes (DDL statements implicitly commit current transactions in most RDBMS).
* **Key Commands:**
  * `CREATE`: Creates a new table, database, view, or index.
  * `ALTER`: Modifies an existing database structure (add/drop columns, constraints).
  * `DROP`: Deletes an entire database object (structure + data).
  * `TRUNCATE`: Removes all records from a table and resets identity counter.
  * `RENAME`: Renames a database object.

```sql
-- DDL Examples
CREATE TABLE Users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE
);

ALTER TABLE Users ADD COLUMN created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP;
```

### B. DML (Data Manipulation Language)
* **Purpose:** Manipulates the **data stored inside** the tables.
* **Auto-Commit:** No (Requires explicit `COMMIT` unless auto-commit is enabled).
* **Key Commands:**
  * `INSERT`: Inserts new records into a table.
  * `UPDATE`: Modifies existing data within a table.
  * `DELETE`: Deletes specific or all records based on conditions.

```sql
-- DML Examples
INSERT INTO Users (name, email) VALUES ('Rahim', 'rahim@example.com');
UPDATE Users SET name = 'Rahim Ahmed' WHERE user_id = 1;
DELETE FROM Users WHERE user_id = 1;
```

### C. DQL (Data Query Language)
* **Purpose:** Used to **fetch/retrieve data** from the database.
* **Key Command:**
  * `SELECT`: Retrieves data from one or more tables.

```sql
-- DQL Example
SELECT user_id, name, email FROM Users WHERE email LIKE '%@example.com';
```

### D. DCL (Data Control Language)
* **Purpose:** Controls **permissions and privileges** on database objects.
* **Key Commands:**
  * `GRANT`: Gives user access privileges to database objects.
  * `REVOKE`: Withdraws user access privileges.

```sql
-- DCL Examples
GRANT SELECT, INSERT ON Users TO 'app_user'@'localhost';
REVOKE INSERT ON Users FROM 'app_user'@'localhost';
```

### E. TCL (Transaction Control Language)
* **Purpose:** Manages **transactions** and maintains data integrity (ACID compliance).
* **Key Commands:**
  * `COMMIT`: Saves changes permanently to the database.
  * `ROLLBACK`: Reverts changes back to the last committed state or savepoint.
  * `SAVEPOINT`: Creates a checkpoint within a transaction for conditional rollback.

```sql
-- TCL Example
BEGIN TRANSACTION;
UPDATE Accounts SET balance = balance - 500 WHERE account_id = 101;
UPDATE Accounts SET balance = balance + 500 WHERE account_id = 102;
SAVEPOINT transfer_done;

-- If an error occurs:
-- ROLLBACK TO transfer_done;
COMMIT;
```

---

## 2. DROP vs TRUNCATE vs DELETE

এটি ইন্টারভিউতে সবচেয়ে বেশি জিজ্ঞাসিত প্রশ্নগুলোর একটি। নিচে এদের মূল পার্থক্যসমূহ তুলে ধরা হলো:

| বৈশিষ্ট্য (Feature) | `DELETE` | `TRUNCATE` | `DROP` |
| :--- | :--- | :--- | :--- |
| **কমান্ডের ধরণ (Type)** | DML (Data Manipulation Language) | DDL (Data Definition Language) | DDL (Data Definition Language) |
| **কাজ (Action)** | টেবিল ঠিক রেখে ভেতরের নির্দিষ্ট বা সব রো (rows) ডিলেট করে। | টেবিল ঠিক রেখে ভেতরের সব রো (rows) একবারে ডিলেট করে। | সম্পূর্ণ টেবিলের স্ট্রাকচার (schema), ইনডেক্স এবং ডেটা চিরতরে মুছে ফেলে। |
| **`WHERE` ক্লজ** | **সাপোর্ট করে** (নির্দিষ্ট রো ডিলেট করা সম্ভব)। | **সাপোর্ট করে না** (সব ডেটা একসাথে ডিলেট হয়)। | **সাপোর্ট করে না** (সম্পূর্ণ টেবিলই ডিলেট হয়ে যায়)। |
| **গতি (Performance)** | **ধীরগতির** (প্রতিটি রো আলাদাভাবে মুছে দেয় এবং ট্রানজেকশন লগ রাখে)। | **অত্যন্ত দ্রুতগতির** (সরাসরি টেবিলের ডেটা পেজগুলো খালি করে দেয়)। | **তাত্ক্ষণিক** (সরাসরি ডেটাবেস মেটাডেটা থেকে টেবিলটি মুছে ফেলে)। |
| **ট্রিগার (Triggers)** | **ট্রিগার ফায়ার হয়** (প্রতিটি রো ডিলেটের সময় `DELETE` ট্রিগার রান করে)। | **ট্রিগার ফায়ার হয় না** (কোনো ট্রিগার রান করে না)। | **ট্রিগার ফায়ার হয় না** (কোনো ট্রিগার রান করে না)। |
| **রোলব্যাক (Rollback)** | **সবসময় সম্ভব** (রোলব্যাক করে ডেটা ফিরিয়ে আনা যায়)। | **সাধারণত সম্ভব নয়** (MySQL/Oracle-এ অটো-কমিট হওয়ায় সম্ভব নয়। তবে Postgres/SQL Server-এ সম্ভব)। | **সাধারণত সম্ভব নয়** (টেবিলটিই মুছে যায়। তবে Postgres-এ ট্রানজেকশনের ভেতর সম্ভব)। |

### উদাহরণসহ বিস্তারিত ব্যাখ্যা (Detailed Explanation with Example)

ধরি আমাদের কাছে **`employees`** নামে একটি টেবিল রয়েছে:

| id | name | salary |
| :--- | :--- | :--- |
| 1 | Rahim | 50000 |
| 2 | Karim | 25000 |
| 3 | Shafi | 45000 |

---

#### ১. `DELETE` উদাহরণ:
```sql
DELETE FROM employees WHERE salary < 30000;
```
* **কী ঘটবে?** 
  - এটি শুধুমাত্র ২ নম্বর আইডিধারী `Karim` (যার বেতন ২৫,০০০) এর রো-টি মুছে দেবে। 
  - বাকিদের ডেটা অক্ষত থাকবে। 
  - আপনি চাইলে ট্রানজেকশনের মাধ্যমে এই ডিলিট হওয়া ডেটাটি `ROLLBACK` করে ফেরত আনতে পারবেন।
  - টেবিল এবং বাকি ডেটা যথারীতি থাকবে।

#### ২. `TRUNCATE` উদাহরণ:
```sql
TRUNCATE TABLE employees;
```
* **কী ঘটবে?**
  - এটি টেবিলের ভেতরের সব রো (১, ২, এবং ৩ নম্বর রো) একবারে সম্পূর্ণ মুছে ফেলবে।
  - টেবিলের স্ট্রাকচার (`id`, `name`, `salary` কলামের হেডারগুলো) খালি অবস্থায় থেকে যাবে (টেবিলটি ডিলিট হবে না)।
  - এটি প্রতিটি রো আলাদা করে মুছে না, বরং সরাসরি ডেটা পেজগুলো খালি করে দেয়। তাই এটি অনেক দ্রুত কাজ করে।
  - সাধারণত এটি `ROLLBACK` করা যায় না (কিছু স্পেশাল ডিবি ব্যতীত) এবং কোনো `DELETE` ট্রিগার ফায়ার হয় না।

#### ৩. `DROP` উদাহরণ:
```sql
DROP TABLE employees;
```
* **কী ঘটবে?**
  - এটি সম্পূর্ণ `employees` টেবিলটিকেই ডেটাবেস থেকে চিরতরে মুছে ফেলবে (ডেটা + টেবিল স্ট্রাকচার দুটোই গায়েব)।
  - এর পর যদি আপনি `SELECT * FROM employees;` কুয়েরি চালান, তবে ডেটাবেস **"Table does not exist"** এরর দেখাবে।
  - এটি কোনোভাবেই `ROLLBACK` করা সম্ভব নয়।

---

## 3. Cascading Operations in SQL

প্যারেন্ট টেবিলের (parent table) কোনো প্রাইমারি কী আপডেট বা ডিলেট করা হলে চাইল্ড টেবিলের (child table) সংশ্লিষ্ট রো-গুলোর ওপর কী প্রভাব পড়বে, তা নির্ধারণ করে ক্যাসকেডিং কনস্ট্রেইন্ট (Cascading constraints)।

### Foreign Key Actions (`ON DELETE` / `ON UPDATE`)

১. **`ON DELETE CASCADE`**: প্যারেন্ট টেবিলের কোনো রো ডিলেট করা হলে চাইল্ড টেবিলের সংশ্লিষ্ট রেফারেন্সড রো-গুলোও স্বয়ংক্রিয়ভাবে ডিলেট হয়ে যাবে।
   * **বাস্তব উদাহরণ (Use Case):** কোনো `User` ডিলেট করা হলে তার করা সমস্ত `Posts` এবং `Comments` স্বয়ংক্রিয়ভাবে ডিলেট হয়ে যাবে।

২. **`ON DELETE SET NULL`**: প্যারেন্ট টেবিলের কোনো রো ডিলেট করা হলে চাইল্ড টেবিলের সংশ্লিষ্ট ফরেন কী কলামের মান স্বয়ংক্রিয়ভাবে `NULL` হয়ে যাবে।
   * **বাস্তব উদাহরণ (Use Case):** কোনো `Department` ডিলেট করা হলে উক্ত ডিপার্টমেন্টের সাথে যুক্ত `Employees` টেবিলে `department_id` কলামটির মান `NULL` হয়ে যাবে।

৩. **`ON DELETE SET DEFAULT`**: প্যারেন্ট টেবিলের কোনো রো ডিলেট করা হলে চাইল্ড টেবিলের সংশ্লিষ্ট ফরেন কী কলামটির মান আগে থেকে সংজ্ঞায়িত ডিফল্ট (default value) মানে সেট হয়ে যাবে।

৪. **`ON DELETE RESTRICT` / `NO ACTION`**: চাইল্ড টেবিলে কোনো রেফারেন্সড রো থাকলে প্যারেন্ট টেবিলের রো-টি ডিলেট হতে বাধা দেবে (এটি রান করলে Foreign Key Constraint Error দেখাবে)।

```sql
CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    user_id INT,
    order_date DATE,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
```

### ক্যাসকেডিং অপারেশনের বাস্তব উদাহরণ (Practical Example)

ধরি আমাদের ডেটাবেসে দুটি টেবিল রয়েছে:
1. **`departments`** (Parent Table)
2. **`employees`** (Child Table - এখানে `dept_id` হলো Foreign Key)

**প্যারেন্ট টেবিল (`departments`):**
| dept_id | dept_name |
| :--- | :--- |
| 1 | HR |
| 2 | Engineering |

**চাইল্ড টেবিল (`employees`):**
| emp_id | name | dept_id |
| :--- | :--- | :--- |
| 101 | Rahim | 1 |
| 102 | Karim | 2 |
| 103 | Shafi | 2 |

ধরি, আমরা প্যারেন্ট টেবিল থেকে **Engineering (`dept_id = 2`)** ডিপার্টমেন্টটি ডিলিট করতে চাই:
```sql
DELETE FROM departments WHERE dept_id = 2;
```

নিচে ৪টি নিয়মের ক্ষেত্রে চাইল্ড টেবিলটির অবস্থা কেমন হবে তা দেখানো হলো:

---

#### ১. `ON DELETE CASCADE` এর ক্ষেত্রে
প্যারেন্ট থেকে `dept_id = 2` ডিলিট করার সাথে সাথে চাইল্ড টেবিল থেকে Karim ও Shafi-এর রো দুটোও স্বয়ংক্রিয়ভাবে মুছে যাবে।

**আউটপুট চাইল্ড টেবিল (`employees`):**
| emp_id | name | dept_id |
| :--- | :--- | :--- |
| 101 | Rahim | 1 |

---

#### ২. `ON DELETE SET NULL` এর ক্ষেত্রে
প্যারেন্ট থেকে `dept_id = 2` ডিলিট হবে, কিন্তু চাইল্ড টেবিলে করিম ও শাফির `dept_id` কলামের মান `NULL` হয়ে যাবে (তারা কোনো ডিপার্টমেন্ট ছাড়া থাকবে, কিন্তু তাদের ডেটা ডিলিট হবে না)।

**আউটপুট চাইল্ড টেবিল (`employees`):**
| emp_id | name | dept_id |
| :--- | :--- | :--- |
| 101 | Rahim | 1 |
| 102 | Karim | `NULL` |
| 103 | Shafi | `NULL` |

---

#### ৩. `ON DELETE SET DEFAULT` এর ক্ষেত্রে
*(ধরি, `dept_id` কলামের ডিফল্ট মান হচ্ছে `1` বা 'HR')*
প্যারেন্ট থেকে `dept_id = 2` ডিলিট হবে এবং চাইল্ড টেবিলে করিম ও শাফির `dept_id` কলামের মান স্বয়ংক্রিয়ভাবে ডিফল্ট মান `1` এ পরিবর্তন হয়ে যাবে।

**আউটপুট চাইল্ড টেবিল (`employees`):**
| emp_id | name | dept_id |
| :--- | :--- | :--- |
| 101 | Rahim | 1 |
| 102 | Karim | 1 |
| 103 | Shafi | 1 |

---

#### ৪. `ON DELETE RESTRICT` / `NO ACTION` এর ক্ষেত্রে
যেহেতু চাইল্ড টেবিলে `dept_id = 2` এর ডেটা রয়েছে (করিম ও শাফি কাজ করছে), তাই ডেটাবেস প্যারেন্ট টেবিলের Engineering ডিপার্টমেন্টটি ডিলিট হতে **বাধা দিবে** এবং একটি **Foreign Key Constraint Error** দেখাবে। 

প্যারেন্ট এবং চাইল্ড দুটি টেবিলই অপরিবর্তিত থাকবে (কোনো ডেটা ডিলিট হবে না)।

---

## 4. Keys & Indexing Deep Dive

### A. Database Keys Overview

ডাটাবেস টেবিলের ডেটার মধ্যে সম্পর্ক স্থাপন এবং প্রতিটি রো-কে ইউনিকভাবে চিহ্নিত করার জন্য বিভিন্ন ধরণের **Keys** ব্যবহার করা হয়। নিচে এগুলোকে উদাহরণসহ বিস্তারিত ব্যাখ্যা করা হলো:

#### আমাদের প্রধান উদাহরণ টেবিল: `students`
ধরি আমাদের একটি `students` টেবিল রয়েছে:

| surrogate_id | student_id | nid | email | first_name | last_name |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | S101 | 123456 | rahim@test.com | Rahim | Rahman |
| 2 | S102 | 789012 | karim@test.com | Karim | Ahmed |
| 3 | S103 | 345678 | shafi@test.com | Shafi | Islam |

---

#### ১. Super Key (সুপার কী)
* **সংজ্ঞা**: যেকোনো কলাম বা একাধিক কলামের সমন্বয় যা টেবিলের প্রতিটি রো-কে অন্য রো থেকে ইউনিকলি (আলাদাভাবে) চিহ্নিত করতে পারে।
* **গুরুত্বপূর্ণ বৈশিষ্ট্য**: একটি সুপার কী-তে ইউনিক কলামের পাশাপাশি অতিরিক্ত বা অপ্রয়োজনীয় (redundant/unnecessary) কলামও থাকতে পারে। কলামের সেই পুরো সমন্বয়টি রো আইডেন্টিফাই করতে পারলে তাকে সুপার কী বলা যাবে।
* **আমাদের উদাহরণ**: 
  - `(student_id)`
  - `(nid)`
  - `(email)`
  - `(student_id, first_name)` -> এখানে `student_id` ইউনিক হওয়ার কারণে, সাথে `first_name` কলামটি অপ্রয়োজনীয় বা রিডানড্যান্ট হিসেবে যুক্ত থাকা সত্ত্বেও এই জোড়াটি একটি সুপার কী।
  - `(nid, email, last_name)` -> এখানে `nid` এবং `email` ইউনিক হওয়া সত্ত্বেও সাথে `last_name` কলামটি যুক্ত আছে, যা অপ্রয়োজনীয়। তবুও এটি একটি সুপার কী।
  - এই সবগুলোই সুপার কী, কারণ এদের প্রতিটির মান দিয়ে একটি নির্দিষ্ট ছাত্রের রো-কে ইউনিকভাবে চেনা সম্ভব।

---

#### ২. Candidate Key (ক্যান্ডিডেট কী)
* **সংজ্ঞা**: সুপার কী-গুলোর মধ্যে যে কলামগুলো **মিনিমাল (minimal)** কলাম নিয়ে গঠিত (অর্থাৎ অতিরিক্ত অপ্রয়োজনীয় কোনো কলাম থাকে না), সেগুলোকে ক্যান্ডিডেট কী বলে।
* **আমাদের উদাহরণ**:
  - `(student_id, first_name)` এটি সুপার কী হলেও ক্যান্ডিডেট কী নয়, কারণ `first_name` বাদ দিলেও `student_id` একা একটি রো চিহ্নিত করতে পারে।
  - এই টেবিলে ক্যান্ডিডেট কী হবে ৩টি: **`student_id`**, **`nid`**, এবং **`email`**। কারণ এদের প্রতিটি কলাম একা একটি রো চিহ্নিত করতে যথেষ্ট এবং এদের সাথে কোনো অতিরিক্ত কলাম নেই।

---

#### ৩. Primary Key (প্রাইমারি কী)
* **সংজ্ঞা**: ক্যান্ডিডেট কী-গুলোর মধ্য থেকে ডাটাবেস ডিজাইনার টেবিলের প্রধান আইডেন্টিফায়ার হিসেবে যাকে বেছে নেন, সেটাই হলো প্রাইমারি কী। এটি কখনো `NULL` (খালি) হতে পারে না এবং অবশ্যই ইউনিক হতে হবে।
* **আমাদের উদাহরণ**:
  - আমরা ক্যান্ডিডেট কী-গুলোর মধ্য থেকে **`student_id`**-কে প্রাইমারি কী হিসেবে বেছে নিলাম।

---

#### ৪. Alternate Key (অল্টারনেট কী)
* **সংজ্ঞা**: ক্যান্ডিডেট কী-গুলোর মধ্যে যে কলামগুলোকে প্রাইমারি কী হিসেবে বেছে নেওয়া **হয়নি**, সেগুলোকে অল্টারনেট কী বা সেকেন্ডারি কী বলা হয়।
* **আমাদের উদাহরণ**:
  - যেহেতু আমরা `student_id`-কে প্রাইমারি কী বানিয়েছি, তাই বাকি দুটি ক্যান্ডিডেট কী— **`nid`** এবং **`email`** হলো অল্টারনেট কী।

---

#### 5. Surrogate Key (সারোগেট কী)
* **সংজ্ঞা**: ব্যবহারকারীর বাস্তব কোনো তথ্য ছাড়া শুধুমাত্র ডাটাবেস রো-গুলোকে সহজে চিহ্নিত করার জন্য অটো-জেনারেটেড (যেমন: Auto-increment ID বা UUID) যে কৃত্রিম কী তৈরি করা হয়, তাকে সারোগেট কী বলে। এর কোনো বাস্তব ব্যবসায়িক বা ইউজার অর্থ থাকে না।
* **আমাদের উদাহরণ**:
  - আমাদের টেবিলের **`surrogate_id`** (1, 2, 3...) একটি সারোগেট কী। কারণ এটি ছাত্রের রোল বা এনআইডির মতো বাস্তব কোনো তথ্য নয়, শুধু ডাটাবেসে ডেটা ইনসার্ট করার সাথে সাথে অটোমেটিক তৈরি হয়েছে।

---

#### ৬. Composite Key (কম্পোজিট কী)
* **সংজ্ঞা**: যখন কোনো টেবিলের রো-কে ইউনিকভাবে চিহ্নিত করার জন্য একাধিক (২ বা তার বেশি) কলামকে একত্রে প্রাইমারি কী হিসেবে ব্যবহার করতে হয়, তখন তাকে কম্পোজিট কী বলে।
* **আমাদের উদাহরণ**: ধরি আমাদের একটি কোর্স রেজিস্ট্রেশন টেবিল `registrations` রয়েছে:
  
  | student_id (FK) | course_code | grade |
  | :--- | :--- | :--- |
  | S101 | CSE101 | A |
  | S101 | CSE102 | A- |
  | S102 | CSE101 | B |
  
  এখানে শুধু `student_id` দিয়ে রো ইউনিক করা যাবে না (যেহেতু একজন ছাত্র একাধিক কোর্স নিতে পারে)। আবার শুধু `course_code` দিয়েও রো ইউনিক হবে না। কিন্তু **`(student_id, course_code)`** এই দুটি কলাম একসাথে নিলে প্রতিটা রো ইউনিক হবে। এই জোড়াটিই হলো একটি কম্পোজিট কী।

* 💡 **কনসেপ্ট ক্লিয়ারিং ও ইন্টারভিউ লজিক (Concept & Interview Logic)**:
  - **প্রশ্ন ১**: যদি কোনো ক্যান্ডিডেট কী ২ বা তার বেশি কলাম নিয়ে গঠিত হয়, তবে তাকে কি কম্পোজিট কী বলা যায়?
    - **উত্তর**: **হ্যাঁ, অবশ্যই।** একাধিক কলামের সমন্বয়ে গঠিত যেকোনো ক্যান্ডিডেট কী-কে **কম্পোজিট ক্যান্ডিডেট কী** বলা হয়। এটি যখন প্রাইমারি কী হিসেবে নির্বাচিত হয় তখন তাকে **কম্পোজিট প্রাইমারি কী** বলা হয়।
  - **প্রশ্ন ২**: যদি একটিমাত্র কলাম (যেমন: `student_id` বা `nid`) দিয়ে কোনো টেবিলকে ইউনিকভাবে আইডেন্টিফাই করা যায়, তবে কি সেখানে কম্পোজিট কী লাগবে?
    - **উত্তর**: **না, মোটেও লাগবে না (আপনার লজিক ১০০% সঠিক)।** যদি একক কোনো কলাম দিয়ে রো ইউনিক করা সম্ভব হয়, তবে সেখানে অতিরিক্ত কলাম যুক্ত করে কম্পোজিট কী তৈরি করার কোনো প্রয়োজন নেই। এরূপ জোর করে অতিরিক্ত কলাম যুক্ত করা ক্যান্ডিডেট কী-এর **মিনিমালিটি (Minimality / Irreducibility)** শর্তকে লঙ্ঘন করে (ক্যান্ডিডেট কী-তে কোনো অপ্রয়োজনীয় কলাম থাকতে পারবে না)।
  - **প্রশ্ন ৩**: তাহলে কম্পোজিট কী কখন প্রয়োজন হয়?
    - **উত্তর**: কম্পোজিট কী কেবল তখনই প্রয়োজন হয় যখন টেবিলে এমন কোনো **একক কলাম (single column) থাকে না** যা দিয়ে প্রতিটি রো-কে ইউনিকলি চিহ্নিত করা সম্ভব (যেমন: ওপরের `registrations` টেবিল, যেখানে একাধিক স্টুডেন্ট এবং একাধিক কোর্স আইডি একসাথে মিলে ইউনিক কম্বিনেশন তৈরি করে)।

---

#### ৭. Foreign Key (ফরেন কী)
* **সংজ্ঞা**: একটি টেবিলের প্রাইমারি কী যখন অন্য কোনো টেবিলে রিলেশনশিপ তৈরি করার জন্য কলাম হিসেবে ব্যবহৃত হয়, তখন তাকে ফরেন কী বলে। এটি রিলেশনাল ডাটাবেসের ডেটার শুদ্ধতা (Referential Integrity) রক্ষা করে, অর্থাৎ ফরেন কী কলামে এমন কোনো মান ইনসার্ট করা যায় না যা প্যারেন্ট টেবিলের প্রাইমারি কী-তে নেই।

* 📊 **PK-FK রিলেশনশিপ ডায়াগ্রাম (Visual Representation)**:
  
  ![Primary Key to Foreign Key Relationship](resources/pk_fk_relationship.png)

---

### বিস্তারিত উদাহরণ (Detailed Examples)

নিচে দুটি বাস্তব উদাহরণের মাধ্যমে প্রাইমারি কী (PK) এবং ফরেন কী (FK)-এর সম্পর্ক দেখানো হলো:

#### উদাহরণ ১: Student (ছাত্র) এবং Enrollments (কোর্স রেজিস্ট্রেশন)
* **`students` টেবিল (Parent)**: এখানে প্রতিটি ছাত্রের ইউনিক আইডি `student_id` হলো **Primary Key (PK)**।
* **`enrollments` টেবিল (Child)**: একজন ছাত্র কোন কোন কোর্সে এনরোল করেছে তা এখানে থাকবে। এই টেবিলের `student_id` হলো **Foreign Key (FK)** যা `students` টেবিলের `student_id`-কে নির্দেশ করে।

**প্যারেন্ট টেবিল (`students`):**
| student_id (PK) | first_name | last_name | email |
| :--- | :--- | :--- | :--- |
| **S101** | Rahim | Rahman | rahim@test.com |
| **S102** | Karim | Ahmed | karim@test.com |

**চাইল্ড টেবিল (`enrollments`):**
| enrollment_id (PK) | student_id (FK) | course_id | grade |
| :--- | :--- | :--- | :--- |
| 1 | **S101** | CSE101 | A |
| 2 | **S101** | CSE102 | B+ |
| 3 | **S102** | CSE101 | A- |

> 💡 **নোট**: `enrollments` টেবিলের `student_id` কলামে এমন কোনো আইডি (যেমন: `S105`) ইনসার্ট করা যাবে না যা `students` টেবিলে নেই। করলে ডাটাবেস **Referential Integrity Constraint Violation** এরর দেখাবে।

---

#### উদাহরণ ২: Product (পণ্য) এবং Orders (অর্ডার)
* **`products` টেবিল (Parent)**: প্রতিটি পণ্যের ইউনিক আইডি `product_id` হলো **Primary Key (PK)**।
* **`orders` টেবিল (Child)**: কোনো কাস্টমার কোন পণ্য কতটি অর্ডার করেছে তা এই টেবিলে স্টোর করা হয়। এই টেবিলের `product_id` কলামটি হলো **Foreign Key (FK)** যা `products` টেবিলকে রেফার করে।

**প্যারেন্ট টেবিল (`products`):**
| product_id (PK) | product_name | category | price |
| :--- | :--- | :--- | :--- |
| **P501** | iPhone 15 | Electronics | 120000 |
| **P502** | Keyboard | Accessories | 3500 |

**চাইল্ড টেবিল (`orders`):**
| order_id (PK) | product_id (FK) | quantity | order_date |
| :--- | :--- | :--- | :--- |
| 10001 | **P501** | 1 | 2026-07-28 |
| 10002 | **P502** | 2 | 2026-07-28 |
| 10003 | **P501** | 1 | 2026-07-28 |

> 💡 **নোট**: এখানে `orders` টেবিলের `product_id` কলামটি প্যারেন্ট টেবিলের প্রোডাক্টের সত্যতা নিশ্চিত করে। যদি কোনো প্রোডাক্টের আইডি `products` টেবিল থেকে মুছে ফেলা হয়, তবে চাইল্ড টেবিলের অর্ডারগুলোর ওপর ক্যাসকেড অপারেশন (যেমন: `ON DELETE CASCADE` বা `SET NULL`) কার্যকর হয়।

---

### B. Indexing Mechanics & Architecture (ইনডেক্সিং মেকানিজম ও আর্কিটেকচার)

**ইনডেক্স (Index)** হলো ডাটাবেসের একটি বিশেষ সহায়ক ডাটা স্ট্রাকচার (যেমন: B+ Tree), যা ডাটাবেস থেকে খুব দ্রুত ডাটা খুঁজে পেতে সাহায্য করে।

* ⚖️ **ট্রেড-অফ (Trade-offs)**:
  - **সুবিধা**: রিড কুয়েরির (`SELECT`) গতি অনেক গুণ বাড়িয়ে দেয়।
  - **অসুবিধা**: অতিরিক্ত মেমরি স্পেসের প্রয়োজন হয় এবং রাইট অপারেশন (`INSERT`, `UPDATE`, `DELETE`) কিছুটা ধীরগতির হয়ে যায়, কারণ প্রতিবার ডাটা পরিবর্তনের সাথে সাথে ইনডেক্স স্ট্রাকচারটিকেও আপডেট করতে হয়।

#### B+ Tree ইনডেক্স আর্কিটেকচার:
ডাটাবেসের অধিকাংশ ইনডেক্স **B+ Tree** ডাটা স্ট্রাকচার ব্যবহার করে তৈরি হয়।

```
                    B+ Tree Index Structure
                           [ 50 ]                   <-- Root Node (রুট নোড)
                         /        \
                    [20, 35]     [65, 85]           <-- Internal Nodes (ইন্টারনাল নোড)
                    /   |   \    /   |   \
                  [Leaf Nodes with Pointers/Data]   <-- Leaf Nodes (লিফ নোড)
```
- **Root & Internal Nodes**: সার্চ ভ্যালু অনুযায়ী ডানে বা বামে যাওয়ার ডিরেকশন দেয়।
- **Leaf Nodes**: এগুলো একদম নিচের নোড, যা সরাসরি ডাটা রো (Clustered Index) অথবা ডাটা রো-এর অ্যাড্রেস/পয়েন্টার (Non-Clustered Index) ধারণ করে।

---

#### ১. Clustered Index vs Non-Clustered Index

| বৈশিষ্ট্য (Feature) | Clustered Index (ক্লাস্টার্ড ইনডেক্স) | Non-Clustered Index (নন-ক্লাস্টার্ড ইনডেক্স) |
| :--- | :--- | :--- |
| **ভৌত স্টোরেজ (Physical Storage)** | ডিস্কের মেমরিতে মূল ডাটা রোগুলোকে ইনডেক্সের ক্রমানুসারে সাজিয়ে রাখে। | মূল ডাটা রোগুলো এলোমেলো থাকে, ইনডেক্স আলাদা একটি জায়গায় কি (Key) এবং পয়েন্টার স্টোর করে রাখে। |
| **টেবিল প্রতি সংখ্যা** | একটি টেবিলে **সর্বোচ্চ ১টি** থাকতে পারে (সাধারণত Primary Key-তে অটো তৈরি হয়)। | একটি টেবিলে **একাধিক** থাকতে পারে (MySQL-এ সর্বোচ্চ ৬৪টি, SQL Server-এ ৯৯৯টি)। |
| **লিফ নোডের ভেতরের ডাটা (Leaf Node Content)** | সরাসরি টেবিলের **আসল ডাটা রো (Actual Data Row)** ধারণ করে। | ডাটা রো-এর বদলে আসল ডাটার **পয়েন্টার বা অ্যাড্রেস (RID/PK)** ধারণ করে। |
| **গতি (Speed)** | রেঞ্জ সার্চ (`BETWEEN`, `>`, `<`) এবং ক্রমানুসারে ডেটা খোঁজার জন্য অত্যন্ত দ্রুত। | কিছুটা ধীরগতির, কারণ প্রথমে ইনডেক্স খুঁজে সেখান থেকে পয়েন্টার নিয়ে আসল টেবিলে গিয়ে ডাটা আনতে হয় (Bookmark Lookup)। |

* 💡 **কনসেপ্ট ক্লিয়ারিং ও ইন্টারভিউ লজিক (Clustered Index Deep Dive)**:
  - **Clustered Index কি কি হতে পারে?**
    - **Primary Key (PK)**: সাধারণত, টেবিলের Primary Key-টিই ডিফল্টভাবে Clustered Index হিসেবে কাজ করে (যেমন: MySQL InnoDB-তে)।
    - **Unique Key**: যদি টেবিলে কোনো Primary Key না থাকে, তবে প্রথম `NOT NULL` বিশিষ্ট Unique Key-টি Clustered Index হিসেবে ব্যবহৃত হয়।
    - **Hidden Row ID**: যদি Primary Key বা Unique Key কোনোটিই না থাকে, তবে ডাটাবেস ইঞ্জিন (যেমন: InnoDB) নিজে থেকে একটি ৬-বাইটের লুকানো (Hidden Row ID) কলাম তৈরি করে সেটিকে Clustered Index হিসেবে ব্যবহার করে।
  - **এটি কি ডাটাকে ফিজিক্যালি সর্ট করে?**
    - **হ্যাঁ, অবশ্যই।** এটি ডিস্কের মধ্যে ডেটার **ভৌত বিন্যাস বা সর্টিং অর্ডার (Physical Sorting Order)** নির্ধারণ করে।
    - *বাস্তব অ্যানালজি*: একটি টেলিফোন ডিরেক্টরি বা ডিকশনারি যেমন ফিজিক্যালি নামের ক্রমানুসারে (Alphabetically) সাজানো থাকে, ক্লাস্টার্ড ইনডেক্স ঠিক তেমনই। যেহেতু ডাটা ডিস্কে যেকোনো একটি নির্দিষ্ট উপায়েই ফিজিক্যালি সাজানো থাকতে পারে, তাই একটি টেবিলে কেবল **১টিই** ক্লাস্টার্ড ইনডেক্স থাকা সম্ভব।
  - **সার্চ ও রাইটের Time Complexity কেমন?**
    - **সার্চের ক্ষেত্রে (Search Complexity)**:
      - **Clustered Index**: **$O(\log N)$**। B+ Tree ট্রাভার্স করে সরাসরি লিফ নোডেই আসল ডাটা রো পাওয়া যায় (মাত্র ১টি B+ Tree সার্চ ট্রাভার্সাল)।
      - **Non-Clustered Index**: **$O(\log N)$**। প্রথমে নন-ক্লাস্টার্ড B+ Tree সার্চ করে Row Pointer (বা Primary Key ID) খুঁজে নেওয়া হয়, তারপর সেই পয়েন্টার দিয়ে মূল টেবিলে গিয়ে ডাটা আনা হয় (Bookmark Lookup)। তাত্ত্বিকভাবে এটিও $O(\log N)$ হলেও কার্যত ক্লাস্টার্ড ইনডেক্সের চেয়ে ২ গুণ বেশি ডিস্ক I/O অপারেশন নেয়।
      - ⚠️ **কেন এটি $O(1)$ নয়? (Common Misconception)**:
        * অনেক সময় মনে হতে পারে ইনডেক্স দিয়ে খুঁজলে সরাসরি $O(1)$ এ ডাটা পাওয়া যায়। কিন্তু রিলেশনাল ডাটাবেস (MySQL, PostgreSQL, Oracle) ইনডেক্সিংয়ের জন্য **B+ Tree** ডাটা স্ট্রাকচার ব্যবহার করে, কোনো Hash Table ব্যবহার করে না।
        * যেহেতু এটি একটি ট্রি (Tree), তাই রুট নোড থেকে শুরু করে লিফ নোড পর্যন্ত ট্রাভার্স করতে **$O(\log N)$** স্টেপ লাগে।
        * শুধুমাত্র **Hash Index**-এর ক্ষেত্রে সার্চ টাইম কমপ্লেক্সিটি **$O(1)$** হয়, কিন্তু স্ট্যান্ডার্ড ক্লাস্টার্ড ইনডেক্স B+ Tree হওয়ায় তা সবসময় **$O(\log N)$**।
    - **রাইটের ক্ষেত্রে (Write Complexity - Insert/Update/Delete)**:
      - ক্লাস্টার্ড ইনডেক্সের ক্ষেত্রে ডাটা ইনসার্ট করলে ডিস্কে ডাটার ফিজিক্যাল অর্ডার বজায় রাখার জন্য পেজ স্প্লিটিং (Page Splitting) বা ডাটা রিলোকেশন হতে পারে। তাই রাইটের ক্ষেত্রে এর জটিলতাও $O(\log N)$ এবং এটি সাধারণ টেবিল ইনসার্টের চেয়ে কিছুটা ব্যয়বহুল।

---

#### ২. বিশেষ ইনডেক্সসমূহ (Specialized Indexes)

##### ক. Composite Index (কম্পোজিট ইনডেক্স)
যখন কোনো টেবিলে একাধিক কলামের ওপর ভিত্তি করে একটি একক ইনডেক্স তৈরি করা হয়, তাকে কম্পোজিট ইনডেক্স বলে। এটি **Leftmost Prefix Rule** মেনে চলে।

* **Leftmost Prefix Rule**: ধরি আমরা একটি কম্পোজিট ইনডেক্স তৈরি করলাম `(A, B)` কলামের ওপর।
  - এই ইনডেক্সটি কাজ করবে যখন আপনি কুয়েরিতে ফিল্টার করবেন: **শুধু `A`** দিয়ে অথবা **`A` এবং `B` দুটো** দিয়ে।
  - কিন্তু এটি কাজ করবে **না** যদি আপনি শুধু **`B`** দিয়ে ফিল্টার করেন (কারণ ইনডেক্সটি বাম থেকে ডানে তৈরি হয়েছে)।
* **উদাহরণ**:
  - `(first_name, last_name)` ইনডেক্সটি `WHERE first_name = 'Rahim'` কুয়েরি স্পিড-আপ করবে।
  - কিন্তু `WHERE last_name = 'Rahman'` কুয়েরিতে এটি কাজ করবে না।

##### খ. Covering Index (কভারিং ইনডেক্স)
যখন কোনো `SELECT` কুয়েরির প্রয়োজনীয় **সব কলামই** একটি ইনডেক্সের ভেতরেই পাওয়া যায়, তখন সেই ইনডেক্সকে কভারিং ইনডেক্স বলে।

* **কেন এটি দ্রুততম?**
  - ডাটাবেস ইঞ্জিনকে কুয়েরির উত্তর দিতে মূল টেবিলে (Data Table) যেতেই হয় না। সে সরাসরি ইনডেক্সের লিফ নোড থেকেই সব ডেটা নিয়ে রিটার্ন করে। একে **Index-Only Scan** বা **Zero Table Lookup** বলা হয়।
* **উদাহরণ**:
  - আমাদের ইনডেক্স আছে `(email, name)` কলামের ওপর।
  - আমরা কুয়েরি করলাম: `SELECT name FROM users WHERE email = 'test@test.com';`
  - এখানে যেহেতু `email` এবং `name` দুটোই ইনডেক্সে আছে, তাই ডাটাবেস মূল টেবিলে হিট না করেই ফলাফল দিয়ে দিবে।

##### গ. Hash Index (হ্যাশ ইনডেক্স)
হ্যাশ ইনডেক্স হলো একটি বিশেষ ইনডেক্স টাইপ যা হ্যাশ টেবিল (Hash Table) ডাটা স্ট্রাকচার ব্যবহার করে কাজ করে এবং পয়েন্ট লুকআপ বা ইকুইটি (`=`) কুয়েরির জন্য **$O(1)$** টাইম কমপ্লেক্সিটি প্রদান করে।

* 💡 **কনসেপ্ট ক্লিয়ারিং ও ইন্টারভিউ লজিক (Hash Index Deep Dive)**:
  - **প্রশ্ন ১: আমরা কি নিজে থেকে সিলেক্ট বা ডিক্লেয়ার করে Hash Index তৈরি করতে পারি?**
    - **PostgreSQL**: **হ্যাঁ, পারি।** পোস্টগ্রিসে সরাসরি আমরা ডিক্লেয়ার করে হ্যাশ ইনডেক্স তৈরি করতে পারি:
      ```sql
      CREATE INDEX index_name ON table_name USING hash (column_name);
      ```
    - **MySQL (InnoDB Engine)**: **না, সরাসরি পারি না।** আপনি যদি InnoDB টেবিলে `CREATE INDEX ... USING HASH` লিখেনও, ডাটাবেস ইঞ্জিন তা সাইলেন্টলি ইগনোর করে একটি সাধারণ B-Tree ইনডেক্স তৈরি করবে। তবে InnoDB ব্যাকগ্রাউন্ডে অটোমেটিক **Adaptive Hash Index (AHI)** তৈরি করে কাজ সম্পন্ন করে।
    - **MySQL (MEMORY Engine)**: **হ্যাঁ, পারি।** মেমরি ইঞ্জিনে হ্যাশ ইনডেক্স তৈরি করা যায়:
      ```sql
      CREATE TABLE users (
          id INT,
          name VARCHAR(50),
          INDEX (id) USING HASH
      ) ENGINE = MEMORY;
      ```

  - **প্রশ্ন ২: Hash Index কি Primary Key বা Clustered Index হিসেবে কাজ করতে পারে?**
    - **না, কখনই না।** হ্যাশ ইনডেক্স কখনোই ক্লাস্টার্ড ইনডেক্স (Clustered Index) হতে পারে না।
    - **কারণ**: ক্লাস্টার্ড ইনডেক্স ডিস্কের উপর ডেটার **ভৌত সাজসজ্জা বা সর্টিং অর্ডার (Physical Sorting/Order)** নির্ধারণ করে। কিন্তু হ্যাশ ইনডেক্স হ্যাশ ফাংশনের মাধ্যমে মেমরি অ্যাড্রেস বরাদ্দ করে যা সম্পূর্ণ র‍্যান্ডম এবং এলোমেলো (যেমন: ১ এর হ্যাশ হতে পারে ৯৮, ২ এর হ্যাশ হতে পারে ১৪)। যেহেতু এখানে কোনো সর্টিং বা ক্রম নির্ধারণের সুযোগ থাকে না, তাই একে ক্লাস্টার্ড ইনডেক্স বানানো অসম্ভব।
    - এটি সবসময় **Non-Clustered (Secondary) Index** হিসেবে কাজ করে।

---

## 5. Normalization & Denormalization

### Normalization
The process of structuring a relational database to minimize data redundancy and prevent insertion, update, and deletion anomalies.

```
       [ Unnormalized Data ]
                 │
                 ▼  1NF: Remove repeating groups & ensure Atomic values
          [ 1st Normal Form ]
                 │
                 ▼  2NF: Remove Partial Dependencies (Must depend on entire PK)
          [ 2nd Normal Form ]
                 │
                 ▼  3NF: Remove Transitive Dependencies (Non-key -> Non-key)
          [ 3rd Normal Form ]
                 │
                 ▼  BCNF: Strict 3NF (For every X -> Y, X must be a Super Key)
        [ Boyce-Codd Normal Form ]
```

#### Normal Forms Explained:
1. **1NF (First Normal Form):**
   * Each cell contains atomic (indivisible) values.
   * No repeating groups or arrays stored in a single column.
2. **2NF (Second Normal Form):**
   * Must be in 1NF.
   * Eliminates **Partial Dependency** (No non-prime attribute should depend on a subset of any candidate key).
3. **3NF (Third Normal Form):**
   * Must be in 2NF.
   * Eliminates **Transitive Dependency** (Non-prime attributes must not depend on other non-prime attributes; $A \rightarrow B$ and $B \rightarrow C$).
4. **BCNF (Boyce-Codd Normal Form):**
   * Advanced version of 3NF. For any functional dependency $X \rightarrow Y$, $X$ must be a Super Key.

### Denormalization
* **Definition:** Intentionally introducing redundancy into a database by combining tables to reduce costly `JOIN` operations.
* **Trade-off:** Faster Read Queries vs Slower Writes & Higher Risk of Data Inconsistency.
* **Common Scenario:** Read-heavy analytics (OLAP) systems and data warehouses.

---

## 6. SQL Query Execution Order

When a database engine processes a SQL query, it does NOT execute clauses in the written syntactic order. Understanding execution order is critical for query optimization and debugging.

```
Syntactic Writing Order           Logical Execution Order
-----------------------           -----------------------
1. SELECT                         1. FROM & JOINs
2. FROM                           2. WHERE
3. JOIN                           3. GROUP BY
4. WHERE                          4. HAVING
5. GROUP BY                       5. SELECT
6. HAVING                         6. DISTINCT
7. ORDER BY                       7. ORDER BY
8. LIMIT / OFFSET                 8. LIMIT / OFFSET
```

### Detailed Step-by-Step Flow:
1. **`FROM` & `JOIN`**: Identifies base tables, builds Cartesian products, and applies `ON` join predicates.
2. **`WHERE`**: Filters individual rows *before* grouping. (Note: Aggregate functions like `SUM()`, `COUNT()` cannot be used here).
3. **`GROUP BY`**: Groups the filtered rows into summary categories.
4. **`HAVING`**: Filters groups *after* aggregation.
5. **`SELECT`**: Computes expressions, aliases, and selects specific columns.
6. **`DISTINCT`**: Removes duplicate rows from the final projection.
7. **`ORDER BY`**: Sorts output rows (Can use column aliases created in `SELECT`).
8. **`LIMIT / OFFSET`**: Restricts the number of returned rows.

---

## 7. SQL Joins & Execution Strategies

Joins combine records from two or more tables based on a related column.

```
INNER JOIN             LEFT JOIN            RIGHT JOIN            FULL OUTER JOIN
┌───┬───┐              ┌───┬───┐            ┌───┬───┐             ┌───┬───┐
│ A │ B │              │ A │ B │            │ A │ B │             │ A │ B │
│  ███  │              │██████ │            │  █████│             │███████│
└───┴───┘              └───┴───┘            └───┴───┘             └───┴───┘
Matching only        All Left + Match     All Right + Match     All records from both
```

### Types of SQL Joins
* **`INNER JOIN`**: Returns rows when there is a match in both tables.
* **`LEFT (OUTER) JOIN`**: Returns all rows from the left table, and matched rows from the right table (`NULL` if no match).
* **`RIGHT (OUTER) JOIN`**: Returns all rows from the right table, and matched rows from the left table.
* **`FULL (OUTER) JOIN`**: Returns records when there is a match in either left or right table.
* **`CROSS JOIN`**: Produces Cartesian product of two tables ($N \times M$ rows).
* **`SELF JOIN`**: A table joined with itself (e.g., Employee table referencing Manager ID).

```sql
-- Self Join Example (Find Employee & Manager Name)
SELECT 
    e.name AS Employee, 
    m.name AS Manager
FROM Employees e
LEFT JOIN Employees m ON e.manager_id = m.emp_id;
```

---

## 8. SQL Top Problem Solving

### Problem 1: Find 2nd Highest / Nth Highest Salary

#### Approach A: Using Window Function (`DENSE_RANK()`) - Recommended & Standard
```sql
WITH RankedSalaries AS (
    SELECT 
        emp_id, 
        name, 
        salary,
        DENSE_RANK() OVER (ORDER BY salary DESC) as rnk
    FROM Employees
)
SELECT salary 
FROM RankedSalaries 
WHERE rnk = 2; -- Change N here
```

#### Approach B: Using Subquery & `MAX()` (Specific to 2nd Highest)
```sql
SELECT MAX(salary) AS SecondHighestSalary
FROM Employees
WHERE salary < (SELECT MAX(salary) FROM Employees);
```

#### Approach C: Using `LIMIT` and `OFFSET` (MySQL/Postgres)
```sql
SELECT DISTINCT salary 
FROM Employees 
ORDER BY salary DESC 
LIMIT 1 OFFSET 1; -- OFFSET N-1
```

---

### Problem 2: Delete Duplicate Rows Keeping Only Lowest ID

```sql
DELETE e1 FROM Employees e1
INNER JOIN Employees e2 
ON e1.email = e2.email AND e1.id > e2.id;
```

---

## 9. Transactions, ACID Properties, Locks, Views & Triggers

### A. ACID Properties
* **Atomicity:** "All or Nothing". Executed via WAL (Write-Ahead Logging) and undo logs.
* **Consistency:** Preserves database invariants before and after transactions.
* **Isolation:** Controls visibility of concurrent transactions.
* **Durability:** Ensures committed data survives system crashes via redo logs.

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

## 11. ER Diagrams & Relationship Modeling

### A. Components of Entity-Relationship (ER) Diagram
1. **Entity:** Real-world object (e.g., `Student`, `Course`). Represented by a **Rectangle**.
   * **Weak Entity:** Depends on a Strong Entity for identification. Represented by a **Double Rectangle**.
2. **Attribute:** Property of an entity. Represented by an **Ellipse**.
   * **Key Attribute:** Underlined text inside ellipse (Primary Key).
   * **Composite Attribute:** Divided into sub-attributes (e.g., `Name` -> `FirstName`, `LastName`).
   * **Multi-valued Attribute:** Can hold multiple values (e.g., `PhoneNumbers`). Represented by a **Double Ellipse**.
   * **Derived Attribute:** Computed from other attributes (e.g., `Age` derived from `DOB`). Represented by a **Dashed Ellipse**.
3. **Relationship:** Connection between entities. Represented by a **Diamond**.

### B. Cardinality Ratios
* **1:1 (One-to-One):** One User has One User Profile.
* **1:N (One-to-Many):** One Department has Many Employees.
* **N:M (Many-to-Many):** Many Students enroll in Many Courses (Requires Junction/Junction table in RDBMS).

---

## 12. Distributed DBMS: Sharding, Connection Pool & ORM

### A. Database Sharding (Horizontal Partitioning)
Distributes table rows across multiple physical database instances (shards).
* **Hash-Based Sharding:** `shard_id = hash(user_id) % num_shards`
* **Range-Based Sharding:** Shard 1 (User ID 1-100k), Shard 2 (User ID 100k-200k).
* **Consistent Hashing:** Minimizes remapping when adding or removing database nodes.

---

### B. Connection Pooling
Opening a new TCP database connection is expensive (Handshake, Authentication, Resource Allocation).
* **Mechanism:** A connection pool pre-allocates a fixed number of DB connections and keeps them warm in memory.
* **Flow:** Application threads borrow an active connection from pool $\rightarrow$ execute query $\rightarrow$ return connection back to pool.
* **Popular Tools:** HikariCP (Java), PGPool-II, PgBouncer.

---

### C. ORM (Object-Relational Mapping)
Provides an abstraction layer mapping OOP objects to database tables (e.g., Hibernate, Entity Framework, Prisma).
* **Pros:** Rapid development, type safety, DB vendor independence.
* **Cons:** Overhead, lack of fine-grained query control, risk of inefficient SQL generation.

---

## 13. N+1 Query Problem & Solutions

### What is the N+1 Query Problem?
An ORM performance bug where an application executes 1 initial query to fetch $N$ parent records, and then issues $N$ individual subsequent queries to fetch child details for each record (Total Queries = $1 + N$).

### Example Scenario:
Fetching 100 Authors and their Books using Lazy Loading:
1. `SELECT * FROM Authors;` (Returns 100 rows) $\leftarrow$ **1 Query**
2. For each Author (100 times):
   * `SELECT * FROM Books WHERE author_id = ?;` $\leftarrow$ **100 Queries**
* **Total Queries Executed:** $1 + 100 = 101$ queries (Destroys DB performance).

### Solutions:
1. **Eager Loading / Join Fetch:** Instruct the ORM to fetch parents and children in a single SQL query using an `INNER JOIN` or `LEFT JOIN`.
   ```sql
   -- Solution Query (Single SQL Execution)
   SELECT a.*, b.* 
   FROM Authors a 
   LEFT JOIN Books b ON a.id = b.author_id;
   ```
2. **Batch Fetching:** Fetch child records in batches using `WHERE author_id IN (1, 2, 3, ..., 20)`.

---

## 14. CAP & PACELC Theorems

### CAP Theorem
In any distributed data store, you can only simultaneously provide **2 of 3** guarantees during a network partition:

```
        Consistency (C)  ──  Every read receives the most recent write.
        Availability (A) ──  Every request receives a non-error response.
        Partition Tolerance (P) ── System functions despite network dropouts.
```

* **CP Databases (Consistency + Partition Tolerance):** MongoDB, HBase, Redis. (Rejects requests if consistency cannot be guaranteed).
* **AP Databases (Availability + Partition Tolerance):** Apache Cassandra, DynamoDB, CouchDB. (Returns stale data rather than failing).

### PACELC Theorem
An extension of CAP that accounts for normal operation state (when no network partition exists):
* **P/A** vs **C** (If **P**artition: choose **A**vailability vs **C**onsistency)
* **E/L** vs **C** (**E**lse: choose **L**atency vs **C**onsistency)

---

## 15. When to Use SQL vs NoSQL

```
                    Decision Matrix
                          │
         Does your data have a strict relational
         structure & require ACID compliance?
                         / \
                       YES  NO
                       /     \
                Use SQL       Is horizontal write scale
             (Postgres, MySQL) or schema flexibility needed?
                                / \
                              YES  NO
                              /     \
                       Use NoSQL   Evaluate Caching / KV
                     (Mongo, Cass)   (Redis, Memcached)
```

---

## 16. SQL Injection (SQLi) & Security

### What is SQL Injection?
An attack vector where malicious SQL statements are inserted into user input fields to execute unauthorized DB commands.

### Vulnerable Code (String Concatenation):
```python
# DANGEROUS CODE
user_input = "admin' OR '1'='1"
query = "SELECT * FROM Users WHERE username = '" + user_input + "' AND password = '" + pass_input + "'"
# Executes: SELECT * FROM Users WHERE username = 'admin' OR '1'='1' ... (Bypasses Auth!)
```

### Prevention (Parameterized Queries / Prepared Statements):
```python
# SECURE CODE
cursor.execute("SELECT * FROM Users WHERE username = %s AND password = %s", (user_input, pass_input))
```

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
