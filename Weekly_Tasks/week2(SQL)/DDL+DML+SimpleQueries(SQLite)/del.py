import sqlite3

con = sqlite3.Connection("mydb.db")

cur = con.cursor()

# delete from data
query = "DELETE FROM emp WHERE Id = 2"
cur.execute(query)
con.commit()