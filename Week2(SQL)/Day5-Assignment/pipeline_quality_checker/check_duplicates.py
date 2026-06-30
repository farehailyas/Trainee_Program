import pandas as pd
import sys
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')
sys.path.append(str(Path(__file__).parent.parent))
from db_connection import get_dbConnection
# join bw order and sales

def get_duplicates(conn):
    print("========================Check Duplicates=========================")
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