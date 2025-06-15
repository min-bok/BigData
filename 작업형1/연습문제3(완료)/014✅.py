# 1. 중복 데이터를 제거하시오
# 2. f3 컬럼의 결측치는 0 "silver"는 1 "gold"는 2 "vip"는 3으로 변환하시오
# 3. 변환된 f3 컬럼의 총합을 정수형으로 구하시오

import pandas as pd

df = pd.read_csv("./type1_data1.csv") # (120, 10)
# print(df.head())

df = df.drop_duplicates() # 중복데이터 제거
# print(df.shape) # (118, 10)

# print(df.isnull().sum())

def encoder(value):
    if value == "silver":
        return 1
    elif value == "gold":
        return 2
    elif value == "vip":
        return 3

df["f3"] = df["f3"].apply(encoder)
df["f3"] = df["f3"].fillna(0)

print(int(df["f3"].sum())) # 167
# print(df.isnull().sum())

# df["f3"] = df["f3"].replace({
#     "silver": 1,
#     "gold": 2,
#     "vip": 3
# }).fillna(0)