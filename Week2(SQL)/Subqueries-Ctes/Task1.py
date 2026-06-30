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
Q1: This query answers: "Find products that have higher average profit than the overall average profit"
# Expected: product_name, category, avg_profit
"""
# join bw order and sales

def get_products(conn):
    query = """ SELECT p.product_name , p.category , AVG(s.profit)
                FROM products p
                JOIN sales s
                ON s.product_id = p.product_id
                GROUP BY p.product_name , p.category
                HAVING AVG(s.profit) > (SELECT  AVG(sales)
                                        FROM sales
                                        )
        """

    result = pd.read_sql(query, conn)
    print(result)

conn = get_connection()
get_products(conn)
