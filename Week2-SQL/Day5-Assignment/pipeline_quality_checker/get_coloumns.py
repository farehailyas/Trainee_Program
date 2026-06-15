import duckdb

# Get column info from all 3 CSV files
csv_files = [
    'data/Amazon Sale Report.csv',
    'data/Cloud Warehouse Compersion Chart.csv',  # replace with your actual file names
    'data/Expense IIGF.csv',
    'data/International sale Report.csv',
    'data/May-2022.csv',
    'data/P  L March 2021.csv',
    'data/Sale Report.csv'
    ''
]

for file in csv_files:
    print(f"\n{'='*60}")
    print(f"FILE: {file}")
    print(f"{'='*60}")
    
    # Get all columns and types
    q = f"DESCRIBE '{file}'"
    schema = duckdb.query(q)
    print(schema)
    
    # # Also get row count
    # count_q = f"SELECT COUNT(*) as row_count FROM '{file}'"
    # count = duckdb.query(count_q).to_df()
    # print(f"\nTotal Rows: {count['row_count'][0]}")