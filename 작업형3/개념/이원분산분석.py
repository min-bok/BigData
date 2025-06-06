# 요인의 수가 2개인 경우 ex) 학습 방법과 학습 장소에 따른 성적 분석
# 기본 가정: 독립성, 정규성, 등분산성을 만족

# 문제 ----------------------------------------
# 데이터는 네 가지 종류의 나무(A,B,C,D)에 대해 세 가지 종류의 비료(1,2,3)를 사용해 성장률을 조사한 결과다.
# 비료 간 및 종류간의 성장률 차이가 있는지 유의수준 0.05하에서 검정하시오(단, 독립성, 정규성, 등분산성에 만족한 데이터)

# 종속변수: 성장률 → 연속형 변수⭐
# 주 효과: 나무 종류, 비료 → 범주형 변수
# 상호작용 효괴: 나무와 비료의 상호작용

import pandas as pd
df = pd.read_csv("tree.csv")
# print(df.sample(10))
# print(df.head(10))

from statsmodels.stats.anova import anova_lm
from statsmodels.formula.api import ols

model = ols("성장률 ~ C(나무) + C(비료) + C(나무):C(비료)", data=df).fit() # ⭐독립변수는 무조건 C()쓴다고 기억하자
anova_table = anova_lm(model, typ=1)
# print(anova_table)

# print(format(6.600012e-10, ".11f")) # 0.00000000066