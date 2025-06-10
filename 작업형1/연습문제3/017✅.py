# 1. views 컬럼의 표준편차를 구하시오
# 2. age 컬럼의 이상치(소수점 나이, 음수 나이, 0살)를 제거하고, views 컬럼의 표준편차를 구하시오
# 3. 이상치 제거 전후의 views 컬럼의 표준편차를 더하여, 반올림 후 소수 둘째자리까지 구하시오
import pandas as pd

df = pd.read_csv("./type1_data1.csv")
# print(df.head())

ori_std = df["views"].std()

# print(df.shape) # (120, 10)

cond1 = df["age"] > 0
cond2 = df["age"] % 1 == 0

filterd = df[cond1 & cond2]

filterd_std = filterd["views"].std()

print(round(ori_std + filterd_std, 2))  # 8297.31

# print(filterd["views"].std())