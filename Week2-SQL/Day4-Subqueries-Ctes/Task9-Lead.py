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
"Show next customer order info (what they ordered next)"
"""
# join bw order and sales

def get_products(conn):
    query = """ SELECT c.customer_name , o.order_date , LEAD( o.order_date) OVER (PARTITION BY c.customer_id ORDER BY o.order_date) 
                as next_order_date , LAG(o.order_id) OVER(PARTITION BY c.customer_id ORDER BY o.order_date) as Next_order_id
                FROM customers c
                JOIN orders o
                ON o.customer_id = c.customer_id
        """
    result = pd.read_sql(query, conn)
    print(result)

conn = get_connection()
get_products(conn)
