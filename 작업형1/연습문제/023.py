# 1. 각 결제 종류별로 실제 도착 시간이 예상 도착 시간보다 늦은 주문의 비율을 계산하시오
# 2. 비율 중 가장 큰 값을 반올림하여 소수 둘째 자리까지 구하시오

import pandas as pd

# 실제도착시간
# 예상도착시간
# 결제종류

df = pd.read_csv("./delivery_time.csv")
# print(df.head())

# print(df["실제도착시간"].dtype)
# print(df["예상도착시간"].dtype)
# print(df["결제종류"].dtype)

df["실제도착시간"] = pd.to_datetime(df["실제도착시간"])
df["예상도착시간"] = pd.to_datetime(df["예상도착시간"])
# print(df["실제도착시간"].dtype)
# print(df["예상도착시간"].dtype)

diff = (df["실제도착시간"] - df["예상도착시간"]).dt.total_seconds()
df["차이"] = diff

df["지연"] = df["실제도착시간"] > df["예상도착시간"]

result = df.groupby(["결제종류"])["지연"].mean().max()
print(round(result, 2)) # 0.56

