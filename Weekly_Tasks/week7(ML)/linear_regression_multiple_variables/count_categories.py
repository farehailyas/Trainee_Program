import duckdb

df = duckdb.read_csv("data/vehicle_price_prediction.csv")
result = duckdb.sql("SELECT COUNT(DISTINCT make) FROM df").fetchall()
print(result)

result = duckdb.sql("SELECT COUNT(DISTINCT model) FROM df").fetchall()
print(result)


result = duckdb.sql("SELECT COUNT(DISTINCT fuel_type) FROM df").fetchall()
print(result)

result = duckdb.sql("SELECT COUNT(DISTINCT transmission) FROM df").fetchall()
print(result)

result = duckdb.sql("SELECT COUNT(DISTINCT drivetrain) FROM df").fetchall()
print(result)

result = duckdb.sql("SELECT COUNT(DISTINCT body_type) FROM df").fetchall()
print(result)

result = duckdb.sql("SELECT COUNT(DISTINCT exterior_color) FROM df").fetchall()
print(result)

result = duckdb.sql("SELECT COUNT(DISTINCT interior_color) FROM df").fetchall()
print(result)

result = duckdb.sql("SELECT COUNT(DISTINCT accident_history) FROM df").fetchall()
print(result)

result = duckdb.sql("SELECT COUNT(DISTINCT seller_type) FROM df").fetchall()
print(result)

result = duckdb.sql("SELECT COUNT(DISTINCT condition) FROM df").fetchall()
print(result)

result = duckdb.sql("SELECT COUNT(DISTINCT trim) FROM df").fetchall()
print(result)

