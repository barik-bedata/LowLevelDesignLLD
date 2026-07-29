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

