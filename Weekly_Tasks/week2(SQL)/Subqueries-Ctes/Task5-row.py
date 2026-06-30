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
Give unique rank to top 10 sales by profit
"""
# join bw order and sales

def get_products(conn):
    query = """ SELECT order_id , profit ,  
                ROW_NUMBER() OVER (ORDER BY profit DESC) 
                FROM sales
                LIMIT 10
        """

    result = pd.read_sql(query, conn)
    print(result)

conn = get_connection()
get_products(conn)
