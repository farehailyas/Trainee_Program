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


# join bw order and sales

def get_duplicates(conn):
    print("Get Duplicates")
    query = """ SELECT 'Inventory' as table_name , COUNT(*) as duplicates 
                FROM (SELECT sku_code
                    FROM inventory 
                    GROUP BY sku_code
                    HAVING COUNT(*) > 1)

                UNION ALL

                SELECT 'Product Pricing' as table_name , COUNT(*) as duplicates 
                FROM (SELECT sku
                    FROM product_pricing 
                    GROUP BY sku
                    HAVING COUNT(*) > 1)
                
                UNION ALL

                SELECT 'Amazon Sales' as table_name , COUNT(*) as duplicates 
                FROM (SELECT order_id
                    FROM amazon_sales 
                    GROUP BY order_id
                    HAVING COUNT(*) > 1)
                

                UNION ALL 

                SELECT 'International Sales' as table_name , COUNT(*) as duplicates 
                FROM (SELECT date, customer, sku, size
                    FROM international_sales  
                    GROUP BY date, customer, sku, size
                    HAVING COUNT(*) > 1)

                UNION ALL

                SELECT 'Amazon Sales' as table_name , COUNT(*) as duplicates 
                FROM (SELECT id
                    FROM warehouse_comparison 
                    GROUP BY id
                    HAVING COUNT(*) > 1)

                UNION ALL

                SELECT 'Amazon Sales' as table_name , COUNT(*) as duplicates 
                FROM (SELECT id
                    FROM expenses 
                    GROUP BY id
                    HAVING COUNT(*) > 1)
        """

    result = pd.read_sql(query, conn)
    print(result)


conn = get_connection()
get_duplicates(conn)
