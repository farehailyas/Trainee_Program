import pandas as pd
from db_connection import get_dbConnection

def get_connection():    
    try:
        conn = get_dbConnection()
        print("Connected to db")
        return conn
    except Exception as e:
        print(e)
    
def create_tables(connection):
    try:
        cur = connection.cursor()
        
        customers = """CREATE TABLE IF NOT EXISTS customers(
                customer_id TEXT PRIMARY KEY,
                customer_name TEXT,
                segment TEXT
            )
        """
        products = """CREATE TABLE IF NOT EXISTS products(
                product_id TEXT PRIMARY KEY,
                product_name TEXT,
                category TEXT,
                sub_category TEXT
            ) 
        """
        orders = """CREATE TABLE IF NOT EXISTS orders(
                order_id TEXT PRIMARY KEY,
                order_date DATE,
                ship_date DATE,
                ship_mode TEXT,
                region TEXT,
                state TEXT,
                city TEXT,
                country TEXT,
                customer_id TEXT,
                FOREIGN KEY (customer_id) REFERENCES customers(customer_id) 
            )
        """
        sales = """CREATE TABLE IF NOT EXISTS sales(
                sales_id SERIAL PRIMARY KEY,
                order_id TEXT,
                product_id TEXT,
                sales REAL,
                quantity INTEGER,
                discount REAL,
                profit REAL,
                FOREIGN KEY (order_id) REFERENCES orders(order_id),
                FOREIGN KEY (product_id) REFERENCES products(product_id) 
            )
        """
        cur.execute(customers)
        cur.execute(products)
        cur.execute(orders)
        cur.execute(sales)
        connection.commit()
        print("tables created successfully")
    except Exception as e:
        print("Error:", e)

connection = get_connection()
create_tables(connection)