import sqlite3

con = sqlite3.Connection("mydb.db")
cr = con.cursor()

# read whole table
query = "SELECT * FROM emp"
cr.execute(query)

ans = cr.fetchall()
for i in ans:
    print(i)