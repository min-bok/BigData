# 1. 각 사용자별로 첫 주문과 마지막 주문 사이의 시간 간격을 일 단위로 계산하시오
# 2. 시간 간격이 1일 이하인 사용자를 제외하고, 나머지 사용자들의 평균 시간 간격(일 단위)을 계산하시오
# 3. 평균 시간 간격보다 긴 시간 간격을 가진 사용자의 수를 정수로 구하시오

import pandas as pd

# user
# 주문시간

df = pd.read_csv("./delivery_time.csv")
# print(df.head())
# print(df.shape) # (1000, 7)

# print(df["주문시간"].dtype)
df["주문시간"] = pd.to_datetime(df["주문시간"])
# print(df["주문시간"].dtype)

# print(df.groupby(["user"])["주문시간"].min().reset_index())

min = df.groupby(["user"])["주문시간"].min().reset_index()
max = df.groupby(["user"])["주문시간"].max().reset_index()
diff = max["주문시간"] - min["주문시간"]

# print(df.shape)
df["diff"] = diff
# print(df.shape)

# print(df.head())
cond = df["diff"].dt.days > 0

df = df[cond]
# print(df.head())
# print(df.shape) # (297, 8)

# print(df["diff"].mean()) # 168 days 17:47:35.161616162
mean = df["diff"].mean()

cond2 = df["diff"] > mean
print(int(len(df[cond2])))


# print(dir(diff.dt))
# print(diff.dt.days <= 1)

# print(max - min)