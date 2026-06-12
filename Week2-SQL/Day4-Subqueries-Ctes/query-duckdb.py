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