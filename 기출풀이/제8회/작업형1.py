# === 문제1 ======================
# 1. 대륙(continent)별 맥주 소비량(beer_servings)의 평균을 계산하고, 평균이 가장 큰 대륙을 찾으시오
# 2. 1번에서 찾은 대륙에서 맥주 소비량이 5번째로 많이 국가(country)의 맥주 소비량을 구하시오

# import pandas as pd

# df = pd.read_csv("drinks.csv")
# # print(df.shape) # (193, 6)

# topContinent = "Europe"
# # print(df.groupby("continent")["beer_servings"].mean().reset_index()) # Europe

# cond = df["continent"] == topContinent
# # print(df[cond].sort_values("beer_servings", ascending=False).iloc[4:5]) 

# 답) 313 ✅

# === 문제2 ======================
# 1. "관광객비율"이 두번째로 높은 국가의 "사업" 방문객 수를 a라고 정의하시오
# 2. "관광"이 두번째로 높은 국가의 "공무" 방문객 수를 b라고 정의하시오
# 3. a와 b의 합을 구하시오
    # 방문객 합계 = 관광 + 공무 + 사업 + 기타
    # 관광객 비율 = 관광 / 방문객 합계
# import pandas as pd

# # 나라    관광   공무   사업   기타
# df = pd.read_csv("tourist.csv")

# df["방문객합계"] = df["관광"] + df["공무"] + df["사업"] + df["기타"]
# df["관광객비율"] = df["관광"] / df["방문객합계"]
# # print(df.shape) # (100, 5)
# # print(df.head())

# a = 203
# b = 238

# print(df.sort_values("관광객비율", ascending=False))
# print(df.sort_values("관광", ascending=False))

# print(a+b)

# 답) 441 ✅

# === 문제3 ======================
# 1. 주어진 데이터에서 "co"와 "nmhc"컬럼을 각각 Min-MAX 스케일링 하시오
# 2. 스케일링된 "co", "nmhc" 컬럼의 표준편차를 각각 구하시오
# 3. "co"컬럼의 표준편차에서 "nmhc"컬럼의 표준편차를 뺀 값을 소수점 3자리로 반올림하여 구하시오
    # 민맥스 스케일링 = (X - min_X) / (max_X - min_X)
    # X변수의 최솟값: min_X
    # X변수의 최댓값: max_X

import pandas as pd

# sample   co  nmhc  etc
df = pd.read_csv("chem.csv")
# print(df.head())
# print(df.shape) # (100, 4)
# print(df.info())

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
df[["co", "nmhc"]] = scaler.fit_transform(df[["co", "nmhc"]]) # ⭐

result = df["co"].std() - df["nmhc"].std()
print(df["co"].std(), df["nmhc"].std())
# print(round(result ,3)) 

# 답) 
# 0.2856516497116944 0.3030617020578397 ✅
# -0.017 ✅