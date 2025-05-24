# 1. 주문 시간과 실제 도착 시간의 차이를 분 단위로 계산하시오
# 2. 앱 종류별 평균 도착 시간(분)을 계산하시오
# 3. 평균적으로 가장 빠른 앱 종류를 찾고, 해당 앱의 평균 도착 시간을 분으로 반올림하여 정수로 구하시오

import pandas as pd

df = pd.read_csv("./delivery_time.csv")
# print(df.head())

# df["주문시간"]
# df["실제도착시간"]

# print(df["주문시간"].dtype)
# print(df["실제도착시간"].dtype)

df["주문시간"] = pd.to_datetime(df["주문시간"])
df["실제도착시간"] = pd.to_datetime(df["실제도착시간"])

# print(df["주문시간"].dtype)
# print(df["실제도착시간"].dtype)

diff = df["실제도착시간"] - df["주문시간"]

# print(df["주문시간"].head())
# print(df["실제도착시간"].head())

# print(diff.dt.total_seconds() / 60)
df["차이"] = diff.dt.total_seconds() / 60
# print(dir(df["주문시간"].dt))

# print(df["차이"].head())

# df.groupby(["앱종류"])["차이"]

first = df.groupby(["앱종류"])["차이"].mean()

# print(df.groupby(["앱종류"])["차이"].mean().min())

# print(round(first.sort_values()[0])) # 62
# print(first.idxmin()) # 배고팡
print(first.sort_values().index[0]) # 배고팡


# print(help(df.groupby))