
import pandas as pd
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from db_connection import get_dbConnection
"""Total revenue (sum of sales)
Total order count
Per: product category, sub_category, and month
Joining: orders, sales, products tables"""

def get_connection():    
    try:
        conn = get_dbConnection()
        print("Connected to db")
        return conn
    except Exception as e:
        print(e)

def get_years(conn):
    cur = conn.cursor()
    query = """ SELECT DISTINCT TO_CHAR(orders.order_date , 'YYYY') as years
                FROM orders
                ORDER BY years
        """
    result = pd.read_sql(query, conn)
    cur.close()
    print(result)        
def get_cat(conn):
    cur = conn.cursor()
    query = """ EXPLAIN ANALYZE SELECT DISTINCT category , COUNT(*) as count
                FROM products
                GROUP BY category
                ORDER BY category
        """
    result = pd.read_sql(query, conn)
    cur.close()
    print(result)     

def index(conn):
    cur = conn.cursor()
    # query = """CREATE INDEX category_ind ON products(category)
    #     """
    # query = """ CREATE INDEX idx_sales_product_id ON sales(product_id);
    #             CREATE INDEX idx_sales_order_id ON sales(order_id);"""

    query = """CREATE INDEX index_on_partition ON products_office_supplies(category)"""
    cur.execute(query)
    conn.commit()
    cur.close()
    # print(result) 

def setup_partitioned_products(conn):
    cur = conn.cursor()
    
    # Step 1: rename existing table as backup
    cur.execute("ALTER TABLE products RENAME TO products_backup;")
    
    # Step 2: create partitioned parent table
    cur.execute("""
        CREATE TABLE products (
            product_id TEXT,
            product_name TEXT,
            category TEXT,
            sub_category TEXT
        ) PARTITION BY LIST (category);
    """)
    
    # Step 3: create partition for office supplies
    cur.execute("""
        CREATE TABLE products_office_supplies PARTITION OF products
        FOR VALUES IN ('Office Supplies');
    """)
    
    # Step 4: create default partition for everything else
    cur.execute("""
        CREATE TABLE products_default PARTITION OF products
        DEFAULT;
    """)
    
    # Step 5: copy data back
    cur.execute("INSERT INTO products SELECT * FROM products_backup;")
    
    conn.commit()
    cur.close()
    print("partitioned table created")

def get_customers(conn):
    cur = conn.cursor()
    query = """EXPLAIN ANALYZE SELECT SUM(sales.sales) total_revenue , COUNT(orders.order_id) as total_order_count 
                FROM products
                 JOIN sales
                ON sales.product_id = products.product_id
                 JOIN orders
                ON sales.order_id = orders.order_id
                WHERE products.category = 'Office Supplies'
                GROUP BY products.category , products.sub_category , TO_CHAR(orders.order_date , 'MM')
        """
    # result = pd.read_sql(query, conn)
    # cur.close()
    # print(result)    
    cur.execute(query)
    result = cur.fetchall()      
    print("\n".join([row[0] for row in result]))

conn = get_connection()
# get_years(conn)
# setup_partitioned_products(conn)
get_customers(conn)

get_cat(conn)
# index(conn)
"""
SELECT o.order_id, o.customer_id, p.payment_value, p.payment_type
FROM olist_orders_dataset o
JOIN olist_order_payments_dataset p ON o.order_id = p.order_id

WHERE p.payment_value > (
    SELECT AVG(p2.payment_value)
    FROM olist_order_payments_dataset p2
    WHERE p2.payment_type = p.payment_type
)"""


"""WITH avg_payment AS( SELECT, payemnt_type, AVG(payment_value)
    FROM olist_order_payments_dataset
    GROUP BY payment_type ) 
    
    SELECT o.order_id, o.customer_id, p.payment_value, p.payment_type
    FROM olist_orders_dataset o
    LEFT JOIN olist_order_payments_dataset p 
    ON o.order_id = p.order_id
    LEFT JOIN avg_payment 
    ON P.payement_type =  avg_payment.payment_type
    WHERE p.payment_value > avg_payment.payement_value

    """