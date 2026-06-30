
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
 Q7: This query answers: "Find states that received shipments BUT never had profitable sales"
"""
# join bw order and sales

def get_oders(conn):
    query = """ 
        SELECT DISTINCT o.state , o.country
        FROM orders o
        JOIN sales s ON o.order_id = s.order_id
        EXCEPT
        SELECT DISTINCT o.state , o.country
        FROM orders o
        JOIN sales s ON o.order_id = s.order_id
        WHERE s.profit > 0
        """

    result = pd.read_sql(query, conn)
    print(result)

conn = get_connection()
get_oders(conn)
