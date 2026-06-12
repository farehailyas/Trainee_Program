import pandas as pd
import sys
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

sys.path.append(str(Path(__file__).parent.parent))
from db_connection import get_dbConnection

conn = get_dbConnection()

def check_duplicates():
    return pd.read_sql("""
        SELECT 'customers' as table_name, COUNT(*) as duplicates
        FROM (
            SELECT customer_id 
            FROM customers 
            GROUP BY customer_id 
            HAVING COUNT(*) > 1) x
        UNION ALL
        SELECT 'products', COUNT(*)
        FROM (
            SELECT product_id 
            FROM products 
            GROUP BY product_id 
            HAVING COUNT(*) > 1) x
        UNION ALL
        SELECT 'orders', COUNT(*)
        FROM (
            SELECT order_id 
            FROM orders 
            GROUP BY order_id 
            HAVING COUNT(*) > 1) x
        UNION ALL
        SELECT 'sales', COUNT(*)
        FROM (
            SELECT order_id, product_id 
            FROM sales 
            GROUP BY order_id, product_id 
            HAVING COUNT(*) > 1) x
    """, conn)

def check_nulls():
    return pd.read_sql("""
        SELECT 'customers' as table_name, COUNT(*) - COUNT(customer_name) as nulls 
        FROM customers
        UNION ALL
        SELECT 'orders', COUNT(*) - COUNT(customer_id) 
        FROM orders
        UNION ALL
        SELECT 'products', COUNT(*) - COUNT(product_name) 
        FROM products
        UNION ALL
        SELECT 'sales', COUNT(*) - COUNT(profit) 
        FROM sales
    """, conn)

def check_referential_integrity():
    return pd.read_sql("""
        SELECT 'orders -> customers' as relationship, 
               COUNT(*) as orphaned_count
        FROM orders o 
        LEFT JOIN customers c
        ON o.customer_id = c.customer_id
        WHERE c.customer_id IS NULL
        UNION ALL
        SELECT 'sales -> orders', COUNT(*)
        FROM sales s 
        LEFT JOIN orders o 
        ON s.order_id = o.order_id
        WHERE o.order_id IS NULL
        UNION ALL
        SELECT 'sales -> products', COUNT(*)
        FROM sales s 
        LEFT JOIN products p 
        ON s.product_id = p.product_id
        WHERE p.product_id IS NULL
    """, conn)

def check_freshness():
    return pd.read_sql("""
        SELECT 'customers' as table_name, COUNT(*) as rows, NULL::date as oldest, NULL::date as newest 
        FROM customers
        UNION ALL
        SELECT 'products', COUNT(*), NULL, NULL 
        FROM products
        UNION ALL
        SELECT 'orders', COUNT(*), MIN(order_date), MAX(order_date) 
        FROM orders
        UNION ALL
        SELECT 'sales', COUNT(*), NULL, NULL 
        FROM sales
    """, conn)

print("DUPLICATE DETECTION")
result = check_duplicates()
print(result if len(result) > 0 else "No duplicates")

print("\nNULL AUDIT")
result = check_nulls()
print(result)

print("\nREFERENTIAL INTEGRITY")
result = check_referential_integrity()
print(result if len(result) > 0 else " No orphaned records")

print("\nFRESHNESS CHECK")
result = check_freshness()
print(result)


conn.close()