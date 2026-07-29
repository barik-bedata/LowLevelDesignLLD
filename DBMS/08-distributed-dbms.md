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

