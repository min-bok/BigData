# 제공된 데이터는 타이타닉호의 침몰 사건에서 생존한 승객 및 사망한 승객의 정보를 포함한 자료이다.
# 아래 데이터를 이용하여 생존여부(Survived)를 예측하고자 한다.
# 각 문항의 답을 [제출 형식]에 맞춰 답안 작성 페이지에 입력하시오(단, 벌점화(penalty))는 부여하지 않는다.

# 1. Gender와 Survived 변수 간의 독립성 검정을 실시하였을 때, 카이제곱 통계량은? (반올림하여 소수 셋째 자리까지 계산)
# 2. Gender, SibSp, Parch, Fare를 독립변수로 사용하여 로지스틱 회귀모형을 실시하였 때, Parch 변수의 계수값은? (반올림하여 소수 셋째자리까지 계산)
# 3. 위 2번 문제에서 추정된 로지스틱 회귀모형에서 SibSp 변수가 한 단위 증가할 때 생존할 오즈비(Odds ratio)값은? (반올림하여 소수 셋째자리까지 계산)

import pandas as pd

df = pd.read_csv("data/Titacic.csv")

# 1번
from scipy.stats import chi2_contingency, ttest_1samp, ttest_ind, ttest_rel, chisquare
table = pd.crosstab(df["Gender"], df["Survived"])
# print(chi2_contingency(table))
statistics, p, df, expected = chi2_contingency(table)
# print(round(statistics, 3)) # 260.717

# 2번
from statsmodels.api import Logit
# Logit : 로지스틱 회귀
# OLS : 선형 회귀

# Survived : 종속변수(예측할변수?)
formula = "Survived ~ Gender + SibSp + Parch + Fare"
results = Logit.from_formula(formula, df).fit()
# print(results.summary()) # summary보는법 알아야겠다
# print(round(results.params["Parch"], 3)) # Parch의 계수구하는 함수(반올림)

# 3번
import numpy as np
print(round(np.exp(-0.3539), 3))
# print(round(np.exp(results.params["ParcSibSph"]), 3))

# 해당 화면에서는 제출하지 않으며, 문제 풀이 후 답안제출에서 결괏값 제출
