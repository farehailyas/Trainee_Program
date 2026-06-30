
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
Q4. For each region, count distinct customers and find average order sales. Only show regions where average sales exceed 200. 
Use EXISTS() instead of COUNT() for any existence check, LEFT JOIN, no subqueries.
"""    

def get_customers(conn):
    cur = conn.cursor()
    query = """WITH customers_in_region AS(SELECT orders.region , COUNT(DISTINCT orders.customer_id) distinct_customer_count, AVG(sales.sales) AS avg_order_sales
                                                FROM orders
                                                LEFT JOIN sales
                                                ON orders.order_id = sales.order_id
                                                GROUP BY orders.region
                                                HAVING AVG(sales.sales) > 200 )
                select * from customers_in_region
        """
    result = pd.read_sql(query, conn)
    cur.close()
    print(result)    

conn = get_connection()
get_customers(conn)
# create_index(conn)
