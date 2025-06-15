# 1. 연도 구분 없이 월별로 숫자형 컬럼의 합을 구하시오
# 2. 합계 중 views가 가장 작은 값을 가진 월을 정수로 구하시오

import pandas as pd

df = pd.read_csv("./type1_data1.csv")
# print(df.head())

# print(df["subscribed"].dtype)
df["subscribed"] = pd.to_datetime(df["subscribed"])
# print(df["subscribed"].dtype)

df["month"] = df["subscribed"].dt.month # 파생변수 생성

df = df.groupby(["month"]).sum(numeric_only=True)

print(df.sort_values("views").index[0])
print(df["views"].sort_values().index[0])