# 1. 연도와 월을 기준으로 주문 수를 집계하시오
# 2. 가장 많은 주문이 있었던 연도와 월을 예시와 같은 형식으로 숫자로만 구하시오 (예: 2024년 2월인 경우 202402, 2024년 10월인 경우 202410)

import pandas as pd

df = pd.read_csv("delivery_time.csv")
# print(df.head())

df["주문시간"] = pd.to_datetime(df["주문시간"])
df["주문시간"] = df["주문시간"].dt.to_period("M")

topMonth = df["주문시간"].value_counts().idxmax()
print(str(topMonth).replace("-", "")) # 202209
# print(df.head())