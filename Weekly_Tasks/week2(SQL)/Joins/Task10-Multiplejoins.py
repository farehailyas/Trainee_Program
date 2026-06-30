import pandas as pd
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from db_connection import get_dbConnection

def get_connection():    
    try:
        conn = get_dbConnection()
        print("Connected to db")
        return conn
    except Exception as e:
        print(e)

"""  
 # Q1: This query answers: "Show each customer's name, segment, total number of orders they placed, total sales amount, and average profit. Include customers who have never placed orders (show 0 orders). List results sorted by total sales DESC"

# Required tables: customers, orders, sales, products
# Required JOIN types: Multiple (use appropriate join types)
# Expected output columns: customer_name, segment, order_count, total_sales, avg_profit
# Constraint: Must handle customers with no orders
"""
# join bw order and sales

def get_oders(conn):
    query = """ SELECT c.customer_name , c.segment , COUNT(*) as order_count ,SUM(s.sales) as total_sales , AVG(s.profit) as avg_profit
                FROM customers c
                LEFT JOIN orders o
                ON o.customer_id = c.customer_id
                LEFT JOIN sales s
                ON s.order_id = o.order_id
                GROUP BY c.customer_name , c.segment
                ORDER BY SUM(s.sales) DESC
        """

    result = pd.read_sql(query, conn)
    print(result)

conn = get_connection()
get_oders(conn)
