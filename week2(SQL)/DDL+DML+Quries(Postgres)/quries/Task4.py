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
Q3: Q4: This query answers: "What is the average profit per category? Show only categories with average profit > 20"
# Topics: GROUP BY, HAVING, AVG (HAVING cannot use WHERE here)
# Expected: Category, average profit (only where avg > 20)
# KEY: You CANNOT filter with WHERE because average is calculated AFTER grouping
"""
# join bw order and sales
def get_products(conn):
    query = """ SELECT p.category , AVG(s.profit) as average_profit
            FROM products p 
            INNER JOIN sales s
            ON s.product_id = p.product_id
            GROUP BY p.category
            HAVING AVG(s.profit) > 20
        """
    # query1 = """SELECT DISTINCT category FROM products """
    result = pd.read_sql(query, conn)
    print(result)

conn = get_connection()
get_products(conn)
