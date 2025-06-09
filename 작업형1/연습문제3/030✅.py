# 1. 주말 주문 건수와 평일 주문 건수를 구하시오
# 2. 주말 주문 건수와 평일 주문 건수의 차이를 절대값으로 구하고 정수형으로 구하시오
import pandas as pd

df = pd.read_csv("delivery_time.csv")
# print(df.head())

df["주문시간"] = pd.to_datetime(df["주문시간"])

# 01234 / 56

df["주문시간"] = df["주문시간"].dt.dayofweek

평일 = df["주문시간"] < 5
주말 = df["주문시간"] >= 5

주문건수차이 = len(df[평일]) - len(df[주말])

print(abs(주문건수차이)) # 412

# print(df["주문시간"].isnull().sum())