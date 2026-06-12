import pandas as pd
import sys
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')
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
def get_null_inventory(conn):

    print("\nTable : Inventory")

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
    print("\nTable : Product Pricing")

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

    print("\n-------overall design_no column stats---------")
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

    print("\n-------overall design_no column stats---------")
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

    print("\n-------overall design_no column stats---------")
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
            SELECT 'Product Pricing' as table_name, 'style_id' as column_name , total_rows , null_rows_count ,(( null_rows_count::FLOAT / total_rows) * 100)
            as percentage
            FROM count_null_rows
     """

    print("\n-------overall design_no column stats---------")
    result = pd.read_sql(query2, conn)
    print(result)

















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

    print("\n-------overall design_no column stats---------")
    result = pd.read_sql(query2, conn)
    print(result)
















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

    print("\n-------overall design_no column stats---------")
    result = pd.read_sql(query2, conn)
    print(result)
















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

    print("\n-------overall design_no column stats---------")
    result = pd.read_sql(query2, conn)
    print(result)


def get_null_coloumns(conn):
    print("Get null coloumns")
    get_null_inventory(conn)
    get_null_product_pricing(conn)
   

conn = get_connection()
get_null_coloumns(conn)
