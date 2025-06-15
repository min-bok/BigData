# 1. views 컬럼의 표준편차를 구하시오
# 2. age 컬럼의 이상치(소수점 나이, 음수 나이, 0살)를 제거하고, views 컬럼의 표준편차를 구하시오
# 3. 이상치 제거 전후의 views 컬럼의 표준편차를 더하여, 반올림 후 소수 둘째자리까지 구하시오
import pandas as pd

df = pd.read_csv("./type1_data1.csv")
# print(df.head())

# print(df["views"].std())
std1 = df["views"].std()
# print((df["age"] % 1 != 0).sum()) # 정수 판별공식


cond1= df["age"] > 0
cond2 = df["age"] == round(df["age"], 0)

# print((df["age"] > 0).sum())
df = df[cond1 & cond2]
# print((df["age"] > 0).sum())

std2 = df["views"].std()

# print(std1, std2)
# print(round(std1 + std2, 2))


# print((df["age"] == 0).sum())
# print(df.head(50))