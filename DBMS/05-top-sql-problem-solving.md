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

