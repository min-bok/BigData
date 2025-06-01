# 1. f5 컬럼이 0이 아닌 데이터(행)를 구하시오
# 2. 앞에서 구한 데이터에 views 컬럼 결측치를 views 컬럼의 최솟값으로 채워주세요
# 3. 그리고 views 컬럼의 중앙값을 계산해 정수로 구하시오

import pandas as pd

df = pd.read_csv("type1_data1.csv")
# print(df.head())

# print(df.shape)
cond1 = df["f5"] != 0
df = df[cond1]
# print(df.shape)

min = df["views"].min()
# print(df.isnull().sum())
df["views"] = df["views"].fillna(min)
# print(df.isnull().sum())

median = df['views'].median()
print(int(median)) # 5924

# print(min)