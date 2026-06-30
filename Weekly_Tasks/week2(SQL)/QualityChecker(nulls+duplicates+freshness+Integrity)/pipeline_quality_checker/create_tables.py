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

def create_tables(conn):

    cur = conn.cursor()
    inventory = """CREATE TABLE IF NOT EXISTS inventory (
        id              SERIAL,
        sku_code        TEXT,
        design_no       TEXT,
        stock           FLOAT,
        category        TEXT,
        size            TEXT,
        color           TEXT,
        inserted_at     TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )"""

    product_pricing = """CREATE TABLE IF NOT EXISTS product_pricing (
        id              SERIAL,
        sku             TEXT,
        style_id        TEXT,
        catalog         TEXT,
        category        TEXT,
        weight          TEXT,
        tp              TEXT,
        mrp_old         TEXT,
        final_mrp_old   TEXT,
        ajio_mrp        TEXT,
        amazon_mrp      TEXT,
        amazon_fba_mrp  TEXT,
        flipkart_mrp    TEXT,
        limeroad_mrp    TEXT,
        myntra_mrp      TEXT,
        paytm_mrp       TEXT,
        snapdeal_mrp    TEXT,
        inserted_at     TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )"""

    amazon_sales = """CREATE TABLE IF NOT EXISTS amazon_sales (
        id                  SERIAL,
        order_id            TEXT,
        date                DATE,
        status              TEXT,
        fulfilment          TEXT,
        sales_channel       TEXT,
        ship_service_level  TEXT,
        style               TEXT,
        sku                 TEXT,
        category            TEXT,
        size                TEXT,
        asin                TEXT,
        courier_status      TEXT,
        qty                 INTEGER,
        currency            TEXT,
        amount              FLOAT,
        ship_city           TEXT,
        ship_state          TEXT,
        ship_postal_code    TEXT,
        ship_country        TEXT,
        promotion_ids       TEXT,
        b2b                 BOOLEAN,
        fulfilled_by        TEXT,
        inserted_at         TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )"""

    international_sales = """CREATE TABLE IF NOT EXISTS international_sales (
        id          SERIAL,
        date        TEXT,
        months      TEXT,
        customer    TEXT,
        style       TEXT,
        sku         TEXT,
        size        TEXT,
        pcs         TEXT,
        rate        TEXT,
        gross_amt   TEXT,
        inserted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )"""

    warehouse_comparison = """CREATE TABLE IF NOT EXISTS warehouse_comparison (
        id          SERIAL PRIMARY KEY,
        shiprocket  TEXT,
        increff     TEXT,
        inserted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )"""

    expenses = """CREATE TABLE IF NOT EXISTS expenses (
        id              SERIAL PRIMARY KEY,
        received_amount TEXT,
        expense         TEXT,
        inserted_at     TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )"""

    cur.execute(inventory)
    cur.execute(product_pricing)
    cur.execute(amazon_sales)
    cur.execute(international_sales)
    cur.execute(warehouse_comparison)
    cur.execute(expenses)

    conn.commit()
    print("tables created successfully")

conn = get_connection()
create_tables(conn)