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
Q4: This query answers: "Divide customers into 4 spending tiers (VIP, High, Medium, Low) and show how many orders each customer placed per tier"
Topics: CTE with NTILE, COUNT window function
Expected: customer_name, total_spent, tier, order_count

"""
# join bw order and sales

def get_products(conn):
    query = """ 
        WITH divide_customers AS (SELECT c.customer_name ,sum(s.sales) as total_spent , NTILE(4) OVER (ORDER BY SUM(s.sales)) as tier,
           CASE
                WHEN NTILE(4) OVER (ORDER BY SUM(s.sales)) = 4 THEN 'VIP'
                WHEN NTILE(4) OVER (ORDER BY SUM(s.sales)) = 3 THEN 'HIGH'
                WHEN NTILE(4) OVER (ORDER BY SUM(s.sales)) = 2 THEN 'Medium'
                WHEN NTILE(4) OVER (ORDER BY SUM(s.sales)) = 1 THEN 'Low'
                ELSE 'NOTHING'
                END AS tiering

            FROM customers c
            JOIN orders o
            ON o.customer_id = c.customer_id
            JOIN sales s
            ON s.order_id = o.order_id
            GROUP BY c.customer_name)
        
       
        SELECT dc.customer_name, dc.total_spent, dc.tier , dc.tiering , COUNT(*) as order_count 
        FROM orders o
        JOIN divide_customers dc 
        ON o.customer_id IN (SELECT customer_id from customers WHERE customer_id = o.customer_id)
        GROUP BY  dc.customer_name, dc.total_spent, dc.tier , dc.tiering
        
        ORDER BY dc.tiering DESC
        """
    result = pd.read_sql(query, conn)
    print(result)

conn = get_connection()
get_products(conn)
