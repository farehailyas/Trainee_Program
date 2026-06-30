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

"""  # Q1: This query answers: "Show all distinct product categories"
# Topics: SELECT, DISTINCT
# Expected: List of unique categories (no duplicates)
"""

def get_products(conn):
    cur = conn.cursor()
    query = """ SELECT DISTINCT product_name , category 
            FROM products
        """
    result = pd.read_sql(query, conn)
    cur.close()
    print(result)


conn = get_connection()
get_products(conn)
