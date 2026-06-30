import pandas as pd
from db_connection import get_dbConnection

def get_connection():    
    try:
        conn = get_dbConnection()
        print("Connected to db")
        return conn
    except Exception as e:
        print(e)

def insert_data(connection):
    df = pd.read_csv("Sample - Superstore.csv", encoding='latin1')
    cur = connection.cursor()
    
    customers = df[['Customer ID','Customer Name','Segment']].drop_duplicates()
    for idx, row in customers.iterrows():
        cur.execute("INSERT INTO customers VALUES (%s,%s,%s) ON CONFLICT DO NOTHING", tuple(row))

    products = df[['Product ID','Product Name','Category','Sub-Category']].drop_duplicates()
    for idx, row in products.iterrows():
        cur.execute("INSERT INTO products VALUES (%s,%s,%s,%s) ON CONFLICT DO NOTHING", tuple(row))

    orders = df[['Order ID','Order Date','Ship Date','Ship Mode','Region','State','City','Country','Customer ID']].drop_duplicates()
    for idx, row in orders.iterrows():
        cur.execute("INSERT INTO orders VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING", tuple(row))

    order_items = df[['Order ID','Product ID','Sales','Quantity','Discount','Profit']]
    for idx, row in order_items.iterrows():
        cur.execute("INSERT INTO sales (order_id,product_id,sales,quantity,discount,profit) VALUES (%s,%s,%s,%s,%s,%s)", tuple(row))
    
    connection.commit()
    print("data inserted successfully")

connection = get_connection()
insert_data(connection)