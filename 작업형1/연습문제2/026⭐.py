# 1. 주문이 가장 많이 발생한 연-월을 찾으시오
# 2. 해당 연-월에 '배고팡'앱을 통한 주문 중 '앱결제'로 결제된 주문의 비율을 계산하시오(반올림 후 소수 둘째자리까지 계산)

import pandas as pd

df = pd.read_csv("delivery_time.csv")

# print(df.shape) # (1000, 7)
# print(df["주문시간"].dtypes)
df["주문시간"] = pd.to_datetime(df["주문시간"])
# print(df["주문시간"].dtypes)
df["주문시간"] = df["주문시간"].dt.to_period("M")

month = df["주문시간"].value_counts().idxmax()
# print(df.head())
# print(df.shape) # (1000, 7)

cond = (df["주문시간"] == month) & (df["앱종류"] == "배고팡")
filtered = df[cond]

ratio = (filtered["결제종류"] == "앱결제").mean() # ⭐

print(round(ratio, 2)) # 0.31

# print(df["주문시간"].value_counts().idxmax())