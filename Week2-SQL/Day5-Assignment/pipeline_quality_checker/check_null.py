import pandas as pd
import sys
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')
sys.path.append(str(Path(__file__).parent.parent))
from db_connection import get_dbConnection

# join bw order and sales
def get_null_inventory(conn):

    print("\n===================Table : Inventory=================================")

    query = """SELECT sku_code , design_no
                FROM inventory
                WHERE design_no IS NULL
                LIMIT 10
    """

    query2 = """
            WITH count_null_rows AS(
            SELECT COUNT(*) FILTER (WHERE design_no IS NULL) as null_rows_count , COUNT(*) as total_rows 
            FROM inventory
            )
            SELECT 'Inventory' as table_name, 'design_no' as column_name , total_rows , null_rows_count ,(( null_rows_count::FLOAT / total_rows) * 100)
            as percentage
            FROM count_null_rows
     """
    print("\n-------overall design_no column stats---------")
    result = pd.read_sql(query2, conn)
    print(result)

    print("Coloumn : stock")
    query = """SELECT sku_code , stock
                FROM inventory
                WHERE stock IS NULL
                LIMIT 10
    """

    # result = pd.read_sql(query, conn)
    # print(result)
    # count no of rows where value is in design_col
    query2 = """
            WITH count_null_rows AS(
            SELECT COUNT(*) FILTER (WHERE stock IS NULL) as null_rows_count , COUNT(*) as total_rows 
            FROM inventory
            )
            SELECT 'Inventory' as table_name, 'stock' as column_name , total_rows , null_rows_count ,(( null_rows_count::FLOAT / total_rows) * 100)
            as percentage
            FROM count_null_rows
     """

    print("\n-------overall stock column stats---------")
    result = pd.read_sql(query2, conn)
    print(result)

    print("Coloumn : category")
    query = """SELECT sku_code , category
                FROM inventory
                WHERE category IS NULL
                LIMIT 10
    """


    query2 = """
            WITH count_null_rows AS(
            SELECT COUNT(*) FILTER (WHERE category IS NULL) as null_rows_count , COUNT(*) as total_rows 
            FROM inventory
            )
            SELECT 'Inventory' as table_name, 'category' as column_name , total_rows , null_rows_count ,(( null_rows_count::FLOAT / total_rows) * 100)
            as percentage
            FROM count_null_rows
     """

    print("\n-------overall category column stats---------")
    result = pd.read_sql(query2, conn)
    print(result)


    print("Coloumn : size")
    query = """SELECT sku_code , size
                FROM inventory
                WHERE size IS NULL
                LIMIT 10
    """


    query2 = """
            WITH count_null_rows AS(
            SELECT COUNT(*) FILTER (WHERE size IS NULL) as null_rows_count , COUNT(*) as total_rows 
            FROM inventory
            )
            SELECT 'Inventory' as table_name, 'size' as column_name , total_rows , null_rows_count ,(( null_rows_count::FLOAT / total_rows) * 100)
            as percentage
            FROM count_null_rows
     """

    print("\n-------overall size column stats---------")
    result = pd.read_sql(query2, conn)
    print(result)



    print("Coloumn : color")
    query = """SELECT sku_code , color
                FROM inventory
                WHERE color IS NULL
                LIMIT 10
    """


    query2 = """
            WITH count_null_rows AS(
            SELECT COUNT(*) FILTER (WHERE color IS NULL) as null_rows_count , COUNT(*) as total_rows 
            FROM inventory
            )
            SELECT 'Inventory' as table_name, 'color' as column_name , total_rows , null_rows_count ,(( null_rows_count::FLOAT / total_rows) * 100)
            as percentage
            FROM count_null_rows
     """

    print("\n-------overall color column stats---------")
    result = pd.read_sql(query2, conn)
    print(result)

