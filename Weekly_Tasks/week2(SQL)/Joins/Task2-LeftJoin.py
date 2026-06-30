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
# Q2: This query answers: "Show all customers and their total orders, including customers with no orders"
# Topics: LEFT JOIN, GROUP BY, COUNT, SUM
# Expected: customer_name, segment, order_count, total_spending
# KEY: All customers + matching orders (right), even if NULL
"""
# join bw order and sales
def get_customers(conn):
    query = """ SELECT c.customer_name , c.segment , COUNT(*) as order_count
                FROM customers c 
                LEFT JOIN orders o
                ON c.customer_id = o.customer_id
                GROUP BY c.customer_id, c.customer_name, c.segment
        """
   
    result = pd.read_sql(query, conn)
    print(result)

conn = get_connection()
get_customers(conn)
