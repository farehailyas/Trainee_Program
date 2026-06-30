import duckdb
import pandas as pd

conn = duckdb.connect('superstore.db')

# Read CSV
df = pd.read_csv('Sample - Superstore.csv', encoding='latin1')

# Create tables from single CSV
conn.execute("""
    CREATE TABLE IF NOT EXISTS customers AS 
    SELECT DISTINCT 
        "Customer ID" as customer_id,
        "Customer Name" as customer_name,
        "Segment" as segment
    FROM (SELECT * FROM df)
""")

conn.execute("""
    CREATE TABLE IF NOT EXISTS products AS 
    SELECT DISTINCT 
        "Product ID" as product_id,
        "Product Name" as product_name,
        "Category" as category,
        "Sub-Category" as sub_category
    FROM (SELECT * FROM df)
""")

conn.execute("""
    CREATE TABLE IF NOT EXISTS orders AS 
    SELECT DISTINCT 
        "Order ID" as order_id,
        "Order Date" as order_date,
        "Ship Date" as ship_date,
        "Ship Mode" as ship_mode,
        "Region" as region,
        "State" as state,
        "City" as city,
        "Country" as country,
        "Customer ID" as customer_id
    FROM (SELECT * FROM df)
""")

conn.execute("""
    CREATE TABLE IF NOT EXISTS sales AS 
    SELECT 
        "Order ID" as order_id,
        "Product ID" as product_id,
        "Sales" as sales,
        "Quantity" as quantity,
        "Discount" as discount,
        "Profit" as profit
    FROM (SELECT * FROM df)
""")

# Now run your query
query = """
WITH customer_stats AS (
    SELECT 
        c.customer_id,
        c.customer_name,
        SUM(s.profit) AS total_profit,
        MAX(s.profit) AS best_order,
        MIN(s.profit) AS worst_order,
        AVG(s.profit) AS avg_profit,
        COUNT(*) AS order_count
    FROM customers c
    JOIN orders o ON c.customer_id = o.customer_id
    JOIN sales s ON o.order_id = s.order_id
    GROUP BY c.customer_id, c.customer_name
)
SELECT 
    *,
    RANK() OVER (ORDER BY total_profit DESC) AS rank
FROM customer_stats
ORDER BY rank
LIMIT 10
"""

result = conn.execute(query).fetchdf()
print(result)
conn.close()

def sample_query():
    conn = duckdb.connect()

    result2 = conn.execute("""
    SELECT category, Country
    FROM read_csv('Sample - Superstore.csv', encoding='cp1252')
    LIMIT 5
""").fetchall()

    print(result2)

sample_query()

import duckdb

def insert_record():
    conn = duckdb.connect(':memory:')

    # Create table from CSV
    conn.execute("""
        CREATE TABLE superstore AS
        SELECT * FROM read_csv_auto('Sample - Superstore.csv', encoding='cp1252')
    """)
    
    # Insert single record
    conn.execute("""
        INSERT INTO superstore 
        VALUES (100, 'NEW-ORDER-001', '2024-06-15', '2024-06-20', 'Express', 'PROD-123', 'John Doe', 'Consumer', 'USA', 'New York', 'NY', 10001, 'East', 'FUR-TA-001', 'Furniture', 'Tables', 'New Table', 499.99, 2, 0.5, 249.95)
    """)
    
    # Insert multiple records
    conn.execute("""
        INSERT INTO superstore VALUES 
        (101, 'NEW-ORDER-002', '2024-06-15', '2024-06-20', 'Standard', 'PROD-124', 'Jane Smith', 'Corporate', 'USA', 'Boston', 'MA', 02101, 'East', 'OFF-BI-001', 'Office Supplies', 'Binders', 'Blue Binders', 19.99, 5, 0.2, 4.00),
        (102, 'NEW-ORDER-003', '2024-06-15', '2024-06-20', 'Standard', 'PROD-125', 'Bob Wilson', 'Consumer', 'USA', 'Seattle', 'WA', 98101, 'West', 'TEC-PH-001', 'Technology', 'Phones', 'Phone', 999.99, 1, 0.1, 99.99)
    """)
    
    # Verify
    result = conn.execute("SELECT * FROM superstore LIMIT 1").fetchall()
    df = pd.DataFrame(result)
    print(df)

insert_record()