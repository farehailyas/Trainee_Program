import pandas as pd

df = pd.read_csv('data/International sale Report.csv', encoding='latin1')
df.columns = df.columns.str.strip()
df = df[['DATE', 'Months', 'CUSTOMER', 'Style', 'SKU', 'Size', 'PCS', 'RATE', 'GROSS AMT']]

# Check nulls BEFORE replacing
print(df.isnull().sum())
print("\nNull rows sample:")
print(df[df.isnull().any(axis=1)].head())