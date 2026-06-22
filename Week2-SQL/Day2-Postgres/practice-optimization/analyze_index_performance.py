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

def get_customers_without_index(conn):
    cur = conn.cursor()
    query = """ EXPLAIN ANALYZE SELECT customer_id 
                FROM customers
                WHERE customer_id >= '100' OR customer_id <= '500'
        """
    result = pd.read_sql(query, conn)
    cur.close()
    print(result)    

def get_customers_with_index(conn):
    cur = conn.cursor()
    query = """ EXPLAIN ANALYZE SELECT orders.region
                FROM customers
                 JOIN orders
                ON customers.customer_id = orders.customer_id
                
                GROUP BY orders.region
        """
    result = pd.read_sql(query, conn)
    cur.close()
    print(result)


conn = get_connection()
get_customers_without_index(conn)
print()
get_customers_with_index(conn)
