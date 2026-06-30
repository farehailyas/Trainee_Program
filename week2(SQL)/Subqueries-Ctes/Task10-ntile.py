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
"Divide customers into 4 spending groups (VIP to Low)"
"""
# join bw order and sales

def get_products(conn):
    query = """ SELECT c.customer_name, sum(s.sales) as Total_sum , NTILE(4) OVER(ORDER BY sum(s.sales)) as quartile,
                CASE 
                    WHEN NTILE(4) OVER(ORDER BY sum(s.sales)) = 4 THEN 'VIP'
                    WHEN NTILE(4) OVER( ORDER BY sum(s.sales)) = 1 THEN 'Low'
                    ELSE 'Medium'
                END as ordered_placed_customers
                FROM customers c
                JOIN orders o
                ON o.customer_id = c.customer_id
                JOIN sales s
                ON s.order_id = o.order_id
                 GROUP BY c.customer_id, c.customer_name
        ORDER BY sum(s.sales) DESC
        """
    result = pd.read_sql(query, conn)
    print(result)

conn = get_connection()
get_products(conn)
