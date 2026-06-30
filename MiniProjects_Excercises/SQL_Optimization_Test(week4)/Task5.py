from db_connection import connect_db
import pandas as pd

def get_connection():
    try:
        conn = connect_db()
        return conn
    except Exception as e:
        print("cannot get connection")

conn = get_connection()
"""Data types : month is INT as it is between 1-12
    product_category_name is text as it can be of variable length 
    total_revevnue and avg_freight  is decimal as precision is necessary
    total_orders is BIGINT as count of orders can grow uptoo millions"""

def create_table(conn):
    cur = conn.cursor()

    query = """CREATE TABLE monthly_category_revenue (
            month INT,
            product_category_name TEXT,
            total_revenue  DECIMAL(10,2),
            total_orders BIGINT, 
            avg_freight DECIMAL(10,2) ,
            PRIMARY KEY(month , product_category_name) 
    )"""
   
    cur.execute(query)
    conn.commit()
    print("table created")
    # query = """ DROP TABLE monthly_category_revenue"""
    # cur.execute(query)
    # conn.commit()
    # print("table DELETED")
    # result = pd.read_sql(query, conn)
    # print(result)

"""DML Is idempotent as it updates already existing records and add new records that donot exist previously
ensuring no duplicates and update existing record"""
def insert_data(conn):
    cur = conn.cursor()
    query = """ WITH monthly_report AS (SELECT EXTRACT(MONTH FROM olist_orders_datasetwith_partition.order_purchase_timestamp) as month, 
                olist_products_dataset.product_category_name , SUM(olist_order_items_dataset.price) as total_revenue , 
                COUNT(olist_orders_datasetwith_partition.order_id) as total_orders , AVG(olist_order_items_dataset.freight_value) AS avg_freight
                FROM olist_orders_datasetwith_partition
                LEFT JOIN olist_order_items_dataset
                ON olist_orders_datasetwith_partition.order_id = olist_order_items_dataset.order_id
                LEFT JOIN olist_products_dataset
                ON olist_products_dataset.product_id = olist_order_items_dataset.product_id
                WHERE olist_orders_datasetwith_partition.order_status = 'delivered' AND (olist_orders_datasetwith_partition.order_purchase_timestamp >= '2017-01-01' AND olist_orders_datasetwith_partition.order_purchase_timestamp < '2019-01-01')
                GROUP BY olist_products_dataset.product_category_name  , EXTRACT(MONTH FROM olist_orders_datasetwith_partition.order_purchase_timestamp) 
                ORDER BY month ,  olist_products_dataset.product_category_name  )

                INSERT INTO monthly_category_revenue (month,product_category_name,total_revenue,total_orders,avg_freight)
                SELECT * FROM monthly_report
                ON CONFLICT (month, product_category_name) 
                DO UPDATE SET 
                total_revenue = EXCLUDED.total_revenue,
                total_orders = EXCLUDED.total_orders,
                avg_freight = EXCLUDED.avg_freight;
        """
    cur.execute(query,conn)
    conn.commit()
    print("monthly revenue data inserted")
    # result = pd.read_sql(query,conn)
    # print(result)
"""Index is created on month as the retrival is most likely on month , when table grows to million , index would be helpful if 
retreiving records of specific month""" 
def create_index(conn):

    cur=conn.cursor()
    query = """CREATE INDEX idx_month ON monthly_category_revenue(month)"""
    cur.execute(query,conn)
    conn.commit()
    print("Index created")

def read_data(conn):
    cur = conn.cursor()

    query = """SELECT *
            FROM monthly_category_revenue
    """
    result = pd.read_sql(query,conn)
    print(result)

# create_table(conn)
# insert_data(conn)
create_index(conn)
# read_data(conn)