# 1. 주어진 데이터에서 문자 자료형 컬럼을 삭제하시오
# 2. 숫자 자료형 컬럼의 결측치를 0으로 대체하시오
# 3. 각 행의 합이 3000보다 큰 값의 개수를 정수로 구하시오 (각 행의 합: age + f1 + f2 + f5 + views)

import pandas as pd

df = pd.read_csv("type1_data1.csv")
# print(df.head())

objCols = df.select_dtypes(exclude="object").columns
df = df[objCols]
# print(objCols)
# print(df.head())

# print(df.info())
# print(df.isnull().sum())

df = df.fillna(0)
# print(df.head())
# print(df.isnull().sum())

df = df.T # 행열전환

print(int(sum(df.sum() > 3000)))
