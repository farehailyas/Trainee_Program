import pandas as pd
import numpy as np
import os
# panda series
s = pd.Series(np.array([1,2,"hello"]))
print(s)

st = pd.Series([1,2,3,4,4])
print(type(st.values))

# pandas dataframe
df = pd.DataFrame()
print(df)
lis = [1,2,4,4,5,6,8,9,0,]
df = pd.DataFrame(lis)
print(df)
print(type(df.values))
print("reading csv and getting info")
# reading csv in pandas
base = os.path.dirname(__file__) #give complete path
df = pd.read_csv(os.path.join(base,"..", "customers-100.csv") , index_col = 0) #".." to go one folder up 
# print(df.head())
# print(df[0])
# print(df.info())

# to check missing values
print(df.isnull().sum())

# to fill missing values
df["Email"] = df["Email"].fillna("NULL")
df["Phone 1"] = df["Phone 1"].fillna(0)

print(df.isnull().sum())
# filtering data
print("east richard city residents")
result = df["City"] == "East Richard"
result = df[result == True]

print(result)

# add new coloumns
df['full name'] = df['First Name'] + " " + df['Last Name']
df['age'] = 23
print(df.head())


# finding all cities that belong to same country
print("all cities that belong to same country")
print(df.groupby('Country')['City'].count())

# instead of loading all tha data at once which is larger than ram get data in chunks
print("data in chunks")
base = os.path.dirname(__file__) #give complete path
for data in pd.read_csv(os.path.join(base,"..", "customers-100.csv"), chunksize = 50 , index_col = 0): #".." to go one folder up 
    df = pd.DataFrame(data)
    print(df.head())
# adjust sizes of diffrent coloumns of data


df = pd.read_csv(os.path.join(base,"..", "customers-100.csv") , index_col = 0 )
df['age'] = 23
print("memory usage before")
print(df.memory_usage(deep=True)) 
print()


df['age'] = df['age'].astype('int8')

print("memory usage after")
print(df.memory_usage(deep=True))
print()

print("using query")
# for clean filtering
res = df.query('Country == "Mali" and Website == "https://banks.biz/"')
print(res)

# math on large data 
df['combine_phone'] = df.eval('age + age')
print(df.head())  