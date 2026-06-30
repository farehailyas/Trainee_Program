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
Q2: This query answers: "For each region, show total sales, running total of sales by region (ordered by month), and compare to previous month"
Topics: CTE, SUM OVER (running total), LAG
Expected: region, month, monthly_sales, running_total, prev_month_sales
"""
# join bw order and sales

def get_products(conn):
    query = """ 
            WITH monthly_sales AS(SELECT o.region , DATE_TRUNC('month' , o.order_date) as month , sum(s.sales) as monthly_sales
                FROM orders o 
                JOIN sales s
                ON o.order_id = s.order_id
                GROUP BY o.region,DATE_TRUNC('month' , o.order_date) 
            )

            SELECT ms.region , ms.month ,ms.monthly_sales  , 
            sum(ms.monthly_sales) OVER(PARTITION BY region ORDER BY month) as running_total, 
            LAG(ms.monthly_sales) OVER (PARTITION BY region ORDER BY month) as prev_month_sales
            FROM monthly_sales ms
            ORDER BY ms.region , ms.month
        """
    result = pd.read_sql(query, conn)
    print(result)

conn = get_connection()
get_products(conn)
