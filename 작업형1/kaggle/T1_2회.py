import pandas as pd

df = pd.read_csv('./작업형1/kaggle/input/basic1.csv')
# print(df)
# print(df.head(3))

# 문제1 ----------------------
#  - 데이터셋(basic1.csv)의 'f5' 컬럼을 기준으로 상위 10개의 데이터를 구하고,
#  - 'f5'컬럼 10개 중 최소값으로 데이터를 대체한 후,
#  - 'age'컬럼에서 80 이상인 데이터의'f5 컬럼 평균값 구하기

# df = df.sort_values("f5", ascending=False)
# df.head(10)

# min = df["f5"][:10].min()
# df["f5"][:10] = min

# print(min) # 91.29779092

# cond = df["age"] >= 80
# print(df[cond]["f5"].mean()) # 62.49774712521738

# 문제 1번: GPT 추천 풀이법
# df = df.sort_values("f5", ascending=False) # 상위 10개 인덱스

# top10_idx = df.head(10).index # 최소값

# min_val = df.loc[top10_idx, "f5"].min() # 해당 인덱스의 f5 값 수정

# df.loc[top10_idx, "f5"] = min_val

# 문제2 ----------------------
  # - 데이터셋(basic1.csv)의 앞에서 순서대로 70% 데이터만 활용해서,
  # - 'f1'컬럼 결측치를 중앙값으로 채우기 전후의 표준편차를 구하고
  # - 두 표준편차 차이 계산하기

# n = int(len(df) * 0.7) # 앞에서 70%

# df_70 = df.iloc[:n].copy()

# # print(df_70["f1"].isnull().sum()) # 23

# std1 = df_70["f1"].std()

# mid = df_70["f1"].median() # 68.0

# df_70["f1"] = df_70["f1"].fillna(mid)

# # print(df_70["f1"].isnull().sum()) # 0

# std2 = df_70["f1"].std()

# print(abs(std1-std2))

# 문제3
  # - 데이터셋(basic1.csv)의 'age'컬럼의 이상치를 더하시오!
  # - 단, 평균으로부터 '표준편차*1.5'를 벗어나는 영역을 이상치라고 판단함

# print(df["age"].head(8))
mean = df["age"].mean()
std = df["age"].std() * 1.5 # 45.664137783883035

min_outlier = mean - std
max_outlier = mean + std
# print(min_outlier, max_outlier)

cond = (df["age"] < min_outlier) | (df["age"] > max_outlier)
print(df[cond]["age"].sum()) # 473.5