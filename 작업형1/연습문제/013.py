# 1. "f1" 컬럼에 결측치가 있는 데이터만 선택하시오
# 2. 선택된 데이터에서 "age" 컬럼의 평균값을 구하시오

import pandas as pd
df = pd.read_csv("./type1_data1.csv")

# print(df.head())

temp = df[df["f1"].isnull()]

print(temp["age"].mean())