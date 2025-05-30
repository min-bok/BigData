# 1. 결측치가 있는 데이터(행) 삭제
# 2. views 컬럼을 f1컬럼으로 나눈 값을 새로운 컬럼으로 추가
# 3. 새로운 컬럼 값 중 가장 큰 값을 가진 행의 age를 정수로 구하기

import pandas as pd

df = pd.read_csv("type1_data1.csv")

# print(df.head())
# print(df.isnull().sum())
# print(df.shape) # (120, 10)

df = df.dropna()

# print(df.isnull().sum())
# print(df.shape) # (70, 10)

# print(df["views"].dtypes, df["f1"].dtypes)
# print(df["views"]/df["f1"])

df["new"] = df["views"]/df["f1"]

cond = df["new"] == df["new"].max()

print(int(df[cond]["age"].values[0]))