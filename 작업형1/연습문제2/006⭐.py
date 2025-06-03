# 1. f3컬럼이 gold이면서 f2컬럼이 2인 데이터를 찾으시오
# 2. 찾은 데이터에서 f1 컬럼의 분산을 구하시오 (반올림 후 소수 둘째 자리까지 계산)

import pandas as pd

df = pd.read_csv("./type1_data1.csv")
# print(df.head())
# print(df["f2"].dtypes) # int64

cond1 = df["f3"] == "gold"
cond2 = df["f2"] == 2

temp = df[(cond1) & (cond2)] # ⭐

print(round(temp["f1"].var(),2)) # ⭐