# 1. subscribed 컬럼이 2024년 2월인 데이터를 찾으시오
# 2. 위에서 찾은 데이터 중 f3 컬럼이 gold인 데이터의 개수를 구하시오
import pandas as pd

df = pd.read_csv("./type1_data1.csv")
# print(df.head())

# print(df["subscribed"].dtypes)
df["subscribed"] = pd.to_datetime(df["subscribed"])
# print(df["subscribed"].dtypes)

df["subscribed"] = df["subscribed"].dt.to_period("M")

cond = df["subscribed"] == "2024-02"

filtered = df[cond]

cond2 = filtered["f3"] == "gold"

print(len(filtered[cond2])) # 5
