# 1. subscribed 컬럼이 2024년 2월인 데이터를 찾으시오
# 2. 위에서 찾은 데이터 중 f3 컬럼이 gold인 데이터의 개수를 구하시오
import pandas as pd

df = pd.read_csv("./type1_data1.csv")
# print(df.head())

df["subscribed"] = pd.to_datetime(df["subscribed"])
# print(df.info())

# print(df["subscribed"].dt.year)
df["year"] = df["subscribed"].dt.year
df["month"] = df["subscribed"].dt.month
# print(df.head())

cond1 = (df["year"] == 2024) & (df["month"] == 2)

new = df[cond1]

cond2 = new["f3"] == "gold"

print(len(new[cond2]))

