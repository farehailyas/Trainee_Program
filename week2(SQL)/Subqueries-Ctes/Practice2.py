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
Find products where average profit is negative across all orders. Show: Product name, category, total sales, total quantity sold, avg profit per unit. 
Use subquery to filter, JOIN 3 tables.
"""
# join bw order and sasum(s.sales)les

def get_products(conn):
    query = """ WITH product_stats as(SELECT p.product_name, p.category , sum(s.sales) as total_sales , sum(s.quantity) as total_quantity_sold, 
                                    (sum(s.profit) ::FLOAT /sum(s.quantity)) as avg_profit_per_unit
                                    FROM products p 
                                    JOIN sales s
                                    ON s.product_id = p.product_id
                                    GROUP BY p.product_name, p.category
                                    )
                SELECT * 
                FROM product_stats
                WHERE avg_profit_per_unit < 0
                ORDER BY avg_profit_per_unit ASC
        """

    result = pd.read_sql(query, conn)
    print(result)

conn = get_connection()
get_products(conn)
