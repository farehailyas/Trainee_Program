
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
Q1. For each month in 2017, 
    find the total orders, 
    total sales revenue, 
    and month-over-month sales change. 
Also find the top performing sub-category by sales for each month. Use CTEs and window functions.
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
    query = """  WITH monthly_orders AS(SELECT TO_CHAR(orders.order_date , 'YYYY-MM') as month ,COUNT(*) as total_orders , sum(sales.sales * sales.quantity) as revenue
                                        FROM orders
                                        LEFT JOIN sales 
                                        ON orders.order_id = sales.order_id
                                        WHERE orders.order_date >= '2017-01-01' AND orders.order_date < '2018-01-01'
                                        GROUP BY TO_CHAR(orders.order_date , 'YYYY-MM')),
                monthly_report AS(SELECT * ,  revenue - LAG(revenue) OVER(ORDER BY month) as mom_sales_change
                                    FROM monthly_orders 
                ),
                top_performing_subcatagory AS(SELECT TO_CHAR(orders.order_date , 'YYYY-MM') as month, products.sub_category , RANK() OVER(PARTITION BY TO_CHAR(orders.order_date , 'YYYY-MM') ORDER BY sum(sales.sales) DESC) as top_rank
                                            FROM products 
                                            LEFT JOIN sales
                                            ON products.product_id = sales.product_id
                                            LEFT JOIN orders
                                            ON orders.order_id = sales.order_id
                                            WHERE orders.order_date >= '2017-01-01' AND orders.order_date < '2018-01-01'
                                            GROUP BY TO_CHAR(orders.order_date , 'YYYY-MM') , products.sub_category  )
                SELECT monthly_report.* , top_performing_subcatagory.*
                FROM monthly_report
                LEFT JOIN top_performing_subcatagory
                ON monthly_report.month = top_performing_subcatagory.month
                WHERE top_rank = 1
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
