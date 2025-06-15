# 1. 중복 데이터를 제거하시오
# 2. f3 컬럼의 결측치는 0 "silver"는 1 "gold"는 2 "vip"는 3으로 변환하시오
# 3. 변환된 f3 컬럼의 총합을 정수형으로 구하시오

import pandas as pd

df = pd.read_csv("./type1_data1.csv")
# print(df.head())
# print(df.isnull().sum())

df = df.drop_duplicates() # ⭐ 중복 데이터 제거

def encoder(val):
    if val == "silver":
        return 1
    elif val == "gold":
        return 2
    elif val == "vip":
        return 3

df["f3"] = df["f3"].apply(encoder)
# df["f3"] = df["f3"].replace("silver", 1).replace("gold", 2).replace("vip", 3) # ⭐ 해설지는 replace 사용
df["f3"] = df["f3"].fillna(0)
# print(df.isnull().sum())
# print(df["f3"].head(15))

print(int(df["f3"].sum())) # 167
