# 1. 데이터에서 결측치가 있는 데이터(행)을 모두 제거하시오
# 2. 결측치가 제거된 데이터를 사용하여 앞에서부터 70% 데이터를 구하시오(단, 데이터 70% 지점의 index가 소수점으로 계산될 경우 소수점 이하는 버림)
# 3. 앞에서 구한 70% 데이터 중 views 컬럼의 3사분위수에서 1사분위수를 뺀 값을 정수로 구하시오

import pandas as pd

df = pd.read_csv("./type1_data1.csv")
# print(df.head())

# print(df.isnull().sum())
# print(df.shape)
df = df.dropna()
# print(df.isnull().sum())
# print(df.shape)

filtered = df.iloc[:int(df.shape[0] * 0.7)]

q1 = filtered["views"].quantile(0.25)
q3 = filtered["views"].quantile(0.75)

print(int(q3 - q1)) # 2771