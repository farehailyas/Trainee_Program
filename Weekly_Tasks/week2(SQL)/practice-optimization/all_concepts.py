
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
For each region, find the top 2 sales representatives (customers) who have shown consistent growth — meaning their total 
sales in the most recent year are higher than their total sales in the previous year

 — but only consider customers who have 
placed orders in at least 3 different states and whose average discount given is below the overall average discount across all orders.
For those qualifying customers, show their region, customer name, their sales in both years, the growth percentage, 
their rank within the region by growth percentage, and a running total of sales (ordered by growth percentage descending) within each region.

"""
def delete_indexes(conn):
    cur = conn.cursor()
    query_drop = """
    DROP INDEX IF EXISTS idx_sales_order_sales;
DROP INDEX IF EXISTS sales_order_ind;
DROP INDEX IF EXISTS sales_ind;
DROP INDEX IF EXISTS order_ind;
DROP INDEX IF EXISTS customer_index;
    """

    cur.execute(query_drop)
    conn.commit()
    print("Unused indexes deleted")
def create_index(conn):
    cur = conn.cursor()
    # query = """ CREATE INDEX customer_orders_index ON orders(customer_id)"""
    # query = """ CREATE INDEX idx_orders_order_date ON orders(order_date)"""
    # query3 = """CREATE INDEX idx_customer_customer_id ON customers(customer_id);"""
    # query4 = """CREATE INDEX idx_sales_order_id ON sales(order_id)"""
    # query5 = """CREATE INDEX idx_orders_customer_state ON orders(customer_id, state);"""
    # query6 = """CREATE INDEX idx_orders_customer_year_region ON orders(customer_id, region, order_date);
# CREATE INDEX idx_sales_order_sales ON sales(order_id, sales);"""
    query7 = """CREATE INDEX sales_order_ind ON sales(order_id, sales);"""
    cur.execute(query7)
    # cur.execute(query3)
    conn.commit()
    cur.close()
    print("Index created")
 # EXPLAIN ANALYZE WITH prev_sales_temp AS(
    #     SELECT orders.customer_id, orders.region, SUM(sales.sales) as current_sale, 
    #         LAG(SUM(sales.sales)) OVER(PARTITION BY orders.customer_id ORDER BY EXTRACT(YEAR FROM orders.order_date)) AS prev_sales
    #     FROM orders
    #     LEFT JOIN sales ON orders.order_id = sales.order_id
    #     GROUP BY orders.customer_id, orders.region, EXTRACT(YEAR FROM orders.order_date)
    # ),
def check_index(conn):
    cur = conn.cursor()

    query = """
    SELECT 
        t.relname as index_name,
        i.relname as table_name,
        pg_size_pretty(pg_relation_size(t.oid)) as size
    FROM pg_class t
    JOIN pg_class i ON t.oid = i.relfilenode
    WHERE t.relkind = 'i'
    AND i.relnamespace = (SELECT oid FROM pg_namespace WHERE nspname = 'public')
    ORDER BY pg_relation_size(t.oid) DESC;
    """

    result = pd.read_sql(query, conn)
    print(result)
def check_view(conn):
    cur = conn.cursor()
    query2 = """
SELECT 
    matviewname,
    pg_size_pretty(pg_total_relation_size('public.'||matviewname)) as size
FROM pg_matviews
WHERE schemaname = 'public'
ORDER BY pg_total_relation_size('public.'||matviewname) DESC;
"""

    result2 = pd.read_sql(query2, conn)
    print(result2)


