# 1. 결측치를 바로 뒤에 있는 값으로 대체하시오 (바로 뒤의 값도 결측치일 경우, 뒤에 있는 데이터 중 가장 가까운 값으로 대체)
# 2. city와 f2 컬럼을 기준으로 그룹합을 계산하시오
# 3. views 값이 세번째로 큰 city 이름을 구하시오

import pandas as pd

df = pd.read_csv("./type1_data1.csv")

# print(df.isnull().sum())
# df = df.fillna(method="bfill")
df = df.bfill()
# print(df.isnull().sum())

df = df.groupby(["city", "f2"]).sum()
df = df.sort_values("views", ascending=False)

print(df.index[2][0]) # 경기