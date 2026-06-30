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
"Show each sale and previous sale profit (track performance)"
"""
# join bw order and sales

def get_products(conn):
    query = """ SELECT s.profit , LAG(s.profit) OVER(ORDER BY o.order_date) as prev_sales , s.profit - LAG(s.profit) OVER(ORDER BY o.order_date) diff_from_prev 
                FROM sales s
                JOIN orders o
                ON o.order_id = s.order_id
        """

    result = pd.read_sql(query, conn)
    print(result)

conn = get_connection()
get_products(conn)
