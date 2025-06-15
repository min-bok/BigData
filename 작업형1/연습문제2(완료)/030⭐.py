# 1. 주말 주문 건수와 평일 주문 건수를 구하시오
# 2. 주말 주문 건수와 평일 주문 건수의 차이를 절대값으로 구하고 정수형으로 구하시오
import pandas as pd

df = pd.read_csv("delivery_time.csv")
# print(df.head())
# print(df.shape)

df["주문시간"] = pd.to_datetime(df["주문시간"])
# print(dir(df["주문시간"].dt))

# print(dir(df["주문시간"].dt.dayofweek)) # ⭐ 0 → 월

df["주문요일"] = df["주문시간"].dt.dayofweek

주말주문건수 = len(df[df["주문요일"] >= 5])
평일주문건수 = len(df[df["주문요일"] < 5])

print(int(abs(주말주문건수 - 평일주문건수))) # 412