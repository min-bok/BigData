# 1. f4 컬럼 데이터에 FJ가 포함된 데이터를 찾으시오
# 2. 찾은 데이터 중에서 f2 컬럼의 평균값을 구하시오(반올림 후 소수 둘째자리까지 계산)

import pandas as pd

df = pd.read_csv("./type1_data1.csv")
# print(df.shape)

cond = df["f4"].str.contains("FJ")
# df["f4"].str.contains("FJ", case=False) # 대소문자 구분없이 찾기

m = df[cond]["f2"].mean()

print(round(m, 2)) # 0.61