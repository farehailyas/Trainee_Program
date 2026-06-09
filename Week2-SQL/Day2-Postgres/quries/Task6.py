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
 Q6: This query answers: "Find sales where profit is BETWEEN 100 and 500"
# Topics: WHERE, BETWEEN
# Expected: order_id, profit
"""
# join bw order and sales
def get_orders(conn):
    query = """ SELECT * 
                FROM orders o
                INNER JOIN sales s
                ON s.order_id = o.order_id
                WHERE s.profit > 100 AND s.discount = 0
                ORDER BY s.profit DESC
                LIMIT 5
        """
    result = pd.read_sql(query, conn)
    print(result)

conn = get_connection()
get_orders(conn)
