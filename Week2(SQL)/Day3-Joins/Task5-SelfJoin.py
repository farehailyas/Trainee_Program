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
Q5: This query answers: "Find pairs of orders from the same customer placed on the same date"
# Topics: SELF JOIN, WHERE
# Expected: customer_id, order_id1, order_id2, order_date
# KEY: Join table to itself - match orders by same customer AND same date
# Table: orders o1 JOIN orders o2
"""
# join bw order and sales

def get_oders(conn):
    query = """ 
              SELECT o1.customer_id , o1.order_id , o2.order_id , o1.order_date , o2.order_date
              FROM orders o1
              JOIN orders o2
              ON o1.customer_id = o2.customer_id
              WHERE o1.order_date = o2.order_date
              AND o1.order_id < o2.order_id
        """

    result = pd.read_sql(query, conn)
    print(result)

conn = get_connection()
get_oders(conn)
