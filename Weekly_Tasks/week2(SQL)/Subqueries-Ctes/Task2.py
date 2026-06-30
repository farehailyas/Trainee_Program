
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
This query answers: "Show each region with total sales and difference of total sales from maximum region sales"
# Tables: orders, sales
# Expected: region, total_sales, difference_from_max
"""
# join bw order and sales

def get_products(conn):
    query = """ SELECT o.region , sum(s.sales) as sales_sum , 
                (SELECT max(total_sales) 
                    FROM(SELECT sum(sales) as total_sales
                        FROM sales s2
                        JOIN orders o2
                        ON o2.order_id = s2.order_id
                        GROUP BY o2.region) as region_sales ) - sum(s.sales) as diff_from_max
                FROM orders o
                JOIN sales s
                ON o.order_id = s.order_id
                GROUP BY o.region
        """

    result = pd.read_sql(query, conn)
    print(result)

conn = get_connection()
get_products(conn)
