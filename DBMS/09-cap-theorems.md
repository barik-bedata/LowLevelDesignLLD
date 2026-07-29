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

