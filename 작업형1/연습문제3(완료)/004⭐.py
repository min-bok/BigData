# 1. views 컬럼의 결측 데이터를 0으로 대체하시오
# 2. views 컬럼에서 상위 10번째 값을 구하시오
# 3. views 컬럼에서 상위 10개의 값을 상위 10번째 값으로 대체하시오
# 4. views 컬럼의 전체 합을 정수로 구하시오

import pandas as pd

df = pd.read_csv("./type1_data1.csv")
# print(df.head())

df["views"] = df["views"].fillna(0)
# print(df.isnull().sum())

df = df.sort_values("views", ascending=False)
views_min = df.iloc[:10]["views"].min()

df.iloc[:10, -1] = views_min # ⭐
# print(views_min)
# print(df.head())

print(int(df["views"].sum())) # 652812