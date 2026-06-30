
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


def monthly_revenue(conn):
    cur = conn.cursor()
    query = """ WITH monthly_revenue AS(SELECT TO_CHAR(%Y-%m , order.order_date ) as month , 
                        COUNT(orders.order_id) as completed_orders , SUM(total) as revenue
                        FROM orders 
                        WHERE status = 'completed' AND TO_CHAR(%Y , order.order_date ) = 2025 AND total IS NOT NULL
                        GROUP BY TO_CHAR(%Y-%m , order.order_date )
                    ),
                    revenue_change AS(
                        SELECT * , revenue - LAG(revenue) as mom_change
                        FROM monthly_revenue
                    ),
                    product_category_revenue AS(
                        SELECT SUM(order_item.unit_price*order_items.quantity) as prod_cat_rev , TO_CHAR(%Y-%m , order.order_date ) as month
                        FROM products
                        JOIN order_items
                        ON order_items.product_id = products.id
                         WHERE status = 'completed' AND TO_CHAR(%Y , order.order_date ) = 2025 AND total IS NOT NULL
                        GROUP BY products.catgoery, TO_CHAR(%Y-%m , order.order_date ) 
                    ),
                    rank_revenue AS(SELECT revenue_change.*, product_category_revenue.catgoery,RANK() OVER(PARTITON BY revenue_change.month ORDER BY product_category_revenue.prod_cat_rev) as rnk
                        FROM revenue_change
                        LEFT JOIN product_category_revenue
                        ON revenue_change.month = revenue_change.month
                    )
                    SELECT * FORM rank_revenue WHERE rnk = 1
                    
              
        """
    result = pd.read_sql(query, conn)
    cur.close()
    print(result)    

def window_function(conn):
    cur = conn.cursor()
    query = """
            SELECT order.order_id ,order.customer_id , order.order_date , order.total
            ,RANK() OVER(PARTITON BY order.customer_id ORDER BY order.total DESC) AS rank_within_customer , 
            order.total - LAG(order.total) OVER(PARTITION BY order.customer_id ORDER BY order.order_date) as diff_from_prev_order
            FROM order
            ODER  BY order.customer_id , order.customer_date
     """
    result = pd.read_sql(query, conn)
    cur.close()
    print(result)   

def running_total(conn):

    cur = conn.cursor()
    query = """
            SELECT order.order_id ,order.customer_id , order.order_date , order.total
            ,DENSE_RANK() OVER(PARTITON BY order.customer_id ORDER BY order.total DESC) AS rank_within_customer , 
            SUM (order.total) OVER(PARTITON BY customer_id ORDER BY order.order_date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)
            FROM order
            WHERE total IS NOT NULL
            ODER  BY order.customer_id , order.customer_date
     """
    result = pd.read_sql(query, conn)
    cur.close()
    print(result)  

def aggregation(conn):

    cur = conn.cursor()
    query = """
            SELECT country , COUNT(DISTINCT id) customer_count , distinct_count, AVG(order.total) as avg_total 
            FROM customers
            LEFT JOIN orders
            ON id = order.id
            GROUP BY country
            HAVING AVG(order.total) > 500
            ORDER BY avg_total DESC
     """
    result = pd.read_sql(query, conn)
    cur.close()
    print(result)  
def orphaned_rows(conn):
    cur = conn.cursor()
    query = """
            SELECT order.order_id , COUNT(*) orphaned_row_count
            FROM order_items
            LEFT JOIN order
            ON order.id = order_items.order_id 
            WHERE order.id IS NULL
            GROUP BY order.order_id 
     """
    result = pd.read_sql(query, conn)
    cur.close()
    print(result) 
    
conn = get_connection()
get_customers(conn)
# create_index(conn)
