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
def get_sales(conn):
    query = """
    SELECT  order_id , profit 
            FROM sales 
            where profit BETWEEN 100 AND 500;
        """
    result = pd.read_sql(query, conn)
    print(result)

conn = get_connection()
get_sales(conn)
