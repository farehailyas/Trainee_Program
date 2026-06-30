import sqlite3

con = sqlite3.connect("mydb.db")
cr = con.cursor()

print("connected to database")

# create table in my db
query = """ 
    CREATE TABLE emp(
        Id INTEGER PRIMARY KEY,
        Name VARCHAR(20),
        Designation VARCHAR(50),
        Joining DATE
    )
"""
cr.execute(query)
print("table created")