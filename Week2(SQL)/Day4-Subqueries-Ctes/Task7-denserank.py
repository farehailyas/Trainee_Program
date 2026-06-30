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
"Rank regions by profit without skipping ranks"
"""
# join bw order and sales

def get_products(conn):
    query = """ SELECT o.region ,SUM(s.profit) as profit_across_regions , DENSE_RANK() OVER(ORDER BY SUM(s.profit) DESC) as rank
                FROM orders o
                JOIN sales s
                ON o.order_id = s.order_id
                GROUP BY o.region 
                ORDER BY rank
        """

    result = pd.read_sql(query, conn)
    print(result)

conn = get_connection()
get_products(conn)
