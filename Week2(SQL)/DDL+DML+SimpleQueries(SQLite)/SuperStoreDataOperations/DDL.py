
import sqlite3

connection = sqlite3.Connection("SuperstoreDb.db")
cur = connection.cursor()
cur.execute("PRAGMA foreign_keys = ON")

customers = """CREATE TABLE IF NOT EXISTS Customers(
        Customer_Id TEXT PRIMARY KEY,
        Name TEXT,
        Segment TEXT
    )
"""
orders = """CREATE TABLE IF NOT EXISTS Orders(
        Order_Id TEXT PRIMARY KEY,
        Order_Date DATE,
        Ship_Date DATE,
        Ship Mode TEXT,
        City TEXT,
        Country TEXT,
        State TEXT,
        Region TEXT,
        Customer_Id TEXT,
        FOREIGN KEY (Customer_Id) REFERENCES Customers(Customer_Id) 
    )
"""
products = """CREATE TABLE IF NOT EXISTS Products(
        Product_Id TEXT PRIMARY KEY,
        Name ,
        Category,
        SubCategory
    ) 
"""
sales = """CREATE TABLE IF NOT EXISTS Sales(
        Sales_Id INTEGER PRIMARY KEY AUTOINCREMENT,
        sales REAL,
        quantity INTEGER,
        discount REAL,
        profit REAL,
        Order_Id TEXT,
        Product_Id TEXT,
        FOREIGN KEY (Order_Id) REFERENCES Orders(Order_Id) 
        FOREIGN KEY (Product_Id) REFERENCES Products(Product_Id) 
    )
"""
cur.execute(customers)
cur.execute(orders)
cur.execute(products)
cur.execute(sales)
print("All Tables created")

cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
print(cur.fetchall())

# cur.execute("PRAGMA table_info(orders)")
# print(cur.fetchall())

cur.execute("PRAGMA foreign_key_list(orders)")
print(cur.fetchall())