import duckdb

print("get albums table")
conn = duckdb.connect('postgres_to_duckdb.duckdb')
result = conn.execute("SELECT * FROM chinook_data.album").df()

print(result)

print('get artist table')

conn = duckdb.connect('postgres_to_duckdb.duckdb')
q = """SELECT * 
        FROM chinook_data.artist """
result = conn.execute(q).df()
print(result)