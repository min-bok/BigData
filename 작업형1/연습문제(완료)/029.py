# 1. 배달료 계산 기준표에 따라 각 주문에 대한 배달료를 계산하시오
# 2. 월별로 배달료의 총합을 집계하시오
# 3. 배달료가 가장 많이 발생한 월을 찾고, 그 월의 총 배달료를 정수로 구하시오

# [배달료 기준표]
# - 5km 미만 : 2000원
# - 5km 이상 ~ 10km 미만: 4000원
# - 10km 이상 ~ 15km 미만 : 6000원
# - 15km 이상 ~ 20km 미만 : 8000원

import pandas as pd

df = pd.read_csv("delivery_time.csv")
# print(df.head())

# print(df["거리"])
def delivery_fee(distance):
    if distance < 5:
        return 2000
    elif 5 <= distance < 10:
        return 4000
    elif 10 <= distance < 15:
        return 6000
    elif 15 <= distance < 20:
        return 8000
    
df["배달료"] = df["거리"].apply(delivery_fee)


# print(df["주문시간"].dtypes)
df["주문시간"] = pd.to_datetime(df["주문시간"])
# print(df["주문시간"].dtypes)

df["주문시간"] = df["주문시간"].dt.to_period("M")

# print(df.head())

filtered = df.groupby(["주문시간"])["배달료"].sum()

print(int(filtered.max()))