import pandas as pd
import sys
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')
sys.path.append(str(Path(__file__).parent.parent))
from db_connection import get_dbConnection

def inventory(conn):
    print(" \n===============Table: Inventory ==============")
    query = """ 
           ( SELECT 'oldest' as type, *
            FROM inventory
            ORDER BY inserted_at
            LIMIT 1)
            
            UNION ALL

           ( SELECT 'newest' as type, *
            FROM inventory
            ORDER BY inserted_at DESC
            LIMIT 1)
            
        """

    result = pd.read_sql(query, conn)
    print(result)

def product_pricing(conn):
    print(" \n===============Table: Product Pricing==============")
    query = """ 
           ( SELECT 'oldest' as type, *
            FROM product_pricing
            ORDER BY inserted_at
            LIMIT 1)
            
            UNION ALL

           ( SELECT 'newest' as type, *
            FROM product_pricing
            ORDER BY inserted_at DESC
            LIMIT 1)
            
        """

    result = pd.read_sql(query, conn)
    print(result)

def amazon_sales(conn):
    print(" \n===============Table: Amazon sales==============")
    query = """ 
           ( SELECT 'oldest' as type, *
            FROM amazon_sales
            ORDER BY inserted_at
            LIMIT 1)
            
            UNION ALL

           ( SELECT 'newest' as type, *
            FROM amazon_sales
            ORDER BY inserted_at DESC
            LIMIT 1)
            
        """

    result = pd.read_sql(query, conn)
    print(result)

def international_sales(conn):
    print(" \n===============Table: International sales==============")
    query = """ 
           ( SELECT 'oldest' as type, *
            FROM international_sales
            ORDER BY inserted_at
            LIMIT 1)
            
            UNION ALL

           ( SELECT 'newest' as type, *
            FROM international_sales
            ORDER BY inserted_at DESC
            LIMIT 1)
            
        """

    result = pd.read_sql(query, conn)
    print(result)

def warehouse_comparison(conn):
    print(" \n===============Table: Warehouse comparison==============")
    query = """ 
           ( SELECT 'oldest' as type, *
            FROM warehouse_comparison
            ORDER BY inserted_at
            LIMIT 1)
            
            UNION ALL

           ( SELECT 'newest' as type, *
            FROM warehouse_comparison
            ORDER BY inserted_at DESC
            LIMIT 1)
            
        """

    result = pd.read_sql(query, conn)
    print(result)

def expenses(conn):
    print(" \n===============Table: Expenses==============")
    query = """ 
           ( SELECT 'oldest' as type, *
            FROM expenses
            ORDER BY inserted_at
            LIMIT 1)
            
            UNION ALL

           ( SELECT 'newest' as type, *
            FROM expenses
            ORDER BY inserted_at DESC
            LIMIT 1)
            
        """

    result = pd.read_sql(query, conn)
    print(result)


# join bw order and sales
def check_freshness(conn):
    print("\n ======================= Checking Freshness=============================")
    inventory(conn)
    product_pricing(conn)
    amazon_sales(conn)
    international_sales(conn)
    warehouse_comparison(conn)
    expenses(conn)
