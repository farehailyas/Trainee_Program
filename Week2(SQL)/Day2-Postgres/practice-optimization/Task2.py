
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
Q2. For each customer, rank their orders by sales amount within their segment, 
and calculate the difference in sales from their previous order (by order date). Use CTEs, PARTITION BY, LAG().
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
    query = """ WITH orders_within_sales AS(SELECT customers.customer_id , orders.order_id, customers.segment , orders.order_date
                                            FROM customers
                                            LEFT JOIN orders 
                                            ON customers.customer_id = orders.customer_id
                                            ),
                rank_orders AS(SELECT orders_within_sales.customer_id , orders_within_sales.segment , orders_within_sales.order_id, orders_within_sales.order_date ,sum(sales.sales) as sales,
                    RANK() OVER(PARTITION BY orders_within_sales.segment ORDER BY sum(sales.sales) DESC) as rank
                                    FROM orders_within_sales
                                    JOIN sales
                                    ON sales.order_id =  orders_within_sales.order_id
                                    GROUP BY orders_within_sales.customer_id , orders_within_sales.segment , orders_within_sales.order_id, orders_within_sales.order_date
                    ) ,
                diff_from_prev AS( SELECT rank_orders.* , sales - LAG(sales) OVER( PARTITION BY customer_id ORDER BY order_date  )  as diff_from_prev
                    FROM rank_orders

                )                    
                SELECT * FROM diff_from_prev
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
