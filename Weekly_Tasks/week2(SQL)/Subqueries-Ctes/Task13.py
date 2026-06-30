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
Q3: This query answers: "Show top 3 products in each category by profit, with their profit rank within category"
Topics: CTE, RANK, PARTITION BY category, then filter top 3
Expected: category, product_name, total_profit, rank_in_category
"""
# join bw order and sales

def get_products(conn):
    query = """ 
            WITH products_category_profit AS(SELECT p.product_name , p.category , sum(s.profit) as total_profit 
                FROM products p
                JOIN sales s
                ON s.product_id = p.product_id
                GROUP BY p.product_name , p.category
                Order BY p.category),

            ranked_products AS(
                SELECT pc.product_name , pc.category , pc.total_profit , RANK() OVER (PARTITION BY pc.category ORDER BY total_profit DESC ) as rank_in_category
                FROM products_category_profit pc
            )

            SELECT product_name, category , total_profit , rank_in_category
            FROM ranked_products
            WHERE rank_in_category <= 3
            ORDER BY category
            
        """
    result = pd.read_sql(query, conn)
    print(result)

conn = get_connection()
get_products(conn)
