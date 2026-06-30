import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv
import os
load_dotenv()

def create_db():
    try:
        conn = psycopg2.connect(
            host = os.getenv("DB_HOST"),
            port = os.getenv("DB_PORT"),
            database = "postgres",
            password = os.getenv("DB_PASSWORD"),
            user = os.getenv("DB_USER")
        )
        conn.autocommit = True
        db_name = os.getenv("DB_NAME")
        q = f"CREATE DATABASE {db_name} "
        cur = conn.cursor()
        # cur.execute(q)
        conn.commit()
        cur.close()
        conn.close()
        print(f"created db {db_name}")
    except Exception as e:
        print(f"Cannot connect to db {e}")


def connect_db():
    conn = psycopg2.connect(
        host = os.getenv("DB_HOST"),
        port = os.getenv("DB_PORT"),
        database = os.getenv("DB_NAME"),
        password = os.getenv("DB_PASSWORD"),
        user = os.getenv("DB_USER")
    )
    return conn
    
create_db()
conn = connect_db()
if conn:
    print("connected successfully")
else:
    print("Cant connect")