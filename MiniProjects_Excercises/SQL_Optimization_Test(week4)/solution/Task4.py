
from db_connection import connect_db
import pandas as pd

def get_connection():
    try:
        conn = connect_db()
        return conn
    except Exception as e:
        print("cannot get connection")

conn = get_connection()

""" union operation handles deduplication using sort operation, it sorts results from both select statements and then remove duplicates 
    so sorting overhead is added which is overhead in performance.
applying filter outside is wastefull as it combine data for all types of statements first and then extract the required type.
"""

def union(conn):
    cur = conn.cursor()
    query = """EXPLAIN ANALYZE WITH individual_payment AS(
                    SELECT olist_order_payments_dataset.payment_type ,olist_orders_datasetwith_partition.order_id , 
                    olist_order_payments_dataset.order_purchase_timestamp
                    FROM olist_orders_datasetwith_partition 
                    LEFT JOIN olist_order_payments_dataset 
                    ON olist_orders_datasetwith_partition.order_id = olist_order_payments_dataset.order_id
                   
                    UNION 
                   
                    SELECT olist_order_payments_dataset.payment_type ,olist_orders_datasetwith_partition.order_id , 
                    olist_order_payments_dataset.order_purchase_timestamp
                    FROM olist_orders_datasetwith_partition 
                    LEFT JOIN olist_order_payments_dataset 
                    ON olist_orders_datasetwith_partition.order_id = olist_order_payments_dataset.order_id
                ) 
                SELECT payment_type , COUNT(DISTINCT order_id) AS count 
                FROM individual_payment
                WHERE payment_type IN ('credit_card' , 'boleto')  
                AND order_purchase_timestamp >= '2018-01-01' AND order_purchase_timestamp < '2019-01-01'
                GROUP BY payment_type
     """

    result = pd.read_sql(query , conn)
    print(result)
    # cur.execute(query)
    # result = cur.fetchall()      
    # print("\n".join([row[0] for row in result]))

"""Union all operator remove this overhead of sorting and just combine rows from both tables """

"""Approach is applying filter before grouping data which reduce the data before grouping it """
 
def union_anti_pattern(conn):
    query = """EXPLAIN ANALYZE SELECT olist_order_payments_dataset.payment_type , COUNT(DISTINCT olist_orders_datasetwith_partition.order_id)
                FROM olist_orders_datasetwith_partition 
                LEFT JOIN olist_order_payments_dataset 
                ON olist_orders_datasetwith_partition.order_id = olist_order_payments_dataset.order_id
                WHERE olist_order_payments_dataset.payment_type IN ('credit_card' , 'boleto')  
                AND (olist_order_payments_dataset.order_purchase_timestamp >= '2018-01-01' 
                AND olist_order_payments_dataset.order_purchase_timestamp < '2019-01-01')
                GROUP BY olist_order_payments_dataset.payment_type
     """
    result = pd.read_sql(query , conn)
    print(result)
    # cur.execute(query)
    # result = cur.fetchall()      
    # print("\n".join([row[0] for row in result]))

union(conn)
union_anti_pattern(conn)
# get_year(conn)
# create_index(conn)