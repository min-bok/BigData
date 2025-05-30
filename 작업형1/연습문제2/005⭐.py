# 1. f4 컬럼 데이터에 FJ가 포함된 데이터를 찾으시오
# 2. 찾은 데이터 중에서 f2 컬럼의 평균값을 구하시오(반올림 후 소수 둘째자리까지 계산)

import pandas as pd

df = pd.read_csv("./type1_data1.csv")

# print(df.head())

cond = df["f4"].str.contains("FJ") # ⭐

# print(help(df["f4"].str.contains))

df = df[cond]

# print(df.head(10))
print(round(df["f2"].mean(),2)) # 0.61