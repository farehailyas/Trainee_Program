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
Q6: This query answers: "Show each salesperson (customer_id) their rank, their best order profit, worst order profit, and running average profit"
Topics: CTE for customer monthly stats, RANK, MIN/MAX OVER, AVG OVER (running)
Expected: customer_id, customer_name, total_profit, best_order, worst_order, running_avg_profit, rank

"""
# join bw order and sales
def get_products(conn):
    query = """
    WITH customer_stats AS (
        SELECT 
            c.customer_id,
            c.customer_name,
            SUM(s.profit) AS total_profit,
            MAX(s.profit) AS best_order,
            MIN(s.profit) AS worst_order,
            AVG(s.profit) AS avg_profit,
            COUNT(*) AS order_count
        FROM customers c
        JOIN orders o ON o.customer_id = c.customer_id
        JOIN sales s ON s.order_id = o.order_id
        GROUP BY c.customer_id, c.customer_name
    )
    SELECT  *, RANK() OVER (ORDER BY total_profit DESC) AS rank
    FROM customer_stats
    ORDER BY rank
"""
    
    result = pd.read_sql(query, conn)
    print(result)

conn = get_connection()
get_products(conn)

