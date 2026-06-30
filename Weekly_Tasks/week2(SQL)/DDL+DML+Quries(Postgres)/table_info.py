import psycopg2 
from db_connection import get_dbConnection

# Get connection (auto-creates database)
def get_connection():    
    try:
        conn = get_dbConnection()
        print("Connected to db")
        return conn
    except Exception as e:
        print(e)
    
def get_tables_info(connection):
    cur = connection.cursor()
    cur.execute("""
    SELECT table_name 
    FROM information_schema.tables 
    WHERE table_schema = 'public'
    """)
    tables = cur.fetchall()
    print("Tables:", [t[0] for t in tables])
    
    # 2. GET COLUMNS OF A Sales table
    cur.execute("""
        SELECT column_name, data_type 
        FROM information_schema.columns 
        WHERE table_name = 'sales'
    """)
    columns = cur.fetchall()
    print("\nColumns in 'sales':")
    for col, dtype in columns:
        print(f"  {col}: {dtype}")

    # 3. GET COLUMNS OF A Customer table
    cur.execute("""
        SELECT column_name, data_type 
        FROM information_schema.columns 
        WHERE table_name = 'customers'
    """)
    columns = cur.fetchall()
    print("\nColumns in 'sales':")
    for col, dtype in columns:
        print(f"  {col}: {dtype}")

    # 4. GET COLUMNS OF A products table
    cur.execute("""
        SELECT column_name, data_type 
        FROM information_schema.columns 
        WHERE table_name = 'products'
    """)
    columns = cur.fetchall()
    print("\nColumns in 'sales':")
    for col, dtype in columns:
        print(f"  {col}: {dtype}")

    # 5. GET COLUMNS OF A orde table
    cur.execute("""
        SELECT column_name, data_type 
        FROM information_schema.columns 
        WHERE table_name = 'orders'
    """)
    columns = cur.fetchall()
    print("\nColumns in 'sales':")
    for col, dtype in columns:
        print(f"  {col}: {dtype}")


connection = get_connection()
get_tables_info(connection)