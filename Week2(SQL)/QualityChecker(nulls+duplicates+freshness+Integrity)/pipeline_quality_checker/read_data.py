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

def read(conn):
    print("truncate tables")        
    query1 = """select * from product_pricing"""
    result = pd.read_sql(query1 , conn)
    print(result)


conn = get_connection()
read(conn)
