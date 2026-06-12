import pandas as pd
from db_connection import get_dbConnection

def get_connection():
    try:
        conn = get_dbConnection()
        print("Connected to db")
        return conn
    except Exception as e:
        print(e)

def create_tables(connection):
    try:
        cur = connection.cursor()

        # Root table — no FK dependencies
        # PK: sku_code — every product SKU must exist here first
        inventory = """CREATE TABLE IF NOT EXISTS inventory (
            sku_code    TEXT        PRIMARY KEY,
            design_no   TEXT,
            stock       FLOAT,
            category    TEXT,
            size        TEXT,
            color       TEXT
        )"""

        # Depends on: inventory
        # PK: sku — one pricing record per SKU
        # FK: sku → inventory.sku_code (a price sheet row must have a real product)
        product_pricing = """CREATE TABLE IF NOT EXISTS product_pricing (
            sku             TEXT        PRIMARY KEY,
            style_id        TEXT,
            catalog         TEXT,
            category        TEXT,
            weight          TEXT,
            tp              FLOAT,
            mrp_old         FLOAT,
            final_mrp_old   FLOAT,
            ajio_mrp        FLOAT,
            amazon_mrp      FLOAT,
            amazon_fba_mrp  FLOAT,
            flipkart_mrp    FLOAT,
            limeroad_mrp    FLOAT,
            myntra_mrp      FLOAT,
            paytm_mrp       FLOAT,
            snapdeal_mrp    FLOAT,
            FOREIGN KEY (sku) REFERENCES inventory(sku_code)
        )"""

        # Depends on: inventory
        # PK: order_id — one row per Amazon order line
        # FK: sku → inventory.sku_code (every sold item must exist in inventory)
        amazon_sales = """CREATE TABLE IF NOT EXISTS amazon_sales (
            order_id            TEXT        PRIMARY KEY,
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
            FOREIGN KEY (sku) REFERENCES inventory(sku_code)
        )"""

        # Depends on: inventory
        # PK: composite (date, customer, sku, size) — no single unique col exists
        # FK: sku → inventory.sku_code
        international_sales = """CREATE TABLE IF NOT EXISTS international_sales (
            date        TEXT,
            months      TEXT,
            customer    TEXT,
            style       TEXT,
            sku         TEXT,
            size        TEXT,
            pcs         TEXT,
            rate        FLOAT,
            gross_amt   FLOAT,
            PRIMARY KEY (date, customer, sku, size),
            FOREIGN KEY (sku) REFERENCES inventory(sku_code)
        )"""

        # No natural PK, no FK — lookup/reference table only
        warehouse_comparison = """CREATE TABLE IF NOT EXISTS warehouse_comparison (
            id          SERIAL      PRIMARY KEY,
            shiprocket  TEXT,
            increff     TEXT
        )"""

        # No natural PK, no FK — financial log, append-only
        expenses = """CREATE TABLE IF NOT EXISTS expenses (
            id              SERIAL  PRIMARY KEY,
            received_amount TEXT,
            expense         TEXT
        )"""

        # Order matters — parent tables first
        cur.execute(inventory)
        cur.execute(product_pricing)
        cur.execute(amazon_sales)
        cur.execute(international_sales)
        cur.execute(warehouse_comparison)
        cur.execute(expenses)

        connection.commit()
        print("Tables created successfully")
    except Exception as e:
        print("Error:", e)

connection = get_connection()
create_tables(connection)