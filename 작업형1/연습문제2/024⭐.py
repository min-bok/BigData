# 1. 사용자별 주문 거리의 합계가 50km 이상인 사람들의 결제 방식을 구하시오
# 2. 이 결제 방식 중 가장 빈도가 높은 수를 구하시오
import pandas as pd

df = pd.read_csv("./delivery_time.csv")

# user, 거리, 결제종류
# print(df.head())

filtered = df.groupby(["user"])["거리"].sum().reset_index()
cond = filtered["거리"] > 50

filtered = filtered[cond]

print(df[df["user"].isin(filtered["user"])]["결제종류"].value_counts().values[0]) # ⭐ isin
# 48

# print(filtered.shape)

# print(filtered[cond]["결제종류"].mode())
# print(filtered["거리"])