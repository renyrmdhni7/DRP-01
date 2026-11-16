import pandas as pd

df = pd.read_csv("Global_Stream.csv", sep=",")

print(df.shape)

print(df.head())

# cek kesehatan data
df.info()
print(df.isna().sum())

# cek duplicate
print("jumlah data duplicate", df.duplicated().sum())

# penulisan
print(df["Country"].value_counts())
print(df["Streaming Platform"].value_counts())
print(df["Top Genre"].value_counts())

# cek kolom dengan type int
print(df[["Age", "Minutes Streamed Per Day", "Number of Songs Liked"]].describe())

df = df.drop_duplicates()
df.info()