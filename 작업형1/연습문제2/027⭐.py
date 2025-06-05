# 1. 점심시간(10시부터 13시 전까지)에 주문된 배달 데이터를 찾으시오
# 2. 점심시간 주문 건 중 과속(평균 속도가 50km/h 이상)하는 주문 수를 정수로 구하시오
# 배달시간 = 실제도착시간 - 주문시간
# 속도(km/h) = 거리/시간(h)

import pandas as pd

# 주문시간, 실제도착시간, 거리
df = pd.read_csv("delivery_time.csv")
# print(df.head())

df["실제도착시간"] = pd.to_datetime(df["실제도착시간"])
df["주문시간"] = pd.to_datetime(df["주문시간"])

# print(df.shape) # (1000, 7)

cond1 = df["주문시간"].dt.hour >= 10 # ⭐ dt.hour
cond2 = df["주문시간"].dt.hour < 13

# print(df[cond1 & cond2].shape) # (120, 7)

temp = df[cond1 & cond2].copy()
# print(temp.head())

시간 = (temp["실제도착시간"] - temp["주문시간"]).dt.total_seconds() / 60 / 60
속도 = temp["거리"]/시간

temp["속도"] = 속도

cond3 = temp["속도"] >= 50
print(len(temp[cond3])) # 1