"""Find product name and category for each sale record"""

import pandas as pd
import sqlite3
import time

connection = sqlite3.Connection("SuperstoreDb.db")
cur = connection.cursor()

query = """ SELECT  Name , Category 
        FROM Products p 
        LEFT JOIN Sales s ON s.Product_Id = p.Product_Id
"""


print("TEST 1: WITHOUT INDEX")
start = time.time()
res1 = pd.read_sql(query, connection)
time1 = time.time() - start
print(f"Time: {time1 * 1000:.2f} ms")
print(f"Rows: {len(res1)}\n")
# cur.execute("DROP INDEX idx_sales_product")
# cur.execute("DROP INDEX idx_products_id")
# connection.commit()

print("Indexes deleted!")
# conn.close()

# # TEST 2: WITH INDEX
print("TEST 2: WITH INDEX")
cur.execute("CREATE INDEX idx_sales_product ON Sales(Product_Id)")
cur.execute("CREATE INDEX idx_products_id ON Products(Product_Id)")
connection.commit()
 
start = time.time()
res2 = pd.read_sql(query, connection)
time2 = time.time() - start
print(f"Time: {time2 * 1000:.2f} ms")
print(f"Rows: {len(res2)}\n")