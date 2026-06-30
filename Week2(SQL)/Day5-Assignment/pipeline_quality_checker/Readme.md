# E-Commerce Data Quality Pipeline

## Overview
Data quality validation pipeline for e-commerce sales data. Loads CSV files into PostgreSQL and runs 4 automated checks to identify data issues before analysis.

## Pipeline Flow

```
create_tables.py → [6 tables created] → insert_data.py [data inserted into tables] → run_pipeline.py → Quality Checks
                                           ↓
                    [check_duplicates, check_null, check_referential_integrity, check_freshness]
```

## How to Run

```bash
# 1. Create tables
python3 create_tables.py

# 2. Insert raw data
python3 insert_data.py

# 3. Run quality checks
python3 run_pipeline.py
```

## Tables Loaded
- `inventory` (9,271 rows) - From Sale Report.csv
- `product_pricing` (2,660 rows) - From May-2022.csv + P L March 2021.csv
- `amazon_sales` (128,975 rows) - From Amazon Sale Report.csv
- `international_sales` (37,432 rows) - From International sale Report.csv
- `warehouse_comparison` (50 rows)
- `expenses` (17 rows)

## Quality Checks (run_pipeline.py)

### 1. **Duplicates** (`check_duplicates.py`)
- Counts duplicate rows per table by key columns
- Detects if pipeline ran twice

### 2. **Nulls** (`check_null.py`)
- Reports NULL count & percentage per column per table
- Identifies missing data

### 3. **Referential Integrity** (`check_refrential_integrity.py`)
- Finds orphaned SKUs in child tables (not in inventory)
- SKU mismatch detection

### 4. **Freshness** (`check_freshness.py`)
- Shows oldest & newest `inserted_at` timestamp per table
- Confirms data recency

## Key Features
- No constraints during insert (allows dirty data)
- `inserted_at` timestamp on all rows (audit trail)
- All data types as TEXT (flexible cleaning)
- NULL handling: values = tuple(None if pd.isna(v) else v for v in row) converts pandas NaN → SQL NULL

## Output
Each check prints results to console. Example:
```
========================Check Duplicates=========================
            table_name  duplicates
0         Amazon Sales           0
1         Amazon Sales           0
2      Product Pricing        1330
3            Inventory           6
4  International Sales       11641
5         Amazon Sales        6846
....