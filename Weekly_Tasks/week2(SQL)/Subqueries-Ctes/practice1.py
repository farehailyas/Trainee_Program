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
Find top 5 customers by total profit. Include their order count, average order value, and rank within segment. 
Use window functions + JOIN + CTE.
"""
# join bw order and sasum(s.sales)les

def get_products(conn):
    query = """ WITH order_stats as(SELECT c.customer_name, c.segment ,sum(s.profit) as total_profit , COUNT(*) as order_count , 
                                    (sum(s.sales)/COUNT(*)::FLOAT ) as avg_order_value , RANK () OVER(PARTITION BY c.segment ORDER BY sum(s.profit) DESC)
                                    FROM customers c
                                    JOIN orders o
                                    ON o.customer_id = c.customer_id
                                    JOIN sales s
                                    ON s.order_id = o.order_id
                                    GROUP BY c.customer_id, c.customer_name, c.segment
                                    ORDER BY c.segment)
                SELECT * 
                FROM order_stats
                LIMIT 5
        """

    result = pd.read_sql(query, conn)
    print(result)

conn = get_connection()
get_products(conn)
