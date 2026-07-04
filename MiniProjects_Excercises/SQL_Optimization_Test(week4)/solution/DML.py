from db_connection import connect_db
import pandas as pd

def get_connection():
    try:
        conn = connect_db()
        return conn
    except Exception as e:
        print("cannot get connection")



def orders_dataset(conn):
    cur = conn.cursor()
    data = pd.read_csv("data/olist_orders_dataset.csv" , encoding='latin1')
    orders = data[["order_id","customer_id","order_status","order_purchase_timestamp","order_approved_at",
    "order_delivered_customer_date","order_estimated_delivery_date" ]].drop_duplicates()

    # converting timestamp col to datetime data type as striing cant be directly converted into timestampz
    time_cols = ["order_purchase_timestamp","order_approved_at",
    "order_delivered_customer_date","order_estimated_delivery_date"]
    for i in time_cols:
        orders[i] = pd.to_datetime(orders[i], errors='coerce')


    orders = orders.astype(object).where(pd.notna(orders), None)
    
    for ind , row in orders.iterrows():
        q = """INSERT INTO olist_orders_datasetwith_partition (order_id, customer_id, order_status, order_purchase_timestamp, 
        order_approved_at, order_delivered_timestamp, order_estimated_delivery_date) VALUES(%s,%s,%s,%s,%s,%s,%s)"""      
        cur.execute(q , tuple(row))
    conn.commit()
    print("data inserted into orders successfulyy")


def products_dataset(conn):
    cur = conn.cursor()
    data = pd.read_csv("data/olist_products_dataset.csv" , encoding='latin1')
    products = data[["product_id","product_category_name","product_name_lenght","product_description_lenght",
    "product_photos_qty","product_weight_g","product_length_cm","product_height_cm","product_width_cm"]].drop_duplicates()

    products = products.fillna(value=None)

    for ind , row in products.iterrows():
        q = """INSERT INTO olist_products_dataset ( product_id , product_category_name ,product_name_length ,
            product_description_lenght ,product_photos_qty ,product_weight_g , product_length_cm  ,product_height_cm ,
            product_width_cm ) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"""      
        cur.execute(q , tuple(row))
    conn.commit()
    print("data inserted into products successfulyy")

def order_items(conn):
    cur = conn.cursor()
    data = pd.read_csv("data/olist_order_items_dataset.csv" , encoding='latin1')
    purchase_timestamp = pd.read_csv("data/olist_orders_dataset.csv" , encoding='latin1')

    purchase_timestamp = purchase_timestamp[['order_id','order_purchase_timestamp']].drop_duplicates()
   
    order_items = data[["order_id","order_item_id","product_id","seller_id","shipping_limit_date","price","freight_value"]].drop_duplicates()

    purchase_timestamp['order_purchase_timestamp'] = pd.to_datetime(purchase_timestamp['order_purchase_timestamp'], errors='coerce')

    order_items = order_items.merge(purchase_timestamp, on='order_id', how='left')
    order_items = order_items[["order_id", "order_purchase_timestamp", "order_item_id", "product_id", "seller_id", "shipping_limit_date", "price", "freight_value"]]

    order_items['order_purchase_timestamp'] = order_items['order_purchase_timestamp'].astype(str)

    for ind , row in order_items.iterrows():
        q = """INSERT INTO olist_order_items_dataset (order_id,order_purchase_timestamp,order_item_id,product_id,seller_id,shipping_limit_date,price,freight_value) 
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"""      
        cur.execute(q , tuple(row))
    conn.commit()
    print("data inserted into order items successfulyy")



def payment(conn):
    cur = conn.cursor()
    data = pd.read_csv("data/olist_order_payments_dataset.csv" , encoding='latin1')
    purchase_timestamp = pd.read_csv("data/olist_orders_dataset.csv" , encoding='latin1')
    purchase_timestamp = purchase_timestamp[['order_id','order_purchase_timestamp']].drop_duplicates()
    
    payment = data[["order_id","payment_sequential","payment_type","payment_installments","payment_value"]].drop_duplicates()

   
    purchase_timestamp['order_purchase_timestamp'] = pd.to_datetime(purchase_timestamp['order_purchase_timestamp'], errors='coerce')

    payment = payment.merge(purchase_timestamp, on='order_id', how='left')
    payment = payment[["order_id","order_purchase_timestamp","payment_sequential","payment_type","payment_installments","payment_value"]]

    payment['order_purchase_timestamp'] = payment['order_purchase_timestamp'].astype(str)

    for ind , row in payment.iterrows():
        q = """INSERT INTO olist_order_payments_dataset (order_id, order_purchase_timestamp ,payment_sequential,payment_type,payment_installments,payment_value) 
        VALUES(%s,%s,%s,%s,%s,%s)"""      
        cur.execute(q , tuple(row))
    conn.commit()
    print("data inserted into payment successfulyy")

def customer_order(conn):
    cur = conn.cursor()
    data = pd.read_csv("data/olist_customers_dataset.csv" , encoding='latin1')
    customer_order = data[["customer_id","customer_unique_id","customer_zip_code_prefix","customer_city","customer_state"]].drop_duplicates()

    customer_order = customer_order.fillna(value=None)

    for ind , row in customer_order.iterrows():
        q = """INSERT INTO olist_order_customer_dataset (customer_id,customer_unique_id,customer_zip_code_prefix,customer_city,customer_state) 
        VALUES(%s,%s,%s,%s,%s)"""      
        cur.execute(q , tuple(row))
    conn.commit()
    print("data inserted into customer_order successfulyy")


conn = get_connection()
# orders_dataset(conn)
# products_dataset(conn)
# order_items(conn)
payment(conn)
customer_order(conn)