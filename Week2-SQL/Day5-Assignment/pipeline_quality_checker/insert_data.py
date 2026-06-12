import pandas as pd
from db_connection import get_dbConnection

def get_connection():
    try:
        conn = get_dbConnection()
        print("Connected to db")
        return conn
    except Exception as e:
        print(e)

def get_existing_skus(cur):
    cur.execute("SELECT sku_code FROM inventory")
    return {row[0] for row in cur.fetchall()}

def insert_missing_skus(cur, skus, existing_skus):
    missing = [s for s in skus if s not in existing_skus]
    for sku in missing:
        cur.execute(
            "INSERT INTO inventory(sku_code,design_no,stock,category,size,color) VALUES (%s,%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING",
            (sku, None, None, None, None, None)
        )

def insert_data(connection):
    cur = connection.cursor()

    # ── inventory  ←  Sale Report.csv
    df = pd.read_csv('data/Sale Report.csv', encoding='latin1')
    df.columns = df.columns.str.strip()
    df = df[['SKU Code','Design No.','Stock','Category','Size','Color']].drop_duplicates(subset='SKU Code')
    df = df.where(df.notna(), other=None)
    for _, row in df.iterrows():
        cur.execute(
            "INSERT INTO inventory(sku_code,design_no,stock,category,size,color) VALUES (%s,%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING",
            tuple(row)
        )
    print("inventory done")

    # ── product_pricing  ←  May-2022.csv + P L March 2021.csv
    may = pd.read_csv('data/May-2022.csv', encoding='latin1')
    may.columns = may.columns.str.strip()
    may = may[['Sku','Style Id','Catalog','Category','Weight','TP','MRP Old','Final MRP Old',
               'Ajio MRP','Amazon MRP','Amazon FBA MRP','Flipkart MRP','Limeroad MRP',
               'Myntra MRP','Paytm MRP','Snapdeal MRP']]

    pl = pd.read_csv('data/P  L March 2021.csv', encoding='latin1')
    pl.columns = pl.columns.str.strip()
    pl = pl.rename(columns={'TP 1': 'TP'}).drop(columns=['TP 2'], errors='ignore')
    pl = pl[['Sku','Style Id','Catalog','Category','Weight','TP','MRP Old','Final MRP Old',
             'Ajio MRP','Amazon MRP','Amazon FBA MRP','Flipkart MRP','Limeroad MRP',
             'Myntra MRP','Paytm MRP','Snapdeal MRP']]

    df = pd.concat([may, pl]).drop_duplicates(subset='Sku')
    price_cols = ['TP','MRP Old','Final MRP Old','Ajio MRP','Amazon MRP','Amazon FBA MRP',
                  'Flipkart MRP','Limeroad MRP','Myntra MRP','Paytm MRP','Snapdeal MRP']
    df[price_cols] = df[price_cols].replace('Nill', None)
    df[price_cols] = df[price_cols].apply(pd.to_numeric, errors='coerce')
    df = df.where(df.notna(), other=None)

    insert_missing_skus(cur, df['Sku'].tolist(), get_existing_skus(cur))

    for _, row in df.iterrows():
        cur.execute(
            """INSERT INTO product_pricing(sku,style_id,catalog,category,weight,tp,mrp_old,final_mrp_old,
               ajio_mrp,amazon_mrp,amazon_fba_mrp,flipkart_mrp,limeroad_mrp,myntra_mrp,paytm_mrp,snapdeal_mrp)
               VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING""",
            tuple(row)
        )
    print("product_pricing done")

    # ── amazon_sales  ←  Amazon Sale Report.csv
    df = pd.read_csv('data/Amazon Sale Report.csv', encoding='latin1', low_memory=False)
    df.columns = df.columns.str.strip()
    df = df[['Order ID','Date','Status','Fulfilment','Sales Channel','ship-service-level','Style','SKU',
             'Category','Size','ASIN','Courier Status','Qty','currency','Amount','ship-city','ship-state',
             'ship-postal-code','ship-country','promotion-ids','B2B','fulfilled-by']].drop_duplicates(subset='Order ID')
    df['Date'] = pd.to_datetime(df['Date'] ,format='mixed', errors='coerce')
    df['ship-postal-code'] = df['ship-postal-code'].astype(str)
    df['Qty'] = pd.to_numeric(df['Qty'], errors='coerce')
    df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce')
    df = df.where(df.notna(), other=None)

    insert_missing_skus(cur, df['SKU'].dropna().tolist(), get_existing_skus(cur))

    for _, row in df.iterrows():
        cur.execute(
            """INSERT INTO amazon_sales(order_id,date,status,fulfilment,sales_channel,ship_service_level,style,sku,
               category,size,asin,courier_status,qty,currency,amount,ship_city,ship_state,ship_postal_code,
               ship_country,promotion_ids,b2b,fulfilled_by)
               VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING""",
            tuple(row)
        )
    print("amazon_sales done")

    # ── international_sales  ←  International sale Report.csv
    df = pd.read_csv('data/International sale Report.csv', encoding='latin1')
    df.columns = df.columns.str.strip()
    df = df[['DATE','Months','CUSTOMER','Style','SKU','Size','PCS','RATE','GROSS AMT']]
    df['RATE'] = pd.to_numeric(df['RATE'], errors='coerce')
    df['GROSS AMT'] = pd.to_numeric(df['GROSS AMT'], errors='coerce')
    df = df.where(df.notna(), other=None)

    insert_missing_skus(cur, df['SKU'].dropna().tolist(), get_existing_skus(cur))

    for _, row in df.iterrows():
        cur.execute(
            """INSERT INTO international_sales(date,months,customer,style,sku,size,pcs,rate,gross_amt)
               VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING""",
            tuple(row)
        )
    print("international_sales done")

    # ── warehouse_comparison  ←  Cloud Warehouse Compersion Chart.csv
    df = pd.read_csv('data/Cloud Warehouse Compersion Chart.csv', encoding='latin1')
    df.columns = df.columns.str.strip()
    df = df[['Shiprocket','INCREFF']].dropna(how='all')
    df = df.where(df.notna(), other=None)
    for _, row in df.iterrows():
        cur.execute(
            "INSERT INTO warehouse_comparison(shiprocket,increff) VALUES (%s,%s)",
            tuple(row)
        )
    print("warehouse_comparison done")

    # ── expenses  ←  Expense IIGF.csv
    df = pd.read_csv('data/Expense IIGF.csv', encoding='latin1')
    df.columns = df.columns.str.strip()
    df = df[['Recived Amount','Expance']].dropna(how='all')
    df = df.where(df.notna(), other=None)
    for _, row in df.iterrows():
        cur.execute(
            "INSERT INTO expenses(received_amount,expense) VALUES (%s,%s)",
            tuple(row)
        )
    print("expenses done")

    connection.commit()
    print("All data inserted")

connection = get_connection()
insert_data(connection)