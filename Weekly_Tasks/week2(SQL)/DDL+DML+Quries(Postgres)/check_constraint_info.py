import psycopg2
from db_connection import get_dbConnection

conn = get_dbConnection()
cur = conn.cursor()

# 1. PRIMARY KEY
print("PRIMARY KEYS:")
print("-" * 50)
cur.execute("""
    SELECT tc.table_name, kcu.column_name
    FROM information_schema.table_constraints tc
    JOIN information_schema.key_column_usage kcu
        ON tc.constraint_name = kcu.constraint_name
    WHERE tc.constraint_type = 'PRIMARY KEY'
""")
for table, col in cur.fetchall():
    print(f"{table}: {col} 🔑")

# 2. FOREIGN KEYS
print("\n\nFOREIGN KEYS:")
print("-" * 50)
cur.execute("""
    SELECT 
        tc.table_name, 
        kcu.column_name,
        ccu.table_name,
        ccu.column_name
    FROM information_schema.table_constraints tc
    JOIN information_schema.key_column_usage kcu
        ON tc.constraint_name = kcu.constraint_name
    JOIN information_schema.constraint_column_usage ccu
        ON ccu.constraint_name = tc.constraint_name
    WHERE tc.constraint_type = 'FOREIGN KEY'
""")
for table, col, ftable, fcol in cur.fetchall():
    print(f"{table}.{col} → {ftable}.{fcol} 🔗")

# 3. NOT NULL
print("\n\nNOT NULL:")
print("-" * 50)
cur.execute("""
    SELECT table_name, column_name
    FROM information_schema.columns
    WHERE is_nullable = 'NO' AND table_schema = 'public'
""")
for table, col in cur.fetchall():
    print(f"{table}.{col}")

cur.close()
conn.close()