from db_connection import connect_db
import pandas as pd

def get_connection():
    try:
        conn = connect_db()
        return conn
    except Exception as e:
        print("cannot get connection")

"""self join have complexity of O(n*n) which is about 9.8 billion operations, the query runs for an hour an timed out."""
def self_join(conn):
    cur = conn.cursor()
    # print("running subqury")
    query = """SELECT o1.order_id,
            (o1.order_delivered_timestamp::DATE - o1.order_approved_at::DATE) as current_customer_delivery_days,
            (o2.order_delivered_timestamp::DATE - o2.order_approved_at::DATE) as prev_customer_delivery_days
        FROM olist_orders_datasetwith_partition o1
        INNER JOIN olist_order_customer_dataset c1 ON c1.customer_id = o1.customer_id
        INNER JOIN olist_orders_datasetwith_partition o2 
        ON o1.order_delivered_timestamp::DATE = o2.order_delivered_timestamp::DATE
        AND o2.order_delivered_timestamp < o1.order_delivered_timestamp
        INNER JOIN olist_order_customer_dataset c2 ON c2.customer_id = o2.customer_id
        
        AND c1.customer_state = c2.customer_state
        
        WHERE (o1.order_delivered_timestamp::DATE - o1.order_approved_at::DATE) > 
            (o2.order_delivered_timestamp::DATE - o2.order_approved_at::DATE)
            AND o2.order_delivered_timestamp = (
            SELECT MAX(temp.order_delivered_timestamp)
            FROM olist_orders_datasetwith_partition temp
            WHERE temp.order_delivered_timestamp < o1.order_delivered_timestamp
            AND temp.order_delivered_timestamp::DATE = o1.order_delivered_timestamp::DATE
            AND temp.customer_id IN (SELECT customer_id FROM olist_order_customer_dataset WHERE customer_state = c1.customer_state)
        )
        ORDER BY o1.order_delivered_timestamp
    """
    result = pd.read_sql(query , conn)
    print(result)
    # cur.execute(query)
    # result = cur.fetchall()      
    # print("\n".join([row[0] for row in result]))

""" window function have linear comlexity and does single pass over the data which reduce the cost to execute query."""

def window_function(conn):
    cur = conn.cursor()
    query = """ WITH customer_delivery_days AS (SELECT o.order_id, LAG(o.order_delivered_timestamp::DATE - o.order_approved_at::DATE) 
                OVER(PARTITION BY c.customer_state , o.order_delivered_timestamp::DATE  ORDER BY o.order_delivered_timestamp) as prev_customer_delivery_days 
                ,(o.order_delivered_timestamp::DATE - o.order_approved_at::DATE) as current_customer_delivery_days 
                FROM olist_orders_datasetwith_partition o
                JOIN olist_order_customer_dataset c
                ON c.customer_id = o.customer_id)
            SELECT *
            FROM customer_delivery_days
            WHERE prev_customer_delivery_days IS NOT NULL 
            AND current_customer_delivery_days > prev_customer_delivery_days
    """
    result = pd.read_sql(query , conn)
    print(result)
    # cur.execute(query)
    # result = cur.fetchall()      
    # print("\n".join([row[0] for row in result]))

conn = get_connection()
# self_join(conn)
window_function(conn)
