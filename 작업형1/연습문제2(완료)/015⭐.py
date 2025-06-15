# 1. 주어진 데이터에서 문자 자료형 컬럼을 삭제하시오
# 2. 숫자 자료형 컬럼의 결측치를 0으로 대체하시오
# 3. 각 행의 합이 3000보다 큰 값의 개수를 정수로 구하시오 (각 행의 합: age + f1 + f2 + f5 + views)

import pandas as pd

df = pd.read_csv("type1_data1.csv")
# print(df.head())
# print(dir(df))
# print(df.select_dtypes(include="object").columns.tolist())
# print(df.shape)

df = df.drop(columns=df.select_dtypes(include="object").columns.tolist()) # ⭐
# print(df.head())

# print(df.isnull().sum())
df = df.fillna(0)
# print(df.isnull().sum())

print(len(df[df.sum(axis=1) > 3000])) # 88

# print(df.select_dtypes(include="object").columns.tolist())
# print(help(df.drop))
