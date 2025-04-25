# 1. views 컬럼 값이 1000 이하인 데이터(결측치 제외)를 찾으시오
# 2. 앞에서 구한 데이터 중 f4 컬럼의 최빈값을 구하시오
import pandas as pd

df = pd.read_csv("./type1_data1.csv")
# print(df.head())

# print(df.isna().sum())
df = df.dropna(subset=["views"])
# print(df.isna().sum())

cond1 = (df["views"] <= 1000)
new = df[cond1]
# print(df["views"].sort_values())

# print(new["f4"].mode()[0])
print(new["f4"].value_counts().index[0])
