# 1. 예상 도착 시간보다 늦게 도착한 건수를 구하시오
# 2. 이 중 거리가 7km 이상인 데이터의 수를 정수로 구하시오

import pandas as pd

df = pd.read_csv("./delivery_time.csv")
# print(df.head())

# print(df["실제도착시간"].head())
# print(df["예상도착시간"].head())

# print(df["실제도착시간"].dtype)
# print(df["예상도착시간"].dtype)

df["실제도착시간"] = pd.to_datetime(df["실제도착시간"])
df["예상도착시간"] = pd.to_datetime(df["예상도착시간"])

# print(df["실제도착시간"].dtype)
# print(df["예상도착시간"].dtype)

# print(dir(df["실제도착시간"].dt.timetz))

df["지연시간"] = (df["실제도착시간"] - df["예상도착시간"]).dt.total_seconds()/60
# print(df["지연시간"])

cond1 = df["지연시간"] > 0

print(len(df[cond1])) # 지연된 건수 510건

cond2 = df["거리"] > 7
# print(df[cond2])

# print(df["거리"].dtype)

print(len(df[cond1&cond2])) # 311건

# 'time', 'timetz'