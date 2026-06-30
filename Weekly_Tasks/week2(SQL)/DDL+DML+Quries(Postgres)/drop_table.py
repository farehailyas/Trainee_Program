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

def drop_table(connection):
    cur = connection.cursor()
    query1 = """ DROP TABLE IF EXISTS products CASCADE
        """
    query2 = """ DROP TABLE IF EXISTS sales CASCADE
        """
    
    cur.execute(query1)
    cur.execute(query2)
    connection.commit()
    cur.close()
    print("sales table dropped")

connection = get_connection()
drop_table(connection)