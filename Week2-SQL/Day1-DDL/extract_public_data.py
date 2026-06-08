import sqlite3
import pandas as pd

df = pd.read_csv("Sample - Superstore.csv")


connection = sqlite3.Connection("SuperstoreDb.db")

df.to_sql("superstore", conn, if_exists="replace", index=False)
print("table created")