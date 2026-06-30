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
 Q1: This query answers: "List all unique product names from both 'Furniture' AND 'Office Supplies' categories"
# Topics: UNION, WHERE, SELECT
# Expected: product_name (no duplicates)
"""
# join bw order and sales

def get_oders(conn):
    query = """ SELECT DISTINCT product_name 
                FROM products 
                WHERE category = 'Furniture'
                UNION
                SELECT DISTINCT product_name 
                FROM products 
                WHERE category = 'Office Supplies'
        """

    result = pd.read_sql(query, conn)
    print(result)

conn = get_connection()
get_oders(conn)
