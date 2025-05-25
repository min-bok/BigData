# 1. 사용자별 주문 거리의 합계가 50km 이상인 사람들의 결제 방식을 구하시오
# 2. 이 결제 방식 중 가장 빈도가 높은 수를 구하시오
import pandas as pd

# 사용자: user
# 거리: 거리
# 결제방식: 결제종류

df = pd.read_csv("./delivery_time.csv")
# print(df.head())

# print(df.shape) # (1000, 7)

# print(df["user"].head())
# print(df["거리"].head())
# print(df["결제종류"].head())

result = df.groupby(["user"])["거리"].sum().reset_index()
# df["test"] = df.groupby(["user"])["거리"].sum().reset_index()

cond = result["거리"] >= 50

# print(result[cond]["user"])

print(df[df["user"].isin(result[cond]["user"])]["결제종류"].value_counts().values[0])
# print(df[df["user"].isin(result[cond]["user"])]["결제종류"].value_counts()[0]) # 이렇게 쓰면 안됨?
# c:\Users\leehy\Desktop\BigData\작업형1\연습문제\024.py:26: FutureWarning: Series.__getitem__ treating keys as positions is deprecated. In a future version, integer keys will always be treated as labels (consistent with DataFrame behavior). To access a value by position, use `ser.iloc[pos]`
#   print(df[df["user"].isin(result[cond]["user"])]["결제종류"].value_counts()[0]) # 이렇게 쓰면 안됨?