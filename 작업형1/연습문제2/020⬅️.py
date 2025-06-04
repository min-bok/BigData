# 1. 연도 구분 없이 월별로 숫자형 컬럼의 합을 구하시오
# 2. 합계 중 views가 가장 작은 값을 가진 월을 정수로 구하시오

import pandas as pd

df = pd.read_csv("./type1_data1.csv")

df["subscribed"] = pd.to_datetime(df["subscribed"])
df["subscribed"] = df["subscribed"].dt.to_period("M")

df = df.groupby(["subscribed"]).sum(numeric_only=True)

cond = df["views"] == df["views"].min()
print(df.sort_values("views"))

# print(type(str(result.index[0])))
print(int(str(df[cond].index[0]).split("-")[1])) # 1
# print(df["subscribed"].head())

# print(dir(df["subscribed"].dt.to_period("M")))
# print(df["subscribed"].dtypes)
