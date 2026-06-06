import sqlite3
import pandas as pd

# df = pd.read_csv("Sample - Superstore.csv"  , encoding = 'latin1')
connection = sqlite3.Connection("SuperstoreDb.db" )

# df.to_sql("superstore", connection, if_exists="replace", index=False)
# print("table created")

cursor = connection.cursor()

# See all columns
cursor.execute("PRAGMA table_info(superstore)")
print(cursor.fetchall())


print()

# Preview data
cursor.execute("SELECT * FROM superstore LIMIT 1")
print(cursor.fetchall())