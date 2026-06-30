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
 Q7: This query answers: "Find customers who ordered in 'East' region AND also ordered in 'West' region"
"""
# join bw order and sales

def get_oders(conn):
    query = """ SELECT c.customer_id
                FROM customers c
                JOIN orders o
                ON o.customer_id = c.customer_id
                WHERE region = 'East'
                INTERSECT
                SELECT c.customer_id
                FROM customers c
                JOIN orders o
                ON o.customer_id = c.customer_id
                WHERE region = 'West'
        """

    result = pd.read_sql(query, conn)
    print(result)

conn = get_connection()
get_oders(conn)
