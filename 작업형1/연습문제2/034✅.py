# 1. school_data.csv와 school_data_science.csv의 학생 순서는 동일하다
# 2. 학생별로 수학, 영어, 국어, 과학 점수의 평균을 구하시오
# 3. 평균 점수가 60점 이상인 인원 수를 계산하시오

import pandas as pd

df = pd.read_csv("school_data.csv")
df_science = pd.read_csv("school_data_science.csv")

# print(df_science.head())
# print(df.shape, df_science.shape) # (30, 7) (30, 3)

full = pd.concat([df, df_science], axis=1)
# print(full["수학"] + full["영어"] + full["국어"] + full["과학"] / 4)
full["평균"] = (full["수학"] + full["영어"] + full["국어"] + full["과학"]) / 4

cond = full["평균"] >= 60

print(len(full[cond])) # 9

# print(full.head())

# print(full.shape) # (30, 10)