def get_null_product_pricing(conn):
    print("\n=========================Table : Product Pricing========================================")

    query = """SELECT sku , style_id
                FROM product_pricing
                WHERE style_id IS NULL
                LIMIT 10
    """
    query2 = """
            WITH count_null_rows AS(
            SELECT COUNT(*) FILTER (WHERE style_id IS NULL) as null_rows_count , COUNT(*) as total_rows 
            FROM product_pricing
            )
            SELECT 'Product Pricing' as table_name, 'style_id' as column_name , total_rows , null_rows_count ,(( null_rows_count::FLOAT / total_rows) * 100)
            as percentage
            FROM count_null_rows
     """

    print("\n-------overall style_id column stats---------")
    result = pd.read_sql(query2, conn)
    print(result)


    query = """SELECT sku , catalog
                FROM product_pricing
                WHERE catalog IS NULL
                LIMIT 10
    """
    query2 = """
            WITH count_null_rows AS(
            SELECT COUNT(*) FILTER (WHERE catalog IS NULL) as null_rows_count , COUNT(*) as total_rows 
            FROM product_pricing
            )
            SELECT 'Product Pricing' as table_name, 'catalog' as column_name , total_rows , null_rows_count ,(( null_rows_count::FLOAT / total_rows) * 100)
            as percentage
            FROM count_null_rows
     """

    print("\n-------overall catalog column stats---------")
    result = pd.read_sql(query2, conn)
    print(result)


    query = """SELECT sku , category
                FROM product_pricing
                WHERE category IS NULL
                LIMIT 10
    """
    query2 = """
            WITH count_null_rows AS(
            SELECT COUNT(*) FILTER (WHERE category IS NULL) as null_rows_count , COUNT(*) as total_rows 
            FROM product_pricing
            )
            SELECT 'Product Pricing' as table_name, 'category' as column_name , total_rows , null_rows_count ,(( null_rows_count::FLOAT / total_rows) * 100)
            as percentage
            FROM count_null_rows
     """

    print("\n-------overall category column stats---------")
    result = pd.read_sql(query2, conn)
    print(result)


    query = """SELECT sku , weight
                FROM product_pricing
                WHERE weight IS NULL
                LIMIT 10
    """
    query2 = """
            WITH count_null_rows AS(
            SELECT COUNT(*) FILTER (WHERE weight IS NULL) as null_rows_count , COUNT(*) as total_rows 
            FROM product_pricing
            )
            SELECT 'Product Pricing' as table_name, 'weight' as column_name , total_rows , null_rows_count ,(( null_rows_count::FLOAT / total_rows) * 100)
            as percentage
            FROM count_null_rows
     """

    print("\n-------overall weight column stats---------")
    result = pd.read_sql(query2, conn)
    print(result)

    query = """SELECT sku , tp
                FROM product_pricing
                WHERE tp IS NULL
                LIMIT 10
    """
    query2 = """
            WITH count_null_rows AS(
            SELECT COUNT(*) FILTER (WHERE tp IS NULL) as null_rows_count , COUNT(*) as total_rows 
            FROM product_pricing
            )
            SELECT 'Product Pricing' as table_name, 'tp' as column_name , total_rows , null_rows_count ,(( null_rows_count::FLOAT / total_rows) * 100)
            as percentage
            FROM count_null_rows
     """

    print("\n-------overall tp column stats---------")
    result = pd.read_sql(query2, conn)
    print(result)



    query = """SELECT sku , mrp_old
                FROM product_pricing
                WHERE mrp_old IS NULL
                LIMIT 10
    """
    query2 = """
            WITH count_null_rows AS(
            SELECT COUNT(*) FILTER (WHERE mrp_old IS NULL) as null_rows_count , COUNT(*) as total_rows 
            FROM product_pricing
            )
            SELECT 'Product Pricing' as table_name, 'mrp_old' as column_name , total_rows , null_rows_count ,(( null_rows_count::FLOAT / total_rows) * 100)
            as percentage
            FROM count_null_rows
     """

    print("\n-------overall mrp_old column stats---------")
    result = pd.read_sql(query2, conn)
    print(result)

    query = """SELECT sku , final_mrp_old
                FROM product_pricing
                WHERE style_id IS NULL
                LIMIT 10
    """
    query2 = """
            WITH count_null_rows AS(
            SELECT COUNT(*) FILTER (WHERE final_mrp_old IS NULL) as null_rows_count , COUNT(*) as total_rows 
            FROM product_pricing
            )
            SELECT 'Product Pricing' as table_name, 'final_mrp_old' as column_name , total_rows , null_rows_count ,(( null_rows_count::FLOAT / total_rows) * 100)
            as percentage
            FROM count_null_rows
     """

    print("\n-------overall final_mrp_old column stats---------")
    result = pd.read_sql(query2, conn)
    print(result)

    query = """SELECT sku , ajio_mrp
                FROM product_pricing
                WHERE style_id IS NULL
                LIMIT 10
    """
    query2 = """
                WITH count_null_rows AS(
                SELECT COUNT(*) FILTER (WHERE ajio_mrp IS NULL) as null_rows_count , COUNT(*) as total_rows 
                FROM product_pricing
                )
                SELECT 'Product Pricing' as table_name, 'ajio_mrp' as column_name , total_rows , null_rows_count ,(( null_rows_count::FLOAT / total_rows) * 100)
                as percentage
                FROM count_null_rows
        """

    print("\n-------overall ajio_mrp column stats---------")
    result = pd.read_sql(query2, conn)
    print(result)


    query = """SELECT sku , amazon_mrp
                    FROM product_pricing
                    WHERE style_id IS NULL
                    LIMIT 10
        """
    query2 = """
                WITH count_null_rows AS(
                SELECT COUNT(*) FILTER (WHERE amazon_mrp IS NULL) as null_rows_count , COUNT(*) as total_rows 
                FROM product_pricing
                )
                SELECT 'Product Pricing' as table_name, 'amazon_mrp' as column_name , total_rows , null_rows_count ,(( null_rows_count::FLOAT / total_rows) * 100)
                as percentage
                FROM count_null_rows
        """

    print("\n-------overall amazon_mrp column stats---------")
    result = pd.read_sql(query2, conn)
    print(result)


    query = """SELECT sku , amazon_fba_mrp
                    FROM product_pricing
                    WHERE style_id IS NULL
                    LIMIT 10
        """
    query2 = """
                WITH count_null_rows AS(
                SELECT COUNT(*) FILTER (WHERE amazon_fba_mrp IS NULL) as null_rows_count , COUNT(*) as total_rows 
                FROM product_pricing
                )
                SELECT 'Product Pricing' as table_name, 'amazon_fba_mrp' as column_name , total_rows , null_rows_count ,(( null_rows_count::FLOAT / total_rows) * 100)
                as percentage
                FROM count_null_rows
        """

    print("\n-------overall amazon_fba_mrp column stats---------")
    result = pd.read_sql(query2, conn)
    print(result)


    query = """SELECT sku , flipkart_mrp
                    FROM product_pricing
                    WHERE style_id IS NULL
                    LIMIT 10
        """
    query2 = """
                WITH count_null_rows AS(
                SELECT COUNT(*) FILTER (WHERE flipkart_mrp IS NULL) as null_rows_count , COUNT(*) as total_rows 
                FROM product_pricing
                )
                SELECT 'Product Pricing' as table_name, 'flipkart_mrp' as column_name , total_rows , null_rows_count ,(( null_rows_count::FLOAT / total_rows) * 100)
                as percentage
                FROM count_null_rows
        """

    print("\n-------overall flipkart_mrp column stats---------")
    result = pd.read_sql(query2, conn)
    print(result)


    query = """SELECT sku , limeroad_mrp
                    FROM product_pricing
                    WHERE style_id IS NULL
                    LIMIT 10
        """
    query2 = """
                WITH count_null_rows AS(
                SELECT COUNT(*) FILTER (WHERE limeroad_mrp IS NULL) as null_rows_count , COUNT(*) as total_rows 
                FROM product_pricing
                )
                SELECT 'Product Pricing' as table_name, 'limeroad_mrp' as column_name , total_rows , null_rows_count ,(( null_rows_count::FLOAT / total_rows) * 100)
                as percentage
                FROM count_null_rows
        """

    print("\n-------overall limeroad_mrp column stats---------")
    result = pd.read_sql(query2, conn)
    print(result)


    query = """SELECT sku , myntra_mrp
                    FROM product_pricing
                    WHERE style_id IS NULL
                    LIMIT 10
        """
    query2 = """
                WITH count_null_rows AS(
                SELECT COUNT(*) FILTER (WHERE myntra_mrp IS NULL) as null_rows_count , COUNT(*) as total_rows 
                FROM product_pricing
                )
                SELECT 'Product Pricing' as table_name, 'myntra_mrp' as column_name , total_rows , null_rows_count ,(( null_rows_count::FLOAT / total_rows) * 100)
                as percentage
                FROM count_null_rows
        """

    print("\n-------overall myntra_mrp column stats---------")
    result = pd.read_sql(query2, conn)
    print(result)


    query = """SELECT sku , paytm_mrp
                    FROM product_pricing
                    WHERE style_id IS NULL
                    LIMIT 10
        """
    query2 = """
                WITH count_null_rows AS(
                SELECT COUNT(*) FILTER (WHERE paytm_mrp IS NULL) as null_rows_count , COUNT(*) as total_rows 
                FROM product_pricing
                )
                SELECT 'Product Pricing' as table_name, 'paytm_mrp' as column_name , total_rows , null_rows_count ,(( null_rows_count::FLOAT / total_rows) * 100)
                as percentage
                FROM count_null_rows
        """

    print("\n-------overall paytm_mrp column stats---------")
    result = pd.read_sql(query2, conn)
    print(result)


    query = """SELECT sku , snapdeal_mrp
                    FROM product_pricing
                    WHERE style_id IS NULL
                    LIMIT 10
        """
    query2 = """
                WITH count_null_rows AS(
                SELECT COUNT(*) FILTER (WHERE snapdeal_mrp IS NULL) as null_rows_count , COUNT(*) as total_rows 
                FROM product_pricing
                )
                SELECT 'Product Pricing' as table_name, 'snapdeal_mrp' as column_name , total_rows , null_rows_count ,(( null_rows_count::FLOAT / total_rows) * 100)
                as percentage
                FROM count_null_rows
        """

    print("\n-------overall snapdeal_mrp column stats---------")
    result = pd.read_sql(query2, conn)
    print(result)

