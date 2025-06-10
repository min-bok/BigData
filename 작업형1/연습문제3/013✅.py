# 1. "f1" 컬럼에 결측치가 있는 데이터만 선택하시오
# 2. 선택된 데이터에서 "age" 컬럼의 평균값을 구하시오 (반올림 후 소수 첫째 자리까지 계산)

import pandas as pd

df = pd.read_csv("./type1_data1.csv")
# print(df.shape)

cond = df["f1"].isnull() == True
# cond = df["f1"].isnull() # 이렇게 쓰면됨

print(round(df[cond]["age"].mean(),1)) # 53.6