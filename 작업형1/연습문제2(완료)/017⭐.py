# 1. views 컬럼의 표준편차를 구하시오
# 2. age 컬럼의 이상치(소수점 나이, 음수 나이, 0살)를 제거하고, views 컬럼의 표준편차를 구하시오
# 3. 이상치 제거 전후의 views 컬럼의 표준편차를 더하여, 반올림 후 소수 둘째자리까지 구하시오
import pandas as pd

df = pd.read_csv("./type1_data1.csv")
# print(df.head())

# print(df["views"].std())

ori_std =df["views"].std()

# outlier = (df["age"] <= 0) | (df["age"] == round(df["age"], 0))
# outlier = (df["age"] <= 0) | (df["age"] != df["age"].astype(int))
outlier = (df["age"] <= 0) | (df["age"]%1 != 0) # ⭐정수판별공식 x % 1 == 0

filtered = df[~outlier]

filtered_std = filtered["views"].std()

print(round(ori_std + filtered_std, 2)) # 8297.31

# print(df[outlier])
# print((df["age"] == round(df["age"], 0)).head(25))
