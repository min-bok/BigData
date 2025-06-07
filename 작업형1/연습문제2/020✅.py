# 1. 연도 구분 없이 월별로 숫자형 컬럼의 합을 구하시오
# 2. 합계 중 views가 가장 작은 값을 가진 월을 정수로 구하시오

import pandas as pd

df = pd.read_csv("./type1_data1.csv")
# print(df.shape)
# print(df.info())

df["subscribed"] = pd.to_datetime(df["subscribed"])
df["month"] = df["subscribed"].dt.month

filtered = df.groupby(["month"])[["age", "f1", "f2", "f5", "views"]].sum()
# filtered = df.groupby(["month"]).sum(numeric_only=True)

print(filtered["views"].idxmin()) # 11
# print(filtered["views"].sort_values().index[0])