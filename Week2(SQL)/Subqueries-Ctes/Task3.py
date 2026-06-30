
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
Rewrite task 2 using cte 
This query answers: "Show each region with total sales and difference of total sales from maximum region sales"
# Tables: orders, sales
# Expected: region, total_sales, difference_from_max
"""
# join bw order and sales

def get_products(conn):
    query = """WITH sales_per_region AS(
                    SELECT o.region, sum(s.sales) as total_sales
                    FROM sales s
                    JOIN orders o
                    ON s.order_id = o.order_id
                    GROUP BY o.region
                ),
                max_total_sales as(
                    SELECT max(total_sales) as max_total
                    FROM sales_per_region
                )
                SELECT sr.region , sr.total_sales , (mx.max_total - sr.total_sales) AS diff_from_max 
                FROM sales_per_region sr
                CROSS JOIN max_total_sales mx
        """

    result = pd.read_sql(query, conn)
    print(result)

conn = get_connection()
get_products(conn)
