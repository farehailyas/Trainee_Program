import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv
import os
from pathlib import Path
import pandas as pd
env_path = Path(__file__).parent.parent / ".env"
load_dotenv(env_path)

def create_db():
    try:
        db_name = os.getenv("DB_NAME")
        temp_connection = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            database="postgres",
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )
        temp_connection.autocommit = True  
        cur = temp_connection.cursor()
        cur.execute(f"CREATE DATABASE {db_name};")
        print(f"databse name {db_name}")
        cur.close()
        temp_connection.close()  # close temporary connection
        # return db_name
    except Exception:
        print("Db already exist")


def get_dbConnection():
    create_db()
    connection = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )
    print(f"database name {os.getenv("DB_NAME")}")
    return connection

def destroy_connection(conn):
    conn.close()