def get_null_amazon_sales(conn):
    print("\n====================Amazon sales table===============================")
    query = """SELECT sku , date
                FROM amazon_sales
                WHERE style IS NULL
                LIMIT 10
        """
    query2 = """
                WITH count_null_rows AS(
                SELECT COUNT(*) FILTER (WHERE date IS NULL) as null_rows_count , COUNT(*) as total_rows 
                FROM amazon_sales
                )
                SELECT 'Amazon Sale Report' as table_name, 'date' as column_name , total_rows , null_rows_count ,(( null_rows_count::FLOAT / total_rows) * 100)
                as percentage
                FROM count_null_rows
        """

    print("\n-------overall date column stats---------")
    result = pd.read_sql(query2, conn)
    print(result)


    query = """SELECT sku , status
                    FROM amazon_sales
                    WHERE style IS NULL
                    LIMIT 10
        """
    query2 = """
                WITH count_null_rows AS(
                SELECT COUNT(*) FILTER (WHERE status IS NULL) as null_rows_count , COUNT(*) as total_rows 
                FROM amazon_sales
                )
                SELECT 'Amazon Sale Report' as table_name, 'status' as column_name , total_rows , null_rows_count ,(( null_rows_count::FLOAT / total_rows) * 100)
                as percentage
                FROM count_null_rows
        """

    print("\n-------overall status column stats---------")
    result = pd.read_sql(query2, conn)
    print(result)


    query = """SELECT sku , fulfilment
                    FROM amazon_sales
                    WHERE style IS NULL
                    LIMIT 10
        """
    query2 = """
                WITH count_null_rows AS(
                SELECT COUNT(*) FILTER (WHERE fulfilment IS NULL) as null_rows_count , COUNT(*) as total_rows 
                FROM amazon_sales
                )
                SELECT 'Amazon Sale Report' as table_name, 'fulfilment' as column_name , total_rows , null_rows_count ,(( null_rows_count::FLOAT / total_rows) * 100)
                as percentage
                FROM count_null_rows
        """

    print("\n-------overall fulfilment column stats---------")
    result = pd.read_sql(query2, conn)
    print(result)


    query = """SELECT sku , sales_channel
                    FROM amazon_sales
                    WHERE style IS NULL
                    LIMIT 10
        """
    query2 = """
                WITH count_null_rows AS(
                SELECT COUNT(*) FILTER (WHERE sales_channel IS NULL) as null_rows_count , COUNT(*) as total_rows 
                FROM amazon_sales
                )
                SELECT 'Amazon Sale Report' as table_name, 'sales_channel' as column_name , total_rows , null_rows_count ,(( null_rows_count::FLOAT / total_rows) * 100)
                as percentage
                FROM count_null_rows
        """

    print("\n-------overall sales_channel column stats---------")
    result = pd.read_sql(query2, conn)
    print(result)


    query = """SELECT sku , ship_service_level
                    FROM amazon_sales
                    WHERE style IS NULL
                    LIMIT 10
        """
    query2 = """
                WITH count_null_rows AS(
                SELECT COUNT(*) FILTER (WHERE ship_service_level IS NULL) as null_rows_count , COUNT(*) as total_rows 
                FROM amazon_sales
                )
                SELECT 'Amazon Sale Report' as table_name, 'ship_service_level' as column_name , total_rows , null_rows_count ,(( null_rows_count::FLOAT / total_rows) * 100)
                as percentage
                FROM count_null_rows
        """

    print("\n-------overall ship_service_level column stats---------")
    result = pd.read_sql(query2, conn)
    print(result)


    query = """SELECT sku , style
                    FROM amazon_sales
                    WHERE style IS NULL
                    LIMIT 10
        """
    query2 = """
                WITH count_null_rows AS(
                SELECT COUNT(*) FILTER (WHERE style IS NULL) as null_rows_count , COUNT(*) as total_rows 
                FROM amazon_sales
                )
                SELECT 'Amazon Sale Report' as table_name, 'style' as column_name , total_rows , null_rows_count ,(( null_rows_count::FLOAT / total_rows) * 100)
                as percentage
                FROM count_null_rows
        """

    print("\n-------overall style column stats---------")
    result = pd.read_sql(query2, conn)
    print(result)


    query = """SELECT sku , sku
                    FROM amazon_sales
                    WHERE style IS NULL
                    LIMIT 10
        """
    query2 = """
                WITH count_null_rows AS(
                SELECT COUNT(*) FILTER (WHERE sku IS NULL) as null_rows_count , COUNT(*) as total_rows 
                FROM amazon_sales
                )
                SELECT 'Amazon Sale Report' as table_name, 'sku' as column_name , total_rows , null_rows_count ,(( null_rows_count::FLOAT / total_rows) * 100)
                as percentage
                FROM count_null_rows
        """

    print("\n-------overall sku column stats---------")
    result = pd.read_sql(query2, conn)
    print(result)


    query = """SELECT sku , category
                    FROM amazon_sales
                    WHERE style IS NULL
                    LIMIT 10
        """
    query2 = """
                WITH count_null_rows AS(
                SELECT COUNT(*) FILTER (WHERE category IS NULL) as null_rows_count , COUNT(*) as total_rows 
                FROM amazon_sales
                )
                SELECT 'Amazon Sale Report' as table_name, 'category' as column_name , total_rows , null_rows_count ,(( null_rows_count::FLOAT / total_rows) * 100)
                as percentage
                FROM count_null_rows
        """

    print("\n-------overall category column stats---------")
    result = pd.read_sql(query2, conn)
    print(result)


    query = """SELECT sku , size
                    FROM amazon_sales
                    WHERE style IS NULL
                    LIMIT 10
        """
    query2 = """
                WITH count_null_rows AS(
                SELECT COUNT(*) FILTER (WHERE size IS NULL) as null_rows_count , COUNT(*) as total_rows 
                FROM amazon_sales
                )
                SELECT 'Amazon Sale Report' as table_name, 'size' as column_name , total_rows , null_rows_count ,(( null_rows_count::FLOAT / total_rows) * 100)
                as percentage
                FROM count_null_rows
        """

    print("\n-------overall size column stats---------")
    result = pd.read_sql(query2, conn)
    print(result)


    query = """SELECT sku , asin
                    FROM amazon_sales
                    WHERE style IS NULL
                    LIMIT 10
        """
    query2 = """
                WITH count_null_rows AS(
                SELECT COUNT(*) FILTER (WHERE asin IS NULL) as null_rows_count , COUNT(*) as total_rows 
                FROM amazon_sales
                )
                SELECT 'Amazon Sale Report' as table_name, 'asin' as column_name , total_rows , null_rows_count ,(( null_rows_count::FLOAT / total_rows) * 100)
                as percentage
                FROM count_null_rows
        """

    print("\n-------overall asin column stats---------")
    result = pd.read_sql(query2, conn)
    print(result)


    query = """SELECT sku , courier_status
                    FROM amazon_sales
                    WHERE style IS NULL
                    LIMIT 10
        """
    query2 = """
                WITH count_null_rows AS(
                SELECT COUNT(*) FILTER (WHERE courier_status IS NULL) as null_rows_count , COUNT(*) as total_rows 
                FROM amazon_sales
                )
                SELECT 'Amazon Sale Report' as table_name, 'courier_status' as column_name , total_rows , null_rows_count ,(( null_rows_count::FLOAT / total_rows) * 100)
                as percentage
                FROM count_null_rows
        """

    print("\n-------overall courier_status column stats---------")
    result = pd.read_sql(query2, conn)
    print(result)


    query = """SELECT sku , qty
                    FROM amazon_sales
                    WHERE style IS NULL
                    LIMIT 10
        """
    query2 = """
                WITH count_null_rows AS(
                SELECT COUNT(*) FILTER (WHERE qty IS NULL) as null_rows_count , COUNT(*) as total_rows 
                FROM amazon_sales
                )
                SELECT 'Amazon Sale Report' as table_name, 'qty' as column_name , total_rows , null_rows_count ,(( null_rows_count::FLOAT / total_rows) * 100)
                as percentage
                FROM count_null_rows
        """

    print("\n-------overall qty column stats---------")
    result = pd.read_sql(query2, conn)
    print(result)


    query = """SELECT sku , currency
                    FROM amazon_sales
                    WHERE style IS NULL
                    LIMIT 10
        """
    query2 = """
                WITH count_null_rows AS(
                SELECT COUNT(*) FILTER (WHERE currency IS NULL) as null_rows_count , COUNT(*) as total_rows 
                FROM amazon_sales
                )
                SELECT 'Amazon Sale Report' as table_name, 'currency' as column_name , total_rows , null_rows_count ,(( null_rows_count::FLOAT / total_rows) * 100)
                as percentage
                FROM count_null_rows
        """

    print("\n-------overall currency column stats---------")
    result = pd.read_sql(query2, conn)
    print(result)


    query = """SELECT sku , amount
                    FROM amazon_sales
                    WHERE style IS NULL
                    LIMIT 10
        """
    query2 = """
                WITH count_null_rows AS(
                SELECT COUNT(*) FILTER (WHERE amount IS NULL) as null_rows_count , COUNT(*) as total_rows 
                FROM amazon_sales
                )
                SELECT 'Amazon Sale Report' as table_name, 'amount' as column_name , total_rows , null_rows_count ,(( null_rows_count::FLOAT / total_rows) * 100)
                as percentage
                FROM count_null_rows
        """

    print("\n-------overall amount column stats---------")
    result = pd.read_sql(query2, conn)
    print(result)


    query = """SELECT sku , ship_city
                    FROM amazon_sales
                    WHERE style IS NULL
                    LIMIT 10
        """
    query2 = """
                WITH count_null_rows AS(
                SELECT COUNT(*) FILTER (WHERE ship_city IS NULL) as null_rows_count , COUNT(*) as total_rows 
                FROM amazon_sales
                )
                SELECT 'Amazon Sale Report' as table_name, 'ship_city' as column_name , total_rows , null_rows_count ,(( null_rows_count::FLOAT / total_rows) * 100)
                as percentage
                FROM count_null_rows
        """

    print("\n-------overall ship_city column stats---------")
    result = pd.read_sql(query2, conn)
    print(result)


    query = """SELECT sku , ship_state
                    FROM amazon_sales
                    WHERE style IS NULL
                    LIMIT 10
        """
    query2 = """
                WITH count_null_rows AS(
                SELECT COUNT(*) FILTER (WHERE ship_state IS NULL) as null_rows_count , COUNT(*) as total_rows 
                FROM amazon_sales
                )
                SELECT 'Amazon Sale Report' as table_name, 'ship_state' as column_name , total_rows , null_rows_count ,(( null_rows_count::FLOAT / total_rows) * 100)
                as percentage
                FROM count_null_rows
        """

    print("\n-------overall ship_state column stats---------")
    result = pd.read_sql(query2, conn)
    print(result)


    query = """SELECT sku , ship_postal_code
                    FROM amazon_sales
                    WHERE style IS NULL
                    LIMIT 10
        """
    query2 = """
                WITH count_null_rows AS(
                SELECT COUNT(*) FILTER (WHERE ship_postal_code IS NULL) as null_rows_count , COUNT(*) as total_rows 
                FROM amazon_sales
                )
                SELECT 'Amazon Sale Report' as table_name, 'ship_postal_code' as column_name , total_rows , null_rows_count ,(( null_rows_count::FLOAT / total_rows) * 100)
                as percentage
                FROM count_null_rows
        """

    print("\n-------overall ship_postal_code column stats---------")
    result = pd.read_sql(query2, conn)
    print(result)


    query = """SELECT sku , ship_country
                    FROM amazon_sales
                    WHERE style IS NULL
                    LIMIT 10
        """
    query2 = """
                WITH count_null_rows AS(
                SELECT COUNT(*) FILTER (WHERE ship_country IS NULL) as null_rows_count , COUNT(*) as total_rows 
                FROM amazon_sales
                )
                SELECT 'Amazon Sale Report' as table_name, 'ship_country' as column_name , total_rows , null_rows_count ,(( null_rows_count::FLOAT / total_rows) * 100)
                as percentage
                FROM count_null_rows
        """

    print("\n-------overall ship_country column stats---------")
    result = pd.read_sql(query2, conn)
    print(result)


    query = """SELECT sku , promotion_ids
                    FROM amazon_sales
                    WHERE style IS NULL
                    LIMIT 10
        """
    query2 = """
                WITH count_null_rows AS(
                SELECT COUNT(*) FILTER (WHERE promotion_ids IS NULL) as null_rows_count , COUNT(*) as total_rows 
                FROM amazon_sales
                )
                SELECT 'Amazon Sale Report' as table_name, 'promotion_ids' as column_name , total_rows , null_rows_count ,(( null_rows_count::FLOAT / total_rows) * 100)
                as percentage
                FROM count_null_rows
        """

    print("\n-------overall promotion_ids column stats---------")
    result = pd.read_sql(query2, conn)
    print(result)


    query = """SELECT sku , b2b
                    FROM amazon_sales
                    WHERE style IS NULL
                    LIMIT 10
        """
    query2 = """
                WITH count_null_rows AS(
                SELECT COUNT(*) FILTER (WHERE b2b IS NULL) as null_rows_count , COUNT(*) as total_rows 
                FROM amazon_sales
                )
                SELECT 'Amazon Sale Report' as table_name, 'b2b' as column_name , total_rows , null_rows_count ,(( null_rows_count::FLOAT / total_rows) * 100)
                as percentage
                FROM count_null_rows
        """

    print("\n-------overall b2b column stats---------")
    result = pd.read_sql(query2, conn)
    print(result)


    query = """SELECT sku , fulfilled_by
                    FROM amazon_sales
                    WHERE style IS NULL
                    LIMIT 10
        """
    query2 = """
                WITH count_null_rows AS(
                SELECT COUNT(*) FILTER (WHERE fulfilled_by IS NULL) as null_rows_count , COUNT(*) as total_rows 
                FROM amazon_sales
                )
                SELECT 'Amazon Sale Report' as table_name, 'fulfilled_by' as column_name , total_rows , null_rows_count ,(( null_rows_count::FLOAT / total_rows) * 100)
                as percentage
                FROM count_null_rows
        """

    print("\n-------overall fulfilled_by column stats---------")
    result = pd.read_sql(query2, conn)
    print(result)