def sample(conn):
    cur = conn.cursor()
    query = query = """ 
   
    EXPLAIN ANALYZE WITH orders_in_state AS(
        SELECT  orders.customer_id , COUNT(DISTINCT orders.state)
        FROM orders 
        GROUP BY orders.customer_id
        HAVING COUNT(DISTINCT orders.state) > 2
    ),
    avg_discount AS(
        SELECT orders.customer_id, AVG(sales.discount) as avg_disc
        FROM orders
        JOIN sales ON sales.order_id = orders.order_id
        GROUP BY orders.customer_id
        HAVING AVG(sales.discount) < ( SELECT AVG(sales.discount) as overall_avg
        FROM sales)
    ),
 
    prev_sales_temp AS(
        SELECT orders.customer_id, orders.region, SUM(sales.sales) as current_sale, 
            LAG(SUM(sales.sales)) OVER(PARTITION BY orders.customer_id ORDER BY EXTRACT(YEAR FROM orders.order_date)) AS prev_sales
        FROM orders
        LEFT JOIN sales ON orders.order_id = sales.order_id
        GROUP BY orders.customer_id, orders.region, EXTRACT(YEAR FROM orders.order_date)
    )

    SELECT orders_in_state.* ,  avg_discount
    FROM orders_in_state
    LEFT JOIN avg_discount
    ON avg_discount.customer_id = orders_in_state.customer_id
    LEFT JOIN prev_sales_temp
    ON prev_sales_temp.customer_id = orders_in_state.customer_id AND prev_sales_temp.prev_sales IS NOT NULL AND prev_sales_temp.prev_sales < prev_sales_temp.current_sale
   
 
    """   
    cur.execute(query)
    # result = pd.read_sql(query, conn)
    # print(result)
    result = cur.fetchall()      
    print("\n".join([row[0] for row in result]))

def get_customers(conn):
    cur = conn.cursor()
    q = """
   EXPLAIN ANALYZE CREATE  MATERIALIZED VIEW prev_sales_view AS
    SELECT orders.customer_id, orders.region, SUM(sales.sales) as current_sale, 
        LAG(SUM(sales.sales)) OVER(PARTITION BY orders.customer_id ORDER BY EXTRACT(YEAR FROM orders.order_date)) AS prev_sales
    FROM orders
    LEFT JOIN sales ON orders.order_id = sales.order_id
    GROUP BY orders.customer_id, orders.region, EXTRACT(YEAR FROM orders.order_date);
    
    """
    cur.execute(q)
    result = cur.fetchall()      
    print("\n".join([row[0] for row in result]))
    query = """ 
    EXPLAIN ANALYZE WITH orders_in_state AS(
        SELECT  orders.customer_id , COUNT(DISTINCT orders.state)
        FROM orders 
        GROUP BY orders.customer_id
        HAVING COUNT(DISTINCT orders.state) > 2
    ),
    avg_discount AS(
        SELECT orders.customer_id, AVG(sales.discount) as avg_disc
        FROM orders
        JOIN sales ON sales.order_id = orders.order_id
        GROUP BY orders.customer_id
        HAVING AVG(sales.discount) < ( SELECT AVG(sales.discount) as overall_avg
        FROM sales)
    ),
    prev_sales AS MATERIALIZED
   ( SELECT orders.customer_id, orders.region, SUM(sales.sales) as current_sale, 
        LAG(SUM(sales.sales)) OVER(PARTITION BY orders.customer_id ORDER BY EXTRACT(YEAR FROM orders.order_date)) AS prev_sales
    FROM orders
    LEFT JOIN sales ON orders.order_id = sales.order_id
    GROUP BY orders.customer_id, orders.region, EXTRACT(YEAR FROM orders.order_date))

    SELECT prev_sales_view.customer_id , prev_sales_view.region , prev_sales_view.current_sale , prev_sales_view.prev_sales
    FROM orders_in_state
    LEFT JOIN avg_discount ON avg_discount.customer_id= orders_in_state.customer_id
    LEFT JOIN prev_sales_view ON prev_sales_view.customer_id = orders_in_state.customer_id
    AND prev_sales_view.prev_sales IS NOT NULL 
    AND prev_sales_view.prev_sales < prev_sales_view.current_sale
    """
    cur.execute(query)
    # result = pd.read_sql(query, conn)
    # print(result)
    result = cur.fetchall()      
    print("\n".join([row[0] for row in result]))

conn = get_connection()
get_customers(conn)
print()
sample(conn)
# create_index(conn)
# delete_indexes(conn)
# check_index(conn)
# check_view(conn)