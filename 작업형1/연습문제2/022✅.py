# 1. 주문 시간과 실제 도착 시간의 차이를 분 단위로 계산하시오
# 2. 앱 종류별 평균 도착 시간(분)을 계산하시오
# 3. 평균적으로 가장 빠른 앱 종류를 찾고, 해당 앱의 평균 도착 시간을 분으로 반올림하여 정수로 구하시오

import pandas as pd

# 앱종류, 주문시간, 실제도착시간
df = pd.read_csv("./delivery_time.csv")
# print(df.head())

df["주문시간"] = pd.to_datetime(df["주문시간"])
df["실제도착시간"] = pd.to_datetime(df["실제도착시간"])

df["diff"] = abs((df["주문시간"] - df["실제도착시간"]).dt.total_seconds()) / 60

result = df.groupby(["앱종류"])["diff"].mean()
print(int(round(result.min(),0))) # 62
print(result.idxmin()) # 배고팡


# print(df["diff"].head())

# print(df["주문시간"].dtypes, df["실제도착시간"].dtypes)