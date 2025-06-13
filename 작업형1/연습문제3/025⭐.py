# 1. 각 사용자별로 첫 주문과 마지막 주문 사이의 시간 간격을 일 단위로 계산하시오
# 2. 시간 간격이 1일 이하인 사용자를 제외하고, 나머지 사용자들의 평균 시간 간격(일 단위)을 계산하시오
# 3. 평균 시간 간격보다 긴 시간 간격을 가진 사용자의 수를 정수로 구하시오

import pandas as pd

df = pd.read_csv("./delivery_time.csv")
# print(df.shape)

df["주문시간"] = pd.to_datetime(df["주문시간"])

df = df.groupby(["user"])["주문시간"].agg(["min", "max"]).reset_index()
df["diff"] = (df["max"] - df["min"]).dt.days

cond = df["diff"] < 1

df = df[~cond]

m = df["diff"].mean()

print(len(df[df["diff"] > m])) # 146