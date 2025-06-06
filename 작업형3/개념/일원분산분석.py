# 3개 이상의 집단 간의 평균 차이가 통계적으로 유의한지 검정
# 집단을 나누는 요인이 하나고 집단의 수가 3개 이상일때 사용
# 독립성, 정규성, 등분산성을 기본 가정으로 함
# scipy의 f_oneway(1집단, 2집단, 3집단)

# 문제 =================
# 주어진 데이터는 4종류의 비료를 사용한 식물의 성장에 대한 실험 결과 이다. 이 실험에서는 비슷한 조건의 식물 40개를 무작위로 10개씩 나누고
# 화학 비료 A,B,C,D 를 일정 기간 사용한 후 성장량을 측정했다, 성장의 차이가 있는지 유의수준 0.05하에서 검정하시오
    # 귀무가설: 네 가지 비료의 효과는 동일하다
    # 대립가설: 비료의 효과에는 차이가 있다 (적어도 두 가지 비료의 효과에는 차이가 있다)

# import pandas as pd
# df = pd.DataFrame({
#     'A': [10.5, 11.3, 10.8, 9.6, 11.1, 10.2, 10.9, 11.4, 10.5, 10.3],
#     'B': [11.9, 12.4, 12.1, 13.2, 12.5, 11.8, 12.2, 12.9, 12.4, 12.3],
#     'C': [11.2, 11.7, 11.6, 10.9, 11.3, 11.1, 10.8, 11.5, 11.4, 11.0],
#     'D': [9.8, 9.4, 9.1, 9.5, 9.6, 9.9, 9.2, 9.7, 9.3, 9.4]
# })
# print(df.head(2))

# from scipy.stats import shapiro, levene, f_oneway
# print(dir(scipy.stats))

# 1. 정규성 검정 -------
# 모두 0.05보다 크므로 정규 분포를 따름
# print(shapiro(df["A"])) # 0.8400161543468654
# print(shapiro(df["B"])) # 0.6308700692815115
# print(shapiro(df["C"])) # 0.892367306190296
# print(shapiro(df["D"])) # 0.9346854448707653

# 2. 등분산성 검정
# 0.05보다 크므로 모든 그룹의 분산이 동일
# print(levene(df["A"], df["B"], df["C"], df["D"])) # 0.14127835331346628
# print(0.14127835331346628 > 0.05) # True

# 3. 일원 분산 분석 ----------------------
# stat, pvalue = f_oneway(df["A"], df["B"], df["C"], df["D"])
# print(pvalue, pvalue < 0.05) # 귀무가설을 기각

# 일원 분산 분석(ols) 활용 ===========================
import pandas as pd

df = pd.read_csv("fertilizer.csv")
# print(df.head())

from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

model = ols("성장 ~ C(비료)", df).fit()
print(anova_lm(model))