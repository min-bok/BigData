# 1. 각 사용자별로 첫 주문과 마지막 주문 사이의 시간 간격을 일 단위로 계산하시오
# 2. 시간 간격이 1일 이하인 사용자를 제외하고, 나머지 사용자들의 평균 시간 간격(일 단위)을 계산하시오
# 3. 평균 시간 간격보다 긴 시간 간격을 가진 사용자의 수를 정수로 구하시오

import pandas as pd

df = pd.read_csv("./delivery_time.csv")
# print(df.head())

df["주문시간"] = pd.to_datetime(df["주문시간"])

min = df.groupby(["user"])["주문시간"].min().reset_index() # ⭐
max= df.groupby(["user"])["주문시간"].max().reset_index()

df["주문시간간격"] = max["주문시간"] - min["주문시간"]

cond = df["주문시간간격"].dt.days > 0

print(df[cond])

# print(df["주문시간간격"].dt.days > 0) # df["주문시간간격"].dt.days했을때 NaN도 나오는데

# print(df.groupby(["user"])["주문시간"].min())
