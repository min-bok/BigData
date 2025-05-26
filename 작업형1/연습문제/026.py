# 1. 주문이 가장 많이 발생한 연-월을 찾으시오
# 2. 해당 연-월에 '배고팡'앱을 통한 주문 중 '앱결제'로 결제된 주문의 비율을 계산하시오(반올림 후 소수 둘째자리까지 계산)

import pandas as pd

# 주문시간               실제도착시간               예상도착시간  앱종류     거리 결제종류      user

df = pd.read_csv("delivery_time.csv")

# print(df.head())

df["주문시간"] = pd.to_datetime(df["주문시간"])
# print(df["주문시간"].dtype)

# print(dir(df["주문시간"].dt))

# print(df["주문시간"].dt.to_period("M"))

df["주문시간"] = df["주문시간"].dt.to_period("M")

# df.groupby(["주문시간"]).max().reset_index()

# print(df["주문시간"].value_counts().index[0])
최다주문 = df["주문시간"].value_counts().index[0]

cond = df["주문시간"] == 최다주문
cond2 = df["앱종류"] == "배고팡"

filterdDf = df[cond & cond2]

cond3 = filterdDf["결제종류"] == "앱결제"

print(round(len(filterdDf[cond3]) / len(filterdDf), 2)) # 0.31

# print(df.groupby(["주문시간"]).max().reset_index())

# print(help(pd.Series.dt.to_period))