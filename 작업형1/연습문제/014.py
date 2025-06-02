# 1. 중복 데이터를 제거하시오
# 2. f3 컬럼의 결측치는 0 "silver"는 1 "gold"는 2 "vip"는 3으로 변환하시오
# 3. 변환된 f3 컬럼의 총합을 정수형으로 구하시오

import pandas as pd

df = pd.read_csv("./type1_data1.csv")
# print(df.head())

# print(df.shape)
df = df.drop_duplicates()
# print(df.shape)

# print(df.isnull().sum())
df["f3"] = df["f3"].fillna(0)
# print(df.isnull().sum())

df["f3"] = df["f3"].replace("silver", 1).replace("gold", 2).replace("vip", 3)
# print(df.head(15))

print(int(sum(df["f3"]))) # 167