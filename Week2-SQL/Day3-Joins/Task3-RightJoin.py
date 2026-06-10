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
# Q3: This query answers: "Show all orders with customer details, even if customer data is missing"
# Topics: RIGHT JOIN, SELECT
# Expected: order_id, order_date, customer_name, segment, region
# KEY: All orders (right) + matching customers (left)
# Tables: customers RIGHT JOIN orders
"""
# join bw order and sales
def get_orders(conn):
    query = """ 
                SELECT o.order_id, o.order_date, c.customer_name, c.segment, o.region
                FROM customers c 
                RIGHT JOIN orders o
                ON c.customer_id = o.customer_id
        """

    result = pd.read_sql(query, conn)
    print(result)

conn = get_connection()
get_orders(conn)
