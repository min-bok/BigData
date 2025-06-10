# 회귀분석은 수치형 변수의 관계 또는 원인과 결과간의 관계를 추정하거나 예측하는데 사용함

# === 01. 상관계수 (corr) ========================================
# 두 변수 간의 선형적인 관계가 어느정도 강한지 나타냄 (-1 <= r <= 1)

# 다음은 학생들의 키와 몸무게 데이터다. 이를 바탕으로 상관 계수를 구하라

# import pandas as pd

# data = {
#     '키': [150, 160, 170, 175, 165],
#     '몸무게': [42, 50, 70, 64, 56]
# }
# df = pd.DataFrame(data)

# # print(df.head())
# corr = df.corr() # 피어슨 상관 계수(기본값)
# # df.corr(method="spearman") # 스피어만 상관 계수
# print(corr.iloc[0,1]) # 0.9195090879163764

# # 상관계수와 t-검정 ----------------------------------------
# # 일반적으로 t-검정을 묻는다면 피어슨 상관 계수값이 표준
# from scipy.stats import pearsonr, spearmanr

# print(pearsonr(df["몸무게"], df["키"]))
# print(spearmanr(df["몸무게"], df["키"]))

# print(dir(scipy.stats))

