import pandas as pd
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from db_connection import get_dbConnection

def get_connection():    
    try:
        conn = get_dbConnection()
        print("Connected to db")
        return conn
    except Exception as e:
        print(e)

"""  
 Q6: This query answers: "List all states sorted alphabetically"
# Topics: SELECT, ORDER BY, DISTINCT
# Expected: state (sorted A-Z, no duplicates)
"""
def get_sales(conn):
    query = """SELECT DISTINCT state
            FROM orders
            ORDER BY state
    
        """
    result = pd.read_sql(query, conn)
    print(result)

conn = get_connection()
get_sales(conn)
