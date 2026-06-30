import sqlite3

con = sqlite3.Connection("mydb.db")
cr = con.cursor()

# insert into db 
insert = """INSERT INTO emp VALUES(4,"FAREHA" ,"TRAINEE" , "1-06-2026")"""
cr.execute(insert)
con.commit()
