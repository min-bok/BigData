# 1. views 컬럼의 결측 데이터를 0으로 대체하시오
# 2. views 컬럼에서 상위 10번째 값을 구하시오
# 3. views 컬럼에서 상위 10개의 값을 상위 10번째 값으로 대체하시오
# 4. views 컬럼의 전체 합을 정수로 구하시오

import pandas as pd

df = pd.read_csv("./type1_data1.csv")

# print(df.head())

# print(df["views"].isnull().sum())
df["views"] = df["views"].fillna(0)
# print(df["views"].isnull().sum())

df = df.sort_values(["views"])

# print(df.head(15))

top10 = df["views"].iloc[9:10].values[0]

df.loc[df.index[:10], "views"] = top10 # ⭐ df.loc[행_선택, 열_선택]
# print(df.head(15))
# print(int(df["views"].sum()))




# print(df.iloc[:10]["views"])