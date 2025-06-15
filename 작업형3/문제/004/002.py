# 4개의 중학교에서 다른 교육 방법을 사용해 학생들에게 수학을 가르쳤다. 각 중학교의 학생들이 받은 교육 후의 수학 성적은 다음과 같다.
# 이 4개의 교육 방법에 따른 성적 차이가 통계적으로 유의미한지 5%의 유의수준에서 검정하시오.
    # 귀무가설: 모든 중학교의 학생들의 수학 성적 평균은 동일하다.
    # 대립가설: 적어도 2개 중학교의 학생들의 수학 성적 평균은 다르다. (4개의 교육 방법 중 최소한 하나의 방법이 다른 방법들과 성적에서 차이가 있다.)

# 1. 각 그룹의 수학 성적에 대해 Shapiro-Wilk 검정을 통한 정규성을 확인하고, 그 결과의 p-value를 구하시오
# 2. 4개 그룹의 수학 성적이 등분산성을 갖는지 확인하기 위해 Levene 검정을 실시하고, p-value를 구하시오
# 3. 유의수준 0.05하에서 귀무가설을 기준으로 검정의 결과를 채택/기각 중 선택해 입력하시오
# 4. 그룹 변수의 자유도를 구하시오
# 5. 잔차의 자유도를 구하시오
# 6. 성적의 제곱합을 구하시오 
# 7. 성적의 평균 제곱을 구하시오
# 8. F-통계랑의 값을 구하시오
# 9. 성적에 대한 p-value를 구하시오

import pandas as pd

df = pd.read_csv("math.csv") # groups  scores

from scipy.stats import shapiro, levene, f_oneway

# print(df.shape) # (40, 2)

A = df[df["groups"] == "group_A"]
B = df[df["groups"] == "group_B"]
C = df[df["groups"] == "group_C"]
D = df[df["groups"] == "group_D"]

# print(A.shape, B.shape, C.shape, D.shape) # (10, 2) (10, 2) (10, 2) (10, 2)

# print(shapiro(A["scores"]).pvalue)
# print(shapiro(B["scores"]).pvalue)
# print(shapiro(C["scores"]).pvalue)
# print(shapiro(D["scores"]).pvalue)

# print(levene(A["scores"], B["scores"], C["scores"], D["scores"]).pvalue)

stats, pvalue = f_oneway(A["scores"], B["scores"], C["scores"], D["scores"])
# print(stats, pvalue) # 34.17427385892114 1.2406415428510513e-10

# print(pvalue < 0.05)

from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

model = ols("scores ~ groups", data=df).fit()
# print(anova_lm(model))

#             df  sum_sq     mean_sq          F        PR(>F)
# groups     3.0   411.8  137.266667  34.174274  1.240642e-10
# Residual  36.0   144.6    4.016667        NaN           NaN


# 1) 0.9051800443853569, 0.6678172590861611, 0.44732595113862045, 0.25824165549017347
# 2) 0.17270284963232105
# 3) 기각
# 4) 3.0
# 5) 36.0
# 6) 411.8
# 7) 137.266667
# 8) 34.174274
# 9) 1.240642e-10

# ==== 답지 =============================
# 1. 0.9051800443853569, 0.6678172590861611, 0.44732595113862045, 0.25824165549017347
# 2. 0.17270284963232105
# 3. 기각
# 4. 3.0
# 5. 36.0
# 6. 411.8
# 7. 137.266667
# 8. 34.174274
# 9. 1.240642e-10