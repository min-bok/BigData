# === 문제1 =============================
# import pandas as pd

# df = pd.read_csv("data5-1.csv")
# # print(df.shape) # (762, 26)

# cond1 = df["종량제봉투종류"] == "규격봉투"
# cond2 = df["종량제봉투용도"] == "음식물쓰레기"
# cond3 = df["2ℓ가격"] != 0

# df = df[cond1 & cond2 & cond3]

# result = df["2ℓ가격"].mean()

# print(int(round(result, 0)))

# 118✅

# === 문제2 =============================
# import pandas as pd 

# # Gender  Height  Weight
# df = pd.read_csv("data5-2.csv")

# df["Height"] = df["Height"] / 100
# df["bmi"] = df["Weight"] / (df["Height"] ** 2)
# # print(df.shape) # (10000, 4)

# def foo(bmi):
#     if 18.5 <= bmi < 23:
#         return "정상"
#     elif 23 <= bmi < 25:
#         return "위험"
#     else:
#         return 0

# df["평가"] = df["bmi"].apply(foo)
# # print(df.sample(10))

# 정상 = len(df[df["평가"] == "정상"])
# 위험 = len(df[df["평가"] == "위험"])

# print(int(abs(정상-위험)))

# 144✅

# === 문제3 =============================
# import pandas as pd

# df = pd.read_csv("data5-3.csv")
# # print(df.columns)

# df["순전입학생"] = df["전입학생수(계)"] - df["전출학생수(계)"]

# print(df.sort_values("순전입학생", ascending=False).iloc[:1]["전체학생수(계)"])

# 230✅