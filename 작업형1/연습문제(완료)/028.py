# 1. 연도와 월을 기준으로 주문 수를 집계하시오
# 2. 가장 많은 주문이 있었던 연도와 월을 예시와 같은 형식으로 숫자로만 구하시오 (예: 2024년 2월인 경우 202402, 2024년 10월인 경우 202410)

import pandas as pd

df = pd.read_csv("delivery_time.csv")
# print(df.head())

# print(df["주문시간"].dtypes)
df["주문시간"] = pd.to_datetime(df["주문시간"])
# print(df["주문시간"].dtypes)

# print(df["주문시간"].dt.to_period("M"))

df["주문시간"] = df["주문시간"].dt.to_period("M")
# print(df.head())

주문량 = df.groupby(["주문시간"]).size()
print(str(주문량.idxmax()).replace("-", "")) # 202209

# cond = df["실제도착시간"].sort_values(ascending=False).values[0]

# print(cond)