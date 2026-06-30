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
Q5: This query answers: "Count total number of distinct customers in 'Consumer' segment who ordered in 'East' region"
# Topics: SELECT, WHERE, AND, COUNT, DISTINCT
# Expected: Single number - total distinct consumers in East region
"""
# join bw order and customers
def get_customers(conn):
    query = """SELECT COUNT(DISTINCT c.customer_id) AS Total_distinct_customers 
                FROM customers c
                INNER JOIN orders o
                ON o.customer_id = c.customer_id
                WHERE c.segment = 'Consumer' AND o.region = 'East'
        """
    result = pd.read_sql(query, conn)
    print(result)

conn = get_connection()
get_customers(conn)
