# 1. 예상 도착 시간보다 늦게 도착한 건수를 구하시오
# 2. 이 중 거리가 7km 이상인 데이터의 수를 정수로 구하시오

import pandas as pd

df = pd.read_csv("./delivery_time.csv")
# 예상도착시간, 실제도착시간, 거리
# print(df.head())
# print(df.shape)

df["예상도착시간"] = pd.to_datetime(df["예상도착시간"])
df["실제도착시간"] = pd.to_datetime(df["실제도착시간"])

# print(df["예상도착시간"].dtypes,  df["실제도착시간"].dtypes)
# print((df["실제도착시간"] - df["예상도착시간"]).dt.total_seconds() > 0)

cond = (df["실제도착시간"] - df["예상도착시간"]).dt.total_seconds() > 0

df = df[cond]
# print(df.shape)
cond2 = df["거리"] >= 7
# print(len(df[cond])) # 510
print(int(len(df[cond2]))) # 311