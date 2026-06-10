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
# Q1: This query answers: "Show all products that have been sold with their sales details"
# Topics: INNER JOIN, SELECT
# Expected: product_name, category, sales_amount, quantity, profit
# KEY: Only products WITH sales (matching rows from both tables)
# Tables: products JOIN sales
"""
# join bw order and sales
def get_products(conn):
    query = """ SELECT p.product_name , p.category , s.sales , s.quantity , s.profit
                FROM products p 
                INNER JOIN sales s
                ON p.product_id = s.product_id
        """
    result = pd.read_sql(query, conn)
    print(result)

conn = get_connection()
get_products(conn)
