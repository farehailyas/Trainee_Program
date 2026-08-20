import duckdb
conn = duckdb.connect('rest_api_stackexchange_incremental.duckdb')
conn.execute("SELECT 1").show()
print("\nDuckDB connected! Type SQL commands or .exit to quit")
