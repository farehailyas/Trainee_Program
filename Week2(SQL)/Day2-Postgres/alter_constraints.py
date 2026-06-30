import pandas as pd
from db_connection import get_dbConnection
 
# Get connection (auto-creates database)
def get_connection():    
    try:
        conn = get_dbConnection()
        print("Connected to db")
        return conn
    except Exception as e:
        print(e)

def alter_constraint_orders(connection):
    cur = connection.cursor()
    query1 = """ALTER TABLE orders
            ALTER COLUMN  Order_Date SET NOT NULL;
        """
    query2 = """ALTER TABLE orders
            ALTER COLUMN  Ship_Date SET NOT NULL;
        """
    query3 = """ALTER TABLE orders
            ALTER COLUMN  Customer_Id SET NOT NULL;
        """
    cur.execute(query1)
    cur.execute(query2)
    cur.execute(query3)
    connection.commit()
    cur.close()
    print("alter constraints for orders tables")


def alter_constraint_sales(connection):
    cur = connection.cursor()
    query1 = """ALTER TABLE sales
            ALTER COLUMN  discount SET NOT NULL;
        """
    query2 = """ALTER TABLE sales
            ALTER COLUMN  profit SET NOT NULL;
        """
    query3 = """ALTER TABLE sales
            ALTER COLUMN  sales SET NOT NULL;
        """
    query4 = """ALTER TABLE sales
            ALTER COLUMN  Order_Id SET NOT NULL;
        """
    query5 = """ALTER TABLE sales
            ALTER COLUMN  Product_Id SET NOT NULL;
        """
    cur.execute(query1)
    cur.execute(query2)
    cur.execute(query3)
    cur.execute(query4)
    cur.execute(query5)
    connection.commit()
    cur.close()
    print("alter constraints of sales tables")

connection = get_connection()
alter_constraint_orders(connection)
alter_constraint_sales(connection)