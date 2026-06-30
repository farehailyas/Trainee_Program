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
Show top products by sales, with ranking"
"""
# join bw order and sales

def get_products(conn):
    query = """ SELECT p.product_name, p.category , RANK() OVER (ORDER BY s.sales DESC) As rank
                FROM products p
                JOIN sales s
                ON s.product_id , s.product_id
        """

    result = pd.read_sql(query, conn)
    print(result)

conn = get_connection()
get_products(conn)
