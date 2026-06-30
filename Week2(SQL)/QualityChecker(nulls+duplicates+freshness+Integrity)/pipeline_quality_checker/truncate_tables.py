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


# join bw order and sales

def truncate(conn):
    print("truncate tables")        
    query1 = """TRUNCATE table inventory CASCADE"""
    query2 = """TRUNCATE table product_pricing CASCADE"""
    query3 = """TRUNCATE table amazon_sales CASCADE"""
    query4 = """TRUNCATE table international_sales CASCADE"""
    query5 = """TRUNCATE table warehouse_comparison CASCADE"""
    query6 = """TRUNCATE table expenses CASCADE"""

    cur = conn.cursor()
    cur.execute(query1)
    cur.execute(query2)
    cur.execute(query3)
    cur.execute(query4)
    cur.execute(query5)
    cur.execute(query6)
    conn.commit()
    # print(result)


conn = get_connection()
truncate(conn)
