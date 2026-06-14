import pandas as pd
from db_connection import get_dbConnection

def get_connection():
    conn = get_dbConnection()
    print("Connected to db")
    return conn

def insert_inventory(cur, connection):
    df = pd.read_csv('data/Sale Report.csv', encoding='latin1')
    df.columns = df.columns.str.strip()
    df = df[['SKU Code', 'Design No.', 'Stock', 'Category', 'Size', 'Color']]
    df.columns = ['sku_code', 'design_no', 'stock', 'category', 'size', 'color']
    df = df.where(pd.notna(df), None)
    df = df.replace('', None)
    
    for _, row in df.iterrows():
        values = tuple(None if pd.isna(v) else v for v in row)
        cur.execute(
            "INSERT INTO inventory (sku_code, design_no, stock, category, size, color) VALUES (%s, %s, %s, %s, %s, %s)",
            values
        )
    connection.commit()
    print(f"inventory: {len(df)} rows inserted")

def insert_product_pricing(cur, connection):
    may = pd.read_csv('data/May-2022.csv', encoding='latin1')
    may.columns = may.columns.str.strip()
    
    pl = pd.read_csv('data/P  L March 2021.csv', encoding='latin1')
    pl.columns = pl.columns.str.strip()
    pl = pl.rename(columns={'TP 1': 'TP'}).drop(columns=['TP 2'], errors='ignore')
    
    cols = ['Sku', 'Style Id', 'Catalog', 'Category', 'Weight', 'TP', 'MRP Old', 'Final MRP Old',
            'Ajio MRP', 'Amazon MRP', 'Amazon FBA MRP', 'Flipkart MRP', 'Limeroad MRP',
            'Myntra MRP', 'Paytm MRP', 'Snapdeal MRP']
    
    df = pd.concat([may[cols], pl[cols]], ignore_index=True)
    df.columns = ['sku', 'style_id', 'catalog', 'category', 'weight', 'tp', 'mrp_old', 'final_mrp_old',
                  'ajio_mrp', 'amazon_mrp', 'amazon_fba_mrp', 'flipkart_mrp', 'limeroad_mrp',
                  'myntra_mrp', 'paytm_mrp', 'snapdeal_mrp']
    df = df.where(pd.notna(df), None)
    df = df.replace('', None)
    
    for _, row in df.iterrows():
        values = tuple(None if pd.isna(v) else v for v in row)
        cur.execute(
            """INSERT INTO product_pricing (sku, style_id, catalog, category, weight, tp, mrp_old, final_mrp_old,
               ajio_mrp, amazon_mrp, amazon_fba_mrp, flipkart_mrp, limeroad_mrp, myntra_mrp, paytm_mrp, snapdeal_mrp) VALUES 
            (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
            values
        )
    connection.commit()
    print(f"product_pricing: {len(df)} rows inserted")

def insert_amazon_sales(cur, connection):
    df = pd.read_csv('data/Amazon Sale Report.csv', encoding='latin1', low_memory=False)
    df.columns = df.columns.str.strip()
    df = df[['Order ID', 'Date', 'Status', 'Fulfilment', 'Sales Channel', 'ship-service-level',
             'Style', 'SKU', 'Category', 'Size', 'ASIN', 'Courier Status', 'Qty', 'currency',
             'Amount', 'ship-city', 'ship-state', 'ship-postal-code', 'ship-country',
             'promotion-ids', 'B2B', 'fulfilled-by']]
    df.columns = ['order_id', 'date', 'status', 'fulfilment', 'sales_channel', 'ship_service_level',
                  'style', 'sku', 'category', 'size', 'asin', 'courier_status', 'qty', 'currency',
                  'amount', 'ship_city', 'ship_state', 'ship_postal_code', 'ship_country',
                  'promotion_ids', 'b2b', 'fulfilled_by']
    df = df.where(pd.notna(df), None)
    df = df.replace('', None)
    
    for _, row in df.iterrows():
        values = tuple(None if pd.isna(v) else v for v in row)
        cur.execute(
            """INSERT INTO amazon_sales (order_id, date, status, fulfilment, sales_channel, ship_service_level,
               style, sku, category, size, asin, courier_status, qty, currency, amount, ship_city, ship_state, 
               ship_postal_code, ship_country, promotion_ids, b2b, fulfilled_by)  VALUES 
            (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
            values
        )
    connection.commit()
    print(f"amazon_sales: {len(df)} rows inserted")

def insert_international_sales(cur, connection):
    df = pd.read_csv('data/International sale Report.csv', encoding='latin1')
    df.columns = df.columns.str.strip()
    df = df[['DATE', 'Months', 'CUSTOMER', 'Style', 'SKU', 'Size', 'PCS', 'RATE', 'GROSS AMT']]
    df.columns = ['date', 'months', 'customer', 'style', 'sku', 'size', 'pcs', 'rate', 'gross_amt']
   
    
    for _, row in df.iterrows():
        values = tuple(None if pd.isna(v) else v for v in row)
        cur.execute(
            "INSERT INTO international_sales (date, months, customer, style, sku, size, pcs, rate, gross_amt) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
            values
        )
    connection.commit()
    print(f"international_sales: {len(df)} rows inserted")

def insert_warehouse_comparison(cur, connection):
    df = pd.read_csv('data/Cloud Warehouse Compersion Chart.csv', encoding='latin1')
    df.columns = df.columns.str.strip()
    df = df[['Shiprocket', 'INCREFF']]
    df.columns = ['shiprocket', 'increff']
    df = df.where(pd.notna(df), None)
    df = df.replace('', None)
    
    for _, row in df.iterrows():
        values = tuple(None if pd.isna(v) else v for v in row)
        cur.execute(
            "INSERT INTO warehouse_comparison (shiprocket, increff) VALUES (%s, %s)",
            values
        )
    connection.commit()
    print(f"warehouse_comparison: {len(df)} rows inserted")

def insert_expenses(cur, connection):
    df = pd.read_csv('data/Expense IIGF.csv', encoding='latin1')
    df.columns = df.columns.str.strip()
    df = df[['Recived Amount', 'Expance']]
    df.columns = ['received_amount', 'expense']
    df = df.where(pd.notna(df), None)
    df = df.replace('', None)
    
    for _, row in df.iterrows():
        values = tuple(None if pd.isna(v) else v for v in row)
        cur.execute(
            "INSERT INTO expenses (received_amount, expense) VALUES (%s, %s)",
            values
        )
    connection.commit()
    print(f"expenses: {len(df)} rows inserted")

# Run all inserts
connection = get_connection()
cur = connection.cursor()

insert_inventory(cur, connection)
insert_product_pricing(cur, connection)
insert_amazon_sales(cur, connection)
insert_international_sales(cur, connection)
insert_warehouse_comparison(cur, connection)
insert_expenses(cur, connection)

print("\nAll data inserted")