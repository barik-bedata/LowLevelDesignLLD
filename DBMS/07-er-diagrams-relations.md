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

