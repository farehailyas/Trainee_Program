from db_connection import connect_db
import pandas as pd

def get_connection():
    try:
        conn = connect_db()
        return conn
    except Exception as e:
        print("cannot get connection")

conn = get_connection()
def create_index(conn):
    cur = conn.cursor()
    query = """CREATE INDEX idx_items_order_id ON olist_order_items_dataset(order_id) """
    cur.execute(query)
    conn.commit()
    cur.close()
    print("Index created")

def get_year(conn):
    cur = conn.cursor()
    
    query =  """SELECT EXTRACT(YEAR FROM olist_orders_dataset.order_purchase_timestamp) , COUNT(*) as count_data
                FROM olist_orders_dataset
                GROUP BY EXTRACT(YEAR FROM olist_orders_dataset.order_purchase_timestamp) 
                """
    result = pd.read_sql(query , conn)
    print(result)
    # cur.execute(query)
    # result = cur.fetchall()      
    # print("\n".join([row[0] for row in result]))

"""Current situation : have 100k records , and data is of 3 years , make yearly partitions to get data in years.
After that the performance bottleneck was nesting during joining order_items and order table , so indexed inner table(order_items) on join key and 
products table to find category which reduces the cost to 0.01 seconds  """

"""Future situation : If the data has to grow upto 1M then we will create monthly partitions , to find revevnue of specific month does not need to 
scan all over the data, even if query runs daily it will only retrive records from that specific month .
and then we can store monthly data into some aggregated table which will be used for further processing """
def get_monthly_report(conn):
    cur = conn.cursor()

    # before partition and indexing
    # query =  """EXPLAIN ANALYZE SELECT SUM(olist_order_items_dataset.price) as total_revenue , COUNT(olist_orders_dataset.order_id) as total_orders 
    #             FROM olist_orders_dataset
    #             LEFT JOIN olist_order_items_dataset
    #             ON olist_orders_dataset.order_id = olist_order_items_dataset.order_id
    #             LEFT JOIN olist_products_dataset
    #             ON olist_products_dataset.product_id = olist_order_items_dataset.product_id
    #             WHERE olist_orders_dataset.order_status = 'delivered'
    #             GROUP BY olist_products_dataset.product_category_name  , EXTRACT(MONTH FROM olist_orders_dataset.order_purchase_timestamp) 
    #             """
    # result = pd.read_sql(query , conn)
    # print(result)
    
    query = """ SELECT olist_products_dataset.product_category_name , SUM(olist_order_items_dataset.price) as total_revenue , 
                COUNT(olist_orders_datasetwith_partition.order_id) as total_orders , 
                EXTRACT(MONTH FROM olist_orders_datasetwith_partition.order_purchase_timestamp) as month
                FROM olist_orders_datasetwith_partition
                LEFT JOIN olist_order_items_dataset
                ON olist_orders_datasetwith_partition.order_id = olist_order_items_dataset.order_id
                LEFT JOIN olist_products_dataset
                ON olist_products_dataset.product_id = olist_order_items_dataset.product_id
                WHERE olist_orders_datasetwith_partition.order_status = 'delivered' AND (olist_orders_datasetwith_partition.order_purchase_timestamp >= '2016-01-01' AND olist_orders_datasetwith_partition.order_purchase_timestamp < '2019-01-01')
                GROUP BY olist_products_dataset.product_category_name  , EXTRACT(MONTH FROM olist_orders_datasetwith_partition.order_purchase_timestamp) 
                ORDER BY month ,  olist_products_dataset.product_category_name  
            """

    # query = """ SELECT olist_products_dataset.product_category_name , COUNT(*) as count
    #             FROM olist_products_dataset
    #             GROUP BY olist_products_dataset.product_category_name  
    #         """
    
    result = pd.read_sql(query , conn)
    print(result)

    # cur.execute(query)
    # result = cur.fetchall()      
    # print("\n".join([row[0] for row in result]))

get_monthly_report(conn)
# get_year(conn)
# create_index(conn)