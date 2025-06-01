# 1. 모든 나이(age)에 1을 더하시오
# 2. 20대의 views 평균과 30대의 views 평균의 절댓값 차이를 구하시오. (반올림 후 소수 둘째 자리까지 계산)

import pandas as pd

df = pd.read_csv("./type1_data1.csv")

df["age"] = df["age"] + 1

df_20대 = df[(df["age"] >= 20) & (df["age"] < 30)]
df_30대 = df[(df["age"] >= 30) & (df["age"] < 40)]

# print(df_20대["views"].mean())
# print(df_30대["views"].mean())

print(round(abs(df_20대["views"].mean() - df_30대["views"].mean()),2)) # 263.13