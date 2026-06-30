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

# Q4: This query answers: "Show all products and all sales, including unmatched records"
# Topics: FULL OUTER JOIN, SELECT
# Expected: product_name, order_id, sales, profit
# KEY: ALL from both tables - matched and unmatched
# Tables: products FULL OUTER JOIN sales
"""
# join bw order and sales
def get_products_sales(conn):
    query = """ 
            SELECT * 
            FROM products p 
            FULL OUTER JOIN sales s
            ON s.product_id = p.product_id
        """

    result = pd.read_sql(query, conn)
    print(result)

conn = get_connection()
get_products_sales(conn)
