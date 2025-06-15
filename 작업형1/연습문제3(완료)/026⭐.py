# 1. 주문이 가장 많이 발생한 연-월을 찾으시오
# 2. 해당 연-월에 '배고팡'앱을 통한 주문 중 '앱결제'로 결제된 주문의 비율을 계산하시오(반올림 후 소수 둘째자리까지 계산)

import pandas as pd

df = pd.read_csv("delivery_time.csv")
# print(df.shape) # (1000, 7)

df["주문시간"] = pd.to_datetime(df["주문시간"])
df["주문시간"] = df["주문시간"].dt.to_period("M")

month = df["주문시간"].mode()[0]

cond1 = df["주문시간"] == month
cond2 = df["앱종류"] == "배고팡"
cond3 = df["결제종류"] == "앱결제"

total = len(df[cond1])
part = len(df[cond1 & cond2 & cond3])

print(round(part / total, 2))

# 0.31