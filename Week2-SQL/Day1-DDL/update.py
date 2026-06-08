import sqlite3

con = sqlite3.Connection("mydb.db")
cur = con.cursor()

query = """ 
        UPDATE emp SET NAME = "Fareha Ilyas" WHERE ID = 1
"""
cur.execute(query)
con.commit()

print("Data updated successfully")