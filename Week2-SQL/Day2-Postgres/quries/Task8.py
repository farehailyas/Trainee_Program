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
 Q6: This query answers: "Get 5 cheapest sales, skip first 2"
# Topics: SELECT, ORDER BY, LIMIT, OFFSET
# Expected: order_id, sales (skip 2, get next 5)
"""
def get_sales(conn):
    query = """
        SELECT order_id, sales
        FROM sales
        ORDER BY sales
        LIMIT 5 OFFSET 2
        """
    result = pd.read_sql(query, conn)
    print(result)

conn = get_connection()
get_sales(conn)
