# === 문제1 ===================================
import pandas as pd

# # 소방서 출동시간 도착시간
df = pd.read_csv("data6-1-1.csv")

df["출동시간"] = pd.to_datetime(df["출동시간"])
df["도착시간"] = pd.to_datetime(df["도착시간"])

df["차이"] = df["도착시간"] - df["출동시간"]

late = df.groupby(["소방서"])["차이"].mean().reset_index().max()["차이"]

print(round(late.total_seconds() / 60))

# 80.65888888333333
# 81 # ⭐ "분"은 관행상 반올림해야함

# === 문제2 ===================================
# import pandas as pd

# # 학교명  교사수  1학년  2학년  3학년  4학년  5학년  6학년
# df = pd.read_csv("data6-1-2.csv")

# df["전체"] = df["1학년"] + df["2학년"] + df["3학년"] + df["4학년"] + df["5학년"] + df["6학년"]
# df["교사1인당"] = df["전체"]/df['교사수']

# target = df.sort_values("교사1인당", ascending=False).iloc[:1]

# print(target["교사수"])

# 19 ✅

# === 문제3 ===================================
# import pandas as pd

# # 날짜  강력범죄  절도범죄  폭력범죄  지능범죄  풍속범죄  교통범죄  경찰서명
# df = pd.read_csv("data6-1-3.csv")

# df["총범죄건수"] = df["강력범죄"] + df["절도범죄"] + df["폭력범죄"] + df["지능범죄"] + df["풍속범죄"] + df["교통범죄"]

# df["날짜"] = df["날짜"].str.slice(0, 5)
# # print(df.head(25))
# # print(df["날짜"].str.slice(0, 5))

# result = df.groupby(["날짜"])["총범죄건수"].mean().reset_index().max()["총범죄건수"]

# print(int(round(result, 0)))

# 533 ✅
