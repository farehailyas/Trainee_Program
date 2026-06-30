import pandas as pd
import sys
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')
sys.path.append(str(Path(__file__).parent.parent))
from db_connection import get_dbConnection

def product_pricing(conn):
    print(" \n===============Relation :  inventory -> product pricing==============")
    query = """ 
            SELECT sku , COUNT(*) as orphaned_records 
            FROM product_pricing
            WHERE sku NOT IN (
                        SELECT sku_code
                        FROM inventory
                        WHERE sku_code IS NOT NULL)
            GROUP BY sku
        """

    result = pd.read_sql(query, conn)
    print(result)

def amazon_sales(conn):
    print(" \n===============Relation :  inventory -> amazon sales==============")
    query = """ 
            SELECT sku , COUNT(*) as orphaned_records 
            FROM amazon_sales
            WHERE sku NOT IN (
                        SELECT sku_code
                        FROM inventory
                        WHERE sku_code IS NOT NULL)
            GROUP BY sku
        """

    result = pd.read_sql(query, conn)
    print(result)

def international_sales(conn):
    print(" \n===============Relation :  inventory -> international sales==============")
    query = """ 
            SELECT sku , COUNT(*) as orphaned_records 
            FROM international_sales
            WHERE sku NOT IN (
                        SELECT sku_code
                        FROM inventory
                        WHERE sku_code IS NOT NULL)
            GROUP BY sku
        """

    result = pd.read_sql(query, conn)
    print(result)


# join bw order and sales
def check_refrential_integrity(conn):
    print("\n ======================= Checking refrential Integrity=============================")
    product_pricing(conn)
    amazon_sales(conn)
    international_sales(conn)