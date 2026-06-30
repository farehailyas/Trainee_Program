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
"""Understanding the SQL order of execution changes how you think about constructing queries. For example, 
imagine you write a query to filter rows based on an alias you created in the SELECT clause:

SELECT price * 0.9 AS discounted_price
FROM products
WHERE discounted_price > 100;

Powered By 
At first glance, this looks logical, but it will throw an error. Why? 
Because the WHERE clause is evaluated before the SELECT clause in SQL's execution order. 
To fix it, you'd need to use a subquery or HAVING instead:

"""

def get_products(conn):
    cur = conn.cursor()
    query = """ EXPLAIN SELECT  (profit * discount) as discount_profit  
                FROM sales
               
        """
    result = pd.read_sql(query, conn)
    cur.close()
    print(result)


conn = get_connection()
get_products(conn)
