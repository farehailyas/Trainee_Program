import pandas as pd
import sqlite3

df = pd.read_csv("Sample - Superstore.csv" , encoding = 'latin1')
print(df.info())

connection = sqlite3.Connection("SuperstoreDb.db")
cur = connection.cursor()

# insert data from csv to tables
# --- Insert Data ---
customers = df[['Customer ID','Customer Name','Segment']].drop_duplicates()
for idx, row in customers.iterrows():
    cur.execute("INSERT OR IGNORE INTO customers VALUES (?,?,?)", tuple(row))

products = df[['Product ID','Product Name','Category','Sub-Category']].drop_duplicates()
for idx, row in products.iterrows():
    cur.execute("INSERT OR IGNORE INTO products VALUES (?,?,?,?)", tuple(row))

orders = df[['Order ID','Order Date','Ship Date','Ship Mode','Region','State','City' , 'Country' ,'Customer ID']].drop_duplicates()
for idx, row in orders.iterrows():
    cur.execute("INSERT OR IGNORE INTO orders VALUES (?,?,?,?,?,?,?,?,?)", tuple(row))

order_items = df[['Order ID','Product ID','Sales','Quantity','Discount','Profit']]
for idx, row in order_items.iterrows():
    cur.execute("INSERT INTO sales (order_id,product_id,sales,quantity,discount,profit) VALUES (?,?,?,?,?,?)", tuple(row))
connection.commit()
print("data inserted successully")

# query_to_read = """SELECT * FROM orders WHERE Order_Id In( "CA-2016-152156" , "CA-2016-138688" ) """ 
# result = cur.execute(query_to_read)
# for i in result:
#     print(f"data in order : {i}")
import time
start = time.time()
df = pd.read_sql("SELECT * FROM products", connection)
end = time.time()
print("time to execute products")
print((end - start) *1000)
# print(df)  # clean table format



start1= time.time()
df = pd.read_sql("SELECT * FROM customers", connection)
end1 = time.time()
print("time to execute customers")
print((end1 - start1) *1000)
# print(df)  # clean table form