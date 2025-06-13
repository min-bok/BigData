# 1. 사용자별 주문 거리의 합계가 50km 이상인 사람들의 결제 방식을 구하시오
# 2. 이 결제 방식 중 가장 빈도가 높은 수를 구하시오
import pandas as pd

df = pd.read_csv("./delivery_time.csv")
# print(df.shape)

new_df = df.groupby(["user"])["거리"].sum().reset_index()
filtered = new_df[new_df["거리"] >= 50]
# print(filtered.shape) # (28, 2)

# print(df["user"].isin(filtered["user"]))

print(df[df["user"].isin(filtered["user"])]["결제종류"].value_counts().values[0]) # 48