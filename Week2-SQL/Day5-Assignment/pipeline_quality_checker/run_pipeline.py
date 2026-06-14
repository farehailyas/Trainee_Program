import pandas as pd
import sys
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')
sys.path.append(str(Path(__file__).parent.parent))
from db_connection import get_dbConnection
from check_duplicates import get_duplicates
from check_null import get_null_coloumns 
from check_refrential_integrity import check_refrential_integrity
from check_freshness import check_freshness


def get_connection():    
    try:
        conn = get_dbConnection()
        print("Connected to db")
        return conn
    except Exception as e:
        print(e)


# join bw order and sales

def run(conn):
   get_duplicates(conn)
   get_null_coloumns(conn)
   check_refrential_integrity(conn)
   check_freshness(conn)



conn = get_connection()
run(conn)
