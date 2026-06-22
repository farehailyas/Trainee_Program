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



def get_products(conn):
    cur = conn.cursor()
    query = """ CREATE INDEX customer_orders_index ON orders(customer_id)
        """
    cur.execute(query)
    conn.commit()
    cur.close()
    print("Index created")


conn = get_connection()
get_products(conn)
