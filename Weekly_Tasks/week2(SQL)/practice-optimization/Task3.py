
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
Q3. For each customer, show each order with its rank by sales (within that customer), 
and a running cumulative total of sales ordered by order date. Use CTEs, DENSE_RANK(), SUM() as window function.
"""
def create_index(conn):
    cur = conn.cursor()
    query = """CREATE INDEX sales_ind ON sales(order_id)
        """

    cur.execute(query)
    conn.commit()
    # result = pd.read_sql(query, conn)
    cur.close()
    # print(result)    

def get_customers(conn):
    cur = conn.cursor()
    query = """  WITH rank_orders AS(SELECT orders.customer_id ,orders.order_id  ,orders.order_date, sum(sales.sales) total_sales,
                                        DENSE_RANK() OVER(PARTITION BY orders.customer_id ORDER BY SUM(sales.sales) DESC) rank_by_sale
                                        FROM orders
                                        JOIN sales
                                        ON orders.order_id = sales.order_id 
                                        GROUP BY orders.customer_id ,orders.order_id ,orders.order_date
                                        ORDER BY rank_by_sale
                                    ),
                    running_total AS(SELECT rank_orders.* , 
                                    SUM(total_sales) OVER(PARTITION BY customer_id ORDER BY order_date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) as running_sum
                                    FROM rank_orders ) 

                SELECT * 
                FROM running_total   
                ORDER BY customer_id          
        """
    result = pd.read_sql(query, conn)
    cur.close()
    print(result)    

# def get_customers_with_index(conn):
#     cur = conn.cursor()
#     query = """ EXPLAIN ANALYZE SELECT orders.region
#                 FROM customers
#                  JOIN orders
#                 ON customers.customer_id = orders.customer_id
                
#                 GROUP BY orders.region
#         """
#     result = pd.read_sql(query, conn)monthly_orders
#     cur.close()
#     print(result)


conn = get_connection()
get_customers(conn)
# create_index(conn)
