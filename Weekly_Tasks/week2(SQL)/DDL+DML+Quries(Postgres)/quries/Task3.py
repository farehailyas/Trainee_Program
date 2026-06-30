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
Q3: This query answers: "List products whose name contains 'Chair' OR category is 'Office Supplies'"
# Topics: WHERE, OR, LIKE
# Expected: Product name, category, sub_category
"""
# join bw order and sales
def get_products(conn):
    query = """ SELECT * 
                FROM products
                WHERE product_name LIKE '%Chair%'
                OR category = 'Office Supplies'
        """
    result = pd.read_sql(query, conn)
    print(result)

conn = get_connection()
get_products(conn)
