import pandas as pd

df = pd.read_csv("./type1_data1.csv")
# print(df.head())
# 시계열 데이터 처리

df = df["subscribed"].value_counts()

date = pd.to_datetime(df.index[0])
print(type(date)) # Timestamp

# print(int(df.index[0][-2:]))

print(int(date.day))