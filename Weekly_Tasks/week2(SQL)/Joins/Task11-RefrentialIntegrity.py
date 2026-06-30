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
 Order table cannot insert the customer record that does not exist in customers table
"""
# join bw order and sales

def get_oders(conn):
    query = """ 
        INSERT INTO orders (order_id,Order_Date ,Ship_date , customer_id) VALUES (5010 ,2016-9-7 , 2016-10-1 , 800);
        """

    result = pd.read_sql(query, conn)
    print(result)

conn = get_connection()
get_oders(conn)
# INSERT INTO orders (order_id, customer_id) VALUES (101, 999);