def get_nul_international_sales(conn):
    print("\n=============================International sales tabele===================================")
    query = """SELECT sku , date
                    FROM international_sales
                    WHERE style IS NULL
                    LIMIT 10
        """
    query2 = """
                WITH count_null_rows AS(
                SELECT COUNT(*) FILTER (WHERE date IS NULL) as null_rows_count , COUNT(*) as total_rows 
                FROM international_sales
                )
                SELECT 'International Sales' as table_name, 'date' as column_name , total_rows , null_rows_count ,(( null_rows_count::FLOAT / total_rows) * 100)
                as percentage
                FROM count_null_rows
        """

    print("\n-------overall date column stats---------")
    result = pd.read_sql(query2, conn)
    print(result)


    query = """SELECT sku , months
                    FROM international_sales
                    WHERE style IS NULL
                    LIMIT 10
        """
    query2 = """
                WITH count_null_rows AS(
                SELECT COUNT(*) FILTER (WHERE months IS NULL) as null_rows_count , COUNT(*) as total_rows 
                FROM international_sales
                )
                SELECT 'International Sales' as table_name, 'months' as column_name , total_rows , null_rows_count ,(( null_rows_count::FLOAT / total_rows) * 100)
                as percentage
                FROM count_null_rows
        """

    print("\n-------overall months column stats---------")
    result = pd.read_sql(query2, conn)
    print(result)


    query = """SELECT sku , customer
                    FROM international_sales
                    WHERE style IS NULL
                    LIMIT 10
        """
    query2 = """
                WITH count_null_rows AS(
                SELECT COUNT(*) FILTER (WHERE customer IS NULL) as null_rows_count , COUNT(*) as total_rows 
                FROM international_sales
                )
                SELECT 'International Sales' as table_name, 'customer' as column_name , total_rows , null_rows_count ,(( null_rows_count::FLOAT / total_rows) * 100)
                as percentage
                FROM count_null_rows
        """

    print("\n-------overall customer column stats---------")
    result = pd.read_sql(query2, conn)
    print(result)


    query = """SELECT style
                    FROM international_sales
                    WHERE style IS NULL
                    LIMIT 10
        """
    query2 = """
                WITH count_null_rows AS(
                SELECT COUNT(*) FILTER (WHERE style IS NULL) as null_rows_count , COUNT(*) as total_rows 
                FROM international_sales
                )
                SELECT 'International Sales' as table_name, 'style' as column_name , total_rows , null_rows_count ,(( null_rows_count::FLOAT / total_rows) * 100)
                as percentage
                FROM count_null_rows
        """

    print("\n-------overall style column stats---------")
    result = pd.read_sql(query2, conn)
    print(result)


    query = """SELECT sku 
           FROM international_sales 
           WHERE sku IS NULL
           LIMIT 10"""

    query2 = """
                WITH count_null_rows AS(
                SELECT COUNT(*) FILTER (WHERE sku IS NULL) as null_rows_count , COUNT(*) as total_rows 
                FROM international_sales
                )
                SELECT 'International Sales' as table_name, 'sku' as column_name , total_rows , null_rows_count ,(( null_rows_count::FLOAT / total_rows) * 100)
                as percentage
                FROM count_null_rows
        """

    print("\n-------overall sku column stats---------")
    result = pd.read_sql(query2, conn)
    print(result)


    query = """SELECT sku , size
                    FROM international_sales
                    WHERE style IS NULL
                    LIMIT 10
        """
    query2 = """
                WITH count_null_rows AS(
                SELECT COUNT(*) FILTER (WHERE size IS NULL) as null_rows_count , COUNT(*) as total_rows 
                FROM international_sales
                )
                SELECT 'International Sales' as table_name, 'size' as column_name , total_rows , null_rows_count ,(( null_rows_count::FLOAT / total_rows) * 100)
                as percentage
                FROM count_null_rows
        """

    print("\n-------overall size column stats---------")
    result = pd.read_sql(query2, conn)
    print(result)


    query = """SELECT sku , pcs
                    FROM international_sales
                    WHERE style IS NULL
                    LIMIT 10
        """
    query2 = """
                WITH count_null_rows AS(
                SELECT COUNT(*) FILTER (WHERE pcs IS NULL) as null_rows_count , COUNT(*) as total_rows 
                FROM international_sales
                )
                SELECT 'International Sales' as table_name, 'pcs' as column_name , total_rows , null_rows_count ,(( null_rows_count::FLOAT / total_rows) * 100)
                as percentage
                FROM count_null_rows
        """

    print("\n-------overall pcs column stats---------")
    result = pd.read_sql(query2, conn)
    print(result)


    query = """SELECT sku , rate
                    FROM international_sales
                    WHERE style IS NULL
                    LIMIT 10
        """
    query2 = """
                WITH count_null_rows AS(
                SELECT COUNT(*) FILTER (WHERE rate IS NULL) as null_rows_count , COUNT(*) as total_rows 
                FROM international_sales
                )
                SELECT 'International Sales' as table_name, 'rate' as column_name , total_rows , null_rows_count ,(( null_rows_count::FLOAT / total_rows) * 100)
                as percentage
                FROM count_null_rows
        """

    print("\n-------overall rate column stats---------")
    result = pd.read_sql(query2, conn)
    print(result)


    query = """SELECT sku , gross_amt
                    FROM international_sales
                    WHERE style IS NULL
                    LIMIT 10
        """
    query2 = """
                WITH count_null_rows AS(
                SELECT COUNT(*) FILTER (WHERE gross_amt IS NULL) as null_rows_count , COUNT(*) as total_rows 
                FROM international_sales
                )
                SELECT 'International Sales' as table_name, 'gross_amt' as column_name , total_rows , null_rows_count ,(( null_rows_count::FLOAT / total_rows) * 100)
                as percentage
                FROM count_null_rows
        """

    print("\n-------overall gross_amt column stats---------")
    result = pd.read_sql(query2, conn)
    print(result)           

def get_null_warehouse(conn):
    print("\n========================Table : warehouse comparison ======================")
    query = """SELECT sku , shiprocket
                FROM warehouse_comparison
                WHERE style IS NULL
                LIMIT 10
    """
    query2 = """
                WITH count_null_rows AS(
                SELECT COUNT(*) FILTER (WHERE shiprocket IS NULL) as null_rows_count , COUNT(*) as total_rows 
                FROM warehouse_comparison
                )
                SELECT 'Warehouse Comparison' as table_name, 'shiprocket' as column_name , total_rows , null_rows_count ,(( null_rows_count::FLOAT / total_rows) * 100)
                as percentage
                FROM count_null_rows
        """

    print("\n-------overall shiprocket column stats---------")
    result = pd.read_sql(query2, conn)
    print(result)


    query = """SELECT sku , increff
                    FROM warehouse_comparison
                    WHERE style IS NULL
                    LIMIT 10
        """
    query2 = """
                WITH count_null_rows AS(
                SELECT COUNT(*) FILTER (WHERE increff IS NULL) as null_rows_count , COUNT(*) as total_rows 
                FROM warehouse_comparison
                )
                SELECT 'Warehouse Comparison' as table_name, 'increff' as column_name , total_rows , null_rows_count ,(( null_rows_count::FLOAT / total_rows) * 100)
                as percentage
                FROM count_null_rows
        """

    print("\n-------overall increff column stats---------")
    result = pd.read_sql(query2, conn)
    print(result)

