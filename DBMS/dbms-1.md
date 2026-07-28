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

Cascading constraints define what happens to child table records when a referenced parent key is updated or deleted.

### Foreign Key Actions (`ON DELETE` / `ON UPDATE`)

1. **`ON DELETE CASCADE`**: Automatically deletes child rows when the referenced parent row is deleted.
   * *Use Case:* Deleting a `User` automatically deletes all their `Posts` and `Comments`.
2. **`ON DELETE SET NULL`**: Sets the foreign key column in child rows to `NULL` when parent is deleted.
   * *Use Case:* Deleting a `Department` sets `department_id` to `NULL` for attached `Employees`.
3. **`ON DELETE SET DEFAULT`**: Sets child foreign key to its defined default value.
4. **`ON DELETE RESTRICT` / `NO ACTION`**: Prevents parent row deletion if any child rows reference it (Throws Foreign Key Constraint Error).

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

---

## 4. Keys & Indexing Deep Dive

### A. Database Keys Overview
* **Super Key:** Any set of attributes that uniquely identifies a row in a table.
* **Candidate Key:** A minimal Super Key with no redundant attributes.
* **Primary Key (PK):** A selected Candidate Key that uniquely identifies each row. Must be `NOT NULL` and `UNIQUE`.
* **Alternate Key:** Candidate Keys that were not chosen as the Primary Key.
* **Foreign Key (FK):** A field in one table that references the Primary Key of another table, establishing referential integrity.
* **Composite Key:** A Primary Key composed of two or more columns (e.g., `student_id` + `course_id`).
* **Surrogate Key:** An artificially generated unique key (e.g., UUID or Auto-increment ID) without business meaning.

---

### B. Indexing Mechanics & Architecture

Indexes are specialized data structures that speed up data retrieval queries at the cost of additional storage and slower write operations (`INSERT`, `UPDATE`, `DELETE`).

```
                    B+ Tree Index Structure
                           [ 50 ]
                         /        \
                    [20, 35]     [65, 85]
                    /   |   \    /   |   \
                  Leaves with pointers to actual Data Rows
```

#### 1. Clustered Index vs Non-Clustered Index

| Feature | Clustered Index | Non-Clustered Index |
| :--- | :--- | :--- |
| **Physical Storage** | Dictates physical order of data rows on disk | Separate structure storing key + row pointer |
| **Quantity per Table** | **Exactly 1** per table (Usually Primary Key) | **Multiple** (Up to 999 in SQL Server, 64 in MySQL) |
| **Leaf Node Content** | Contains the **actual data rows** | Contains index key + pointer (RID/PK) to data row |
| **Speed** | Faster for range searches (`BETWEEN`, `>`, `<`) | Slightly slower due to secondary lookup (Bookmark Lookup) |

#### 2. Specialized Indexes
* **Composite Index:** An index created on multiple columns `(col1, col2)`. Follows the **Leftmost Prefix Rule** (An index on `(A, B)` will serve queries filtering by `A` or `A, B`, but NOT `B` alone).
* **Covering Index:** An index that contains all columns requested by a `SELECT` query. The DB engine can fulfill the query entirely from the index leaf nodes without touching the main data table (Zero Table Lookup).

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
