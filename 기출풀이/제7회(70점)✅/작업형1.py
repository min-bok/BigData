import pandas as pd

# === 문제1 ======================================
# 결측치가 있는 행을 제거한 후 학생이 가장 많이 수강한 과목을 찾고, 
# 해당 과목 점수를 표준화(스탠더드 스케일)한 다음 가장 큰 표준화된 값을 구하시오 (반올림하여 소수 셋째자리까지 계산)
# df = pd.read_csv("student_assessment.csv")
# # print(df.sample(5))

# df = df.dropna()

# top = df["id_assessment"].value_counts().idxmax() # ⭐

# cond = df["id_assessment"] == top
# df = df[cond]

# from sklearn.preprocessing import StandardScaler
# scaler = StandardScaler()
# df["score"] = scaler.fit_transform(df[["score"]]) # ⭐

# print(round(df["score"].max(), 3)) # 2.183

# === 문제2 ======================================
# DE1 ~ DE77 컬럼 중 주가지수의 종가 "close"와 가장 상관 관계가 높은 변수를 찾아 해당 변수의 평균값을 구하시오 (반올림하여 소수 넷째자리까지 계산)
import pandas as pd

# df = pd.read_csv("stock_market.csv")
# # print(df.sample(5))

# df_corr = abs(df.corr()["close"]) # ⭐
# max = df_corr.loc["DE1":"DE77"].idxmax()
# print(round(df[max].mean(),4)) # -0.0004

# === 문제3 ======================================
# IQR을 이용해 이산화탄소(CO2) 이상치 수를 찾으시오
    # Q1: 하위 25%값
    # Q3: 상위 25%값
    # IQR = Q3 - Q1
    # lower : Q1 - 1.5 * IQR 이 값보다 작은 데이터는 이상치로 간주
    # upper : Q3 + 1.5 * IQR 이 값보다 큰 데이터는 이상치로 간주
import pandas as pd

# CO2
df = pd.read_csv("air_quality.csv")
# print(df.sample(5))

q1 = df["CO2"].quantile(.25)
q3 = df["CO2"].quantile(.75)
iqr = q3 - q1

lower = df["CO2"] < q1 - 1.5 * iqr
upper = df["CO2"] > q3 + 1.5 * iqr

# print(len(df[lower]) + len(df[upper])) # 304 ✅

