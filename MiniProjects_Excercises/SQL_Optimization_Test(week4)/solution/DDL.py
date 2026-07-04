from db_connection import connect_db
import pandas as pd
def get_connection():
    try:
        conn = connect_db()
        return conn
    except Exception as e:
        print("cannot get connection")

def drop_table(conn):
        cur = conn.cursor()
        print("here to del table")
        q = """DROP TABLE olist_orders_datasetwith_partition """
        cur.execute(q)
        conn.commit()
        print("table deleted success")


def create_tables(conn):
    cur = conn.cursor()
    try:
        olist_orders_datasetwith_partition = """CREATE TABLE IF NOT EXISTS olist_orders_datasetwith_partition (
                order_id TEXT,
                customer_id TEXT ,
                order_status VARCHAR(20),
                order_purchase_timestamp TIMESTAMPTZ,
                order_approved_at TIMESTAMPTZ,
                order_delivered_timestamp TIMESTAMPTZ,
                order_estimated_delivery_date TIMESTAMPTZ,
                PRIMARY KEY(order_id ,order_purchase_timestamp)

        ) PARTITION BY RANGE (order_purchase_timestamp);

        CREATE TABLE partition_2016 PARTITION OF olist_orders_datasetwith_partition
                FOR VALUES FROM ('2016-01-01 00:00:00') TO ('2017-01-01 00:00:00');

        CREATE TABLE partition_2017 PARTITION OF olist_orders_datasetwith_partition
                FOR VALUES FROM ('2017-01-01 00:00:00') TO ('2018-01-01 00:00:00');
        
        CREATE TABLE partition_2018 PARTITION OF olist_orders_datasetwith_partition
                FOR VALUES FROM ('2018-01-01 00:00:00') TO ('2019-01-01 00:00:00');

        """ 
        olist_orders_dataset = """CREATE TABLE IF NOT EXISTS olist_orders_dataset (
                order_id TEXT PRIMARY KEY,
                customer_id TEXT ,
                order_status VARCHAR(20),
                order_purchase_timestamp TIMESTAMPTZ,
                order_approved_at TIMESTAMPTZ,
                order_delivered_timestamp TIMESTAMPTZ,
                order_estimated_delivery_date TIMESTAMPTZ
        ) """
        olist_products_dataset = """CREATE TABLE IF NOT EXISTS olist_products_dataset(
                product_id TEXT PRIMARY KEY,
                product_category_name TEXT,
                product_name_length TEXT,
                product_description_lenght TEXT,
                product_photos_qty TEXT,
                product_weight_g DECIMAL(10,2),      
                product_length_cm DECIMAL(10,2),    
                product_height_cm DECIMAL(10,2),     
                product_width_cm DECIMAL(10,2) 
        )"""
        olist_order_items_dataset ="""CREATE TABLE IF NOT EXISTS olist_order_items_dataset(
                items_id SERIAL PRIMARY KEY,
                order_id TEXT,
                order_purchase_timestamp TIMESTAMPTZ,
                order_item_id INTEGER ,
                product_id TEXT,
                seller_id TEXT,
                shipping_limit_date TIMESTAMPTZ,
                price DECIMAL(10,2),
                freight_value DECIMAL(10,2),
                FOREIGN KEY (order_id , order_purchase_timestamp) REFERENCES olist_orders_datasetwith_partition(order_id, order_purchase_timestamp),
                FOREIGN KEY (product_id) REFERENCES olist_products_dataset(product_id)
        )"""
       
        olist_order_payments_dataset = """CREATE TABLE IF NOT EXISTS olist_order_payments_dataset(
                payment_id SERIAL PRIMARY KEY ,
                order_id TEXT,
                order_purchase_timestamp TIMESTAMPTZ,
                payment_sequential INTEGER,
                payment_type TEXT,
                payment_installments INTEGER,
                payment_value DECIMAL(10,2),
                FOREIGN KEY (order_id, order_purchase_timestamp) REFERENCES olist_orders_datasetwith_partition(order_id ,order_purchase_timestamp)
        )""" 
        olist_order_customer_dataset = """CREATE TABLE IF NOT EXISTS olist_order_customer_dataset(
                customer_id TEXT PRIMARY KEY,
                customer_unique_id TEXT,
                customer_zip_code_prefix TEXT,
                customer_city TEXT,
                customer_state TEXT
        )"""
        cur.execute(olist_orders_datasetwith_partition)
        cur.execute(olist_orders_dataset)
        cur.execute(olist_products_dataset)
        cur.execute(olist_order_items_dataset)
        cur.execute(olist_order_payments_dataset)
        cur.execute(olist_order_customer_dataset)

        conn.commit()
    except Exception as e:
        print(f"cannot create table {e}")

def read_table(conn):
    cur = conn.cursor()
    print('reading olist_orders')
    q = """SELECT * 
        FROM olist_products_dataset
        """
    result = pd.read_sql(q,conn)
    print(result)

conn = get_connection()
create_tables(conn)
# read_table(conn)
# drop_table(conn)