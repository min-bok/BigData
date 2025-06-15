# 1. 주말 주문 건수와 평일 주문 건수를 구하시오
# 2. 주말 주문 건수와 평일 주문 건수의 차이를 절대값으로 구하고 정수형으로 구하시오
import pandas as pd

df = pd.read_csv("delivery_time.csv")

# print(df.head())
# print(df["주문시간"].dtypes)
df["주문시간"] = pd.to_datetime(df["주문시간"])
# print(df["주문시간"].dtypes)

# print(df["주문시간"].dt.dayofweek) # 0: 월
# print(help(df["주문시간"].dt.dayofweek))

주말 = df[df["주문시간"].dt.dayofweek >= 5]
평일 = df[df["주문시간"].dt.dayofweek < 5]

# print(len(주말), len(평일))
print(int(abs(len(주말) - len(주말)))) # 412

# df["주말"] = df["주문시간"].dt.dayofweek >= 5
# print(df.head(15))