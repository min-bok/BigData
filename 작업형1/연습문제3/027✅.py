# 1. 점심시간(10시부터 13시 전까지)에 주문된 배달 데이터를 찾으시오
# 2. 점심시간 주문 건 중 과속(평균 속도가 50km/h 이상)하는 주문 수를 정수로 구하시오
# 배달시간 = 실제도착시간 - 주문시간
# 속도(km/h) = 거리/시간(h)

import pandas as pd

# 주문시간, 실제도착시간, 거리
df = pd.read_csv("delivery_time.csv")
# print(df.shape)

df["주문시간"] = pd.to_datetime(df["주문시간"])

# cond = 10 <= df["주문시간"].dt.hour < 13
cond1 = df["주문시간"].dt.hour >= 10
cond2 = df["주문시간"].dt.hour < 13

new = df[cond1 & cond2].copy()
new["실제도착시간"] = pd.to_datetime(new["실제도착시간"])

h = (new["실제도착시간"] - new["주문시간"]).dt.total_seconds() / 60 / 60
new["속도"] = new["거리"]/h

cond3 = new["속도"] >= 50

print(int(len(new[cond3]))) # 1