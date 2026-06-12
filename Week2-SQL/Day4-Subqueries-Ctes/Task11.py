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
Practice all concepts together
Q1: This query answers: "Show each customer's rank by total spending within their segment (Consumer, Corporate, Home Office)"
Topics: CTE, ROW_NUMBER, PARTITION BY segment
Expected: customer_name, segment, total_spent, rank_in_segment
"""
# join bw order and sales

def get_products(conn):
    query = """  WITH customer_segment_spending AS(
                    SELECT c.customer_name , c.segment ,SUM(s.sales) as total_spending
                    FROM orders o
                    JOIN customers c
                    ON c.customer_id = o.customer_id
                    JOIN sales s
                    ON s.order_id = o.order_id
                    GROUP BY c.segment, c.customer_name
                )
                SELECT cs.customer_name , cs.segment , cs.total_spending as total_spent , ROW_NUMBER() OVER (PARTITION BY cs.segment ORDER BY cs.total_spending )  AS rank_in_segment
                FROM customer_segment_spending cs
                
        """
    result = pd.read_sql(query, conn)
    print(result)

conn = get_connection()
get_products(conn)