def get_null_expenses(conn):
    print("\n=====================Table : expense table =================================")
    query = """SELECT  received_amount 
                FROM expenses 
                WHERE received_amount IS NULL
                LIMIT 10"""
    query2 = """
            WITH count_null_rows AS(
            SELECT COUNT(*) FILTER (WHERE received_amount IS NULL) as null_rows_count , COUNT(*) as total_rows 
            FROM expenses
            )
            SELECT 'Expenses' as table_name, 'received_amount' as column_name , total_rows , null_rows_count ,(( null_rows_count::FLOAT / total_rows) * 100)
            as percentage
            FROM count_null_rows
    """
    print("\n-------overall received amount column stats---------")
    result = pd.read_sql(query2, conn)
    print(result)

    query = """SELECT  expense 
                FROM expenses 
                WHERE expense IS NULL
                LIMIT 10"""

    query2 = """
            WITH count_null_rows AS(
            SELECT COUNT(*) FILTER (WHERE expense IS NULL) as null_rows_count , COUNT(*) as total_rows 
            FROM expenses
            )
            SELECT 'Expenses' as table_name, 'expense' as column_name , total_rows , null_rows_count ,(( null_rows_count::FLOAT / total_rows) * 100)
            as percentage
            FROM count_null_rows
    """

    print("\n-------overall expense column stats---------")
    result = pd.read_sql(query2, conn)
    print(result)

def get_null_coloumns(conn):
    print("================== Checking Nulls ============================")
    get_null_inventory(conn)
    get_null_product_pricing(conn)
    get_null_amazon_sales(conn)
    get_nul_international_sales(conn)
    get_null_warehouse(conn)
    get_null_expenses(conn)

