# WellDev DBMS & SQL Interview Q&A

This document compiles all DBMS, SQL, and database-related interview questions asked in various rounds of the WellDev recruitment process, along with structured, comprehensive answers.

---

## Table of Contents
1. [SQL Queries & Practical Scenarios](#1-sql-queries--practical-scenarios)
2. [DBMS Concepts & Database Design](#2-dbms-concepts--database-design)
3. [Concurrency, System Design & Security](#3-concurrency-system-design--security)

---

## 1. SQL Queries & Practical Scenarios

### Q1. Explain the order of SQL query execution.
Although written in a specific syntax order, a relational database engine executes SQL clauses in a logical sequence to optimize query performance and filter data correctly.

**Syntax Order (How you write it):**
```sql
SELECT DISTINCT column_name
FROM table_name
JOIN join_table ON join_condition
WHERE filter_condition
GROUP BY group_columns
HAVING group_filter
ORDER BY sort_column
LIMIT count;
```

**Logical Execution Order (How the database runs it):**
1. **`FROM` & `JOIN`**: The database determines which tables are being queried and sets up the initial workspace. Joins are evaluated here first.
2. **`ON`**: Applies join-specific filters.
3. **`WHERE`**: Filters individual rows based on non-aggregate conditions.
4. **`GROUP BY`**: Groups the remaining rows into buckets based on specified columns.
5. **`HAVING`**: Filters groups using aggregate functions (e.g., `SUM()`, `AVG()`, `COUNT()`).
6. **`SELECT`**: Extracts the columns, computes expressions, and assigns aliases.
7. **`DISTINCT`**: Discards duplicate rows from the projected output.
8. **`ORDER BY`**: Sorts the resulting rows based on the specified columns or expressions.
9. **`LIMIT` / `OFFSET`**: Restricts the returned records to a specific window (essential for pagination).

---

### Q2. Write a SQL query to show all the duplicate rows in a table.
Suppose we have a table `users` and we want to find duplicate records based on the `email` column.

**Method 1: Find duplicates with count**
```sql
SELECT email, COUNT(*) as occurrence_count
FROM users
GROUP BY email
HAVING COUNT(*) > 1;
```

**Method 2: Display the full rows of duplicate entries**
```sql
SELECT * 
FROM users 
WHERE email IN (
    SELECT email 
    FROM users 
    GROUP BY email 
    HAVING COUNT(*) > 1
)
ORDER BY email;
```

---

### Q3. Given a table with `product_id`, `price`, and `product_name`, write a query to find products with the same price.
To find products that share a price, we can perform a self-join to match product entries with identical prices but different identifiers.

**Query (Self-Join):**
```sql
SELECT p1.product_id, p1.product_name, p1.price
FROM products p1
INNER JOIN products p2 
  ON p1.price = p2.price 
  AND p1.product_id <> p2.product_id
ORDER BY p1.price;
```

**Alternative (Grouped view of duplicate prices):**
```sql
SELECT price, GROUP_CONCAT(product_name ORDER BY product_name SEPARATOR ', ') AS products
FROM products
GROUP BY price
HAVING COUNT(*) > 1;
```

---

### Q4. What is the difference between `DELETE`, `TRUNCATE`, and `DROP` in SQL?

| Feature | `DELETE` | `TRUNCATE` | `DROP` |
| :--- | :--- | :--- | :--- |
| **Command Category** | DML (Data Manipulation Language) | DDL (Data Definition Language) | DDL (Data Definition Language) |
| **Action** | Deletes specific or all rows. | Deletes all rows by deallocating pages. | Completely deletes table schema & data. |
| **`WHERE` Clause** | Supported (allows partial deletion). | Not supported. | Not supported. |
| **Speed** | Slow (deletes row-by-row and logs each). | Very Fast (deletes data pages directly). | Immediate (removes table metadata). |
| **Triggers** | Fires active `DELETE` triggers. | Does not fire triggers. | Does not fire triggers. |
| **Rollback** | Can be rolled back inside a transaction. | Can be rolled back in some DBs (PG, SQL Server), not in MySQL. | Cannot be rolled back (except in transactional DDL). |
| **Index Resets** | Keeps auto-increment values. | Resets auto-increment to initial value. | Removes table structure and index definitions completely. |

---

### Q5. Write SQL query to find a unique column of a database (Metadata query vs. Value Check).

**Scenario A: Find columns defined with UNIQUE or PRIMARY KEY constraints**
You can query the database metadata catalog. For instance, in **MySQL**:
```sql
SELECT TABLE_NAME, COLUMN_NAME, CONSTRAINT_NAME
FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
WHERE CONSTRAINT_SCHEMA = 'your_database_name'
  AND (CONSTRAINT_NAME = 'PRIMARY' OR CONSTRAINT_NAME LIKE '%unique%');
```

**Scenario B: Test if a specific column's current data is unique**
You check if the count of distinct values equals the total count of rows:
```sql
SELECT CASE 
    WHEN COUNT(DISTINCT column_name) = COUNT(*) THEN 'Column is Unique'
    ELSE 'Column has Duplicates'
END AS uniqueness_status
FROM table_name;
```

---

### Q6. Write SQL query to find the second highest salary.
Suppose we have a table `employee` with a column `salary`.

**Method 1: Using a Subquery (Compatible with most RDBMS)**
```sql
SELECT MAX(salary) AS second_highest_salary
FROM employee
WHERE salary < (SELECT MAX(salary) FROM employee);
```

**Method 2: Using `LIMIT` and `OFFSET` (MySQL / PostgreSQL)**
```sql
SELECT DISTINCT salary 
FROM employee
ORDER BY salary DESC
LIMIT 1 OFFSET 1;
```

**Method 3: Using Window Functions (SQL Server / Oracle / PostgreSQL / MySQL 8.0+)**
```sql
WITH SalaryRankings AS (
    SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) as rnk
    FROM employee
)
SELECT DISTINCT salary 
FROM SalaryRankings 
WHERE rnk = 2;
```

---

### Q7. Write SQL query to sort salary in descending order.
```sql
SELECT salary 
FROM employee 
ORDER BY salary DESC;
```

---

### Q8. Difference between Left Outer Join and Right Outer Join?
Both are types of Outer Joins used to combine records from two tables based on a condition:

- **`LEFT OUTER JOIN` (or `LEFT JOIN`)**:
  - Returns **all** rows from the left (first-named) table, along with matched rows from the right table.
  - If a row in the left table doesn't have a matching row in the right table, columns from the right table are populated with `NULL`.
- **`RIGHT OUTER JOIN` (or `RIGHT JOIN`)**:
  - Returns **all** rows from the right (second-named) table, along with matched rows from the left table.
  - If a row in the right table has no matching row in the left table, columns from the left table are populated with `NULL`.

> **Note:** `A LEFT JOIN B` yields the exact same query result as `B RIGHT JOIN A` (though the column order in the result set matches the select sequence).

---

## 2. DBMS Concepts & Database Design

### Q9. What are the ACID properties in DBMS?
ACID represents the core properties that guarantee database transactions are processed reliably:

* **Atomicity ("All or Nothing")**: Guarantees that all operations within a transaction are completed successfully; if any operation fails, the entire transaction is aborted and rolled back, leaving the database state unchanged.
* **Consistency**: Ensures a transaction can only transition the database from one valid state to another, maintaining database constraints, rules, and triggers.
* **Isolation**: Guarantees that concurrent execution of transactions leaves the database in the same state as if they were executed sequentially. Intermediate transaction states are invisible to other transactions.
* **Durability**: Guarantees that once a transaction commits, its changes are permanently written to non-volatile storage (disk) and will survive subsequent power losses or system crashes.

---

### Q10. What is a trigger in DBMS, and what does cascading mean?
* **Trigger**: A named database object containing procedural code that is automatically executed (fired) in response to a specific event (such as `INSERT`, `UPDATE`, or `DELETE`) on a particular table. Triggers are typically used to enforce complex business rules, generate audit logs, or compute values automatically.
* **Cascading**: A configuration rule established on foreign keys that automatically propagates data updates or deletions from a parent record to child records in related tables.
  - `ON DELETE CASCADE`: If a parent row is deleted, all referenced child rows are automatically deleted.
  - `ON UPDATE CASCADE`: If a parent key changes (e.g., ID updates), all referenced child keys are automatically updated.

---

### Q11. What is the difference between SQL and NoSQL?

| Feature | SQL Databases (Relational) | NoSQL Databases (Non-Relational) |
| :--- | :--- | :--- |
| **Data Model** | Table-based (Rows and columns with strict relationships). | Key-value pairs, document collections, wide-column stores, or graphs. |
| **Schema** | Static, predefined schema must be designed beforehand. | Dynamic schema allows storing unstructured or semi-structured data. |
| **Scalability** | Vertically scalable (scale by improving CPU/RAM on one machine). | Horizontally scalable (scale by adding more servers to distribute load). |
| **Transactions** | Strict compliance with ACID properties. | Prioritizes scalability and performance (BASE properties, eventual consistency). |
| **Use Case** | Complex joins, transactional systems (e.g., banking, ERP). | Real-time analytics, user profiles, big data, caching, catalogs. |

---

### Q12. For storing values from cache memory to RAM, should we use SQL or NoSQL?
**NoSQL** is typically selected for this task:
* **Caching is optimized for high-speed, key-value lookup** (e.g., storing serialized objects, user sessions, or cached API responses by key).
* Databases like **Redis** or **Memcached** are designed specifically to run entirely in RAM as NoSQL stores, providing sub-millisecond read/write latency.
* Fixed tables and the query parser overhead of relational SQL systems are unnecessary and degrade performance when managing volatile caching layers.

---

### Q13. How do you check for changes in a database?
There are several techniques to detect database updates depending on system requirements:
1. **CDC (Change Data Capture)**: Tools (e.g., Debezium) read database transaction logs (like binlog in MySQL) to capture and publish changes to event streaming platforms (like Kafka) in real-time.
2. **Database Triggers**: Configuring an `AFTER UPDATE` or `AFTER INSERT` trigger to write change logs into an audit table.
3. **Audit Columns**: Creating columns like `updated_at` (timestamp) and filtering queries by querying records updated since the last check.
4. **Row Versioning**: Storing an auto-incrementing version or hash for rows and comparing values.

---

### Q14. Explain ER Diagram in Relational Database.
An **Entity-Relationship (ER) Diagram** is a visual blueprint that maps out the structure of a database by illustrating relationships between data items.
* **Entities**: Objects or concepts that store data (e.g., *Customer*, *Order*), represented as rectangles.
* **Attributes**: Properties of entities (e.g., *customer_email*, *order_date*), represented as ovals.
* **Relationships**: How entities associate with one another (e.g., *Customer "places" Order*), represented as diamonds.
* **Cardinality**: Shows the numerical constraint of relationships (e.g., One-to-One `1:1`, One-to-Many `1:N`, Many-to-Many `M:N`).

---

### Q15. Describe database normalization.
Normalization is the database design technique of organizing table columns and relationships to minimize **redundancy** and prevent **anomalies** (insertion, update, and deletion anomalies) while keeping data consistent.

**Normal Forms (NF):**
* **1st Normal Form (1NF)**: All column values must be atomic (no arrays/comma-separated lists), and each table must have a unique identifier (Primary Key).
* **2nd Normal Form (2NF)**: Must be in 1NF, and all non-key columns must fully depend on the primary key (no partial dependencies on composite keys).
* **3rd Normal Form (3NF)**: Must be in 2NF, and no non-key column can depend transitively on another non-key column (no transitive dependencies).
* **Boyce-Codd Normal Form (BCNF)**: A stricter variant of 3NF where for every non-trivial functional dependency $X \rightarrow Y$, $X$ must be a super key.

---

## 3. Concurrency, System Design & Security

### Q16. What happens if two people try to reserve the same ticket simultaneously in a ticket reservation system? How would you solve this problem?
This is a classic **race condition** where simultaneous requests read the seat status as "Available", and both attempt to write "Reserved", causing double-booking.

**Solutions:**
1. **Pessimistic Locking**: 
   - Lock the row during the read step so other transactions must wait until it's finished.
   - SQL: `SELECT * FROM seats WHERE seat_id = 42 FOR UPDATE;`
2. **Optimistic Locking**:
   - Add a `version` column to the table. Update only if the version hasn't changed.
   - SQL: `UPDATE seats SET status = 'reserved', version = version + 1 WHERE seat_id = 42 AND version = current_version;`
   - If the update returns 0 affected rows, the transaction is rejected, prompting the second user to refresh or choose another seat.
3. **Distributed Locks (Redis/Redlock)**:
   - Acquire a distributed lock for `seat_42` for a duration of 10 seconds. Process the reservation in the DB, then release the lock.
4. **Message Queuing**:
   - Route seat reservation requests to a single-threaded queue (e.g., RabbitMQ, SQS, Kafka topic partition) to process them sequentially.

---

### Q17. How many APIs are required to solve the ticket reservation problem?
Typically, a microservice or modular application needs **3 to 5 key APIs**:

1. **`GET /events/{id}/seats`**: Fetches the interactive layout of seats showing current status (Available, Locked, Reserved).
2. **`POST /bookings/hold`**: Creates a temporary hold (e.g., 5-10 minutes) on specific seat IDs. (Essential to prevent lock starvation while checking out).
3. **`POST /bookings/{booking_id}/checkout`**: Initiates the payment process.
4. **`POST /bookings/{booking_id}/confirm`**: Confirms the booking post-payment success and marks the database status as permanently reserved.
5. **`DELETE /bookings/{booking_id}/release`**: Releases the hold if checkout fails or the timeout is reached.
6. **`GET /health`**: Standard API to check system status.

---

### Q18. If we need to display a large amount of data on a website, what technique should be followed? (Pagination)
To render massive datasets efficiently, use **Pagination** to load records in chunks.

1. **Offset-Based Pagination**:
   - SQL: `SELECT * FROM items ORDER BY id LIMIT 10 OFFSET 50;`
   - **Pros**: Easy to implement; supports direct jumping to page *N*.
   - **Cons**: Extremely slow for deep pages (e.g., `OFFSET 100000` scans and discards 100k records); inconsistent results if items are inserted/deleted during browsing.
2. **Cursor-Based (Keyset) Pagination**:
   - SQL: `SELECT * FROM items WHERE id > last_seen_id ORDER BY id LIMIT 10;`
   - **Pros**: Highly efficient (always executes an index scan); stable under concurrent insertions/deletions.
   - **Cons**: Cannot skip pages directly (must navigate page-by-page).

---

### Q19. How can passwords be secured so that no one (even the administrator) can view them? How can password hashing be strengthened?
Passwords must **never** be stored in plain text or using fast reversible encryption.

**Security Strategies:**
1. **Cryptographic Hashing**: Apply one-way cryptographic algorithms like **Argon2**, **bcrypt**, or **PBKDF2**. Do not use fast hashes like MD5 or SHA-256 (vulnerable to GPU-based brute-force search).
2. **Salting**:
   - Append a unique, cryptographically secure random string (the *salt*) to the password before hashing it.
   - Prevents **Rainbow Table attacks** (precomputed hash lookups) and ensures identical user passwords produce different hashes.
3. **Peppering**:
   - Apply a secret key (the *pepper*) to the password before hashing.
   - Keep the pepper secure in an external key management service or environment variable—**never** in the database. If the DB is compromised but the app server is secure, the hashes remain protected.
4. **Work Factor Adjustments**: Increase the cost iterations parameter of bcrypt/Argon2 over time to keep pace with improvements in computing power.
