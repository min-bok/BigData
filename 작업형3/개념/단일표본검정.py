# 어떤 집단의 평균이 특정 값과 유의미하게 다른지를 검정하는 통계 방법
# 영화관에서 판매하는 팝콘 라지 사이즈의 무게는 일반적으로 120g으로 알려져 있다.
# 이제 이 데이터를 갖고 t-test를 수행한다. 가설검정 프로세스 순서로 풀어본다.

# ttest_1samp(표본데이터, 평균 또는 기대값, alternative)
# alternative: 기본적으로 양측검정(120g보다 크거나 작음에 대해 검증),  단층검증(크다 or 작다)
    # 양측검정: alternative="two-sided"
    # 단측검정: 보다 크다, alternative="greater"
    # 단측검정: 보다 작다, alternative="less"

import pandas as pd

df = pd.DataFrame({
'weights':[122, 121, 120, 119, 125, 115, 121, 118, 117, 127,
123, 129, 119, 124, 114, 126, 122, 124, 121, 116,
120, 123, 127, 118, 122, 117, 124, 125, 123, 121],
})

# 1. 통계설 가설 설정
    # 귀무가설: 팝콘 라지 사이즈의 평균 무게는 120g이다.
    # 대립가설: 팝콘 라지 사이즈의 평균 무게는 120g이 아니다.
# 2. 유의 수준 결정
    # 0.05
# 3. 검정 통계량과 유의확률(p-value) 계산 → ttest_1samp 함수 사용
from scipy.stats import ttest_1samp
statistic, pvalue = ttest_1samp(df["weights"], 120)

# print(ttest_1samp(df["weights"], 120))
# print(statistic, pvalue)
print(pvalue < 0.05) # True, 귀무가설 기각

# print(help(scipy))
# print(dir(scipy.stats))
# 4. 결과 도출: 
    # p-value가 유의수준 0.05보다 작다면 귀무가설을 기각하고, 대립가설을 채택한다.
    # p-value가 유의수준 0.05보다 크다면 귀무가설을 채택하고, 대립가설을 기각한다.

# ----------------------------------

# 표본 데이터가 정규 분포를 따를 때는 모수 검정인 t-검정을 사용
# 데이터가 정규성 가정을 만족하지 않을때는 비모수 검정방식을 고려해야함
    # 데이터의 정규성을 판별하는 '샤피로-윌크 검정' 결과 정규성을 만족하지않으면,
    # 윌콕슨의 부호 순위 검정을 통해 가설검정을 수행
import pandas as pd

df = pd.DataFrame({
    'weights':[125, 126, 118, 124, 117, 127, 123, 122, 119, 142]
})

# 샤피로-윌크 검정 (정규성 판별)
from scipy.stats import shapiro, wilcoxon

shapiro(df["weights"])
statistic, pvalue = shapiro(df["weights"])
# print(pvalue < 0.05) # True: 작으므로 정규분포를 따르지않음

# 윌콕슨의 부호 순위 검정 (비모수 가설검정)
    # 귀무가설: 아메리카노 한잔의 원두의 중앙값이 120g이다 (중앙값 = 120g)
    # 대립가설: 아메리카노 한잔의 원두의 중앙값이 120g이 아니다 (중앙값 =/ 120g)

wilcoxonResult = wilcoxon(df["weights"] - 120, alternative="less")
print(wilcoxonResult.pvalue) # 0.9814453125, 귀무가설 채택

# print(dir(scipy.stats))