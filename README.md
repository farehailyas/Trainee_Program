## Trainee Program | Week 2 Progress Report

---

## Overview
SQL fundamentals practiced through hands-on queries against real e-commerce dataset. Every topic below has corresponding SQL queries written, tested, and documented.

---

## Topics Covered

### PostgreSQL & Schema Design
- Database setup on PostgreSQL (local + Supabase)
- 6 tables created with proper DDL (CREATE TABLE, ALTER, DROP)
- Data types: VARCHAR, INTEGER, FLOAT, TEXT, TIMESTAMP, BOOLEAN
- Primary keys, composite keys, constraints (NOT NULL, UNIQUE)
- No FK constraints during raw insert (quality checks added later)
- ERD designed on dbdiagram.io

### Core Querying
- SELECT, WHERE, ORDER BY, LIMIT, OFFSET, DISTINCT
- Aliases, WHERE vs HAVING distinction
- Aggregations: COUNT, SUM, AVG, MIN, MAX
- GROUP BY with HAVING (post-grouping filter)
- 5 real business queries written answering dataset questions

### Subqueries & CTEs
- Subqueries in WHERE, FROM, SELECT clauses
- Correlated vs non-correlated subqueries
- CTEs (WITH clause) for readability over nested subqueries
- Practical: Orphan detection via subqueries + CTEs
- Issue identified: NOT IN breaks with NULL → used EXCEPT/LEFT JOIN instead

### JOINs & Set Operations
- INNER, LEFT, RIGHT, FULL OUTER, CROSS, SELF JOINs
- UNION, UNION ALL, INTERSECT, EXCEPT
- Referential integrity checks (orphaned SKUs in child tables)
- Tested: LEFT JOIN returns unmatched rows; INNER JOIN excludes them
- Example: Found 45 orphaned SKUs in product_pricing (not in inventory)

### Data Quality Pipeline
- Built 4-check quality validation pipeline:
  - Duplicates detection (GROUP BY + COUNT)
  - NULL audit per column (COUNT FILTER WHERE IS NULL)
  - Referential integrity (orphan detection)
  - Freshness check (MIN/MAX inserted_at)
- Inserted 178,747 rows across 6 tables (no constraints, all data kept)


## Additional
- SQL Murder Mystery challenge : https://mystery.knightlab.com/

---

**Done when:** Quality checks run seamlessly, 4-table JOIN queries written, GitHub repo populated with all SQL files.
