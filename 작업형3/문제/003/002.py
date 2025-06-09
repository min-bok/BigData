# 대응 표본 검정

# 연구소에서는 새로 개발한 교육과정에 참여하면 학습 시간이 단축된다고 주장한다.
# 10명의 학생들을 대상으로 기존의 교육 방법과 새로운 교육 방법을 적용한 결과에 대해
# 유의수준 5%에서 새로운 교육 방법이 교육 시간을 단축시켰는지 검정하시오 (단 모집단은 정규분포를 가정한다.)
    # 뮤 = (새로운 교수방법 - 기존 교수 방법)의 평균
    # 귀무가설: 뮤 = 0
    # 대립가설: 뮤 < 0 : μ < 0이면 (새로운 - 기존), μ > 0이면 (기존 - 새로운)

# 1. 뮤의 표본 평균을 구하시오
# 2. 위의 가설을 검정하기 위한 검정 통계량을 구하시오
# 3. 위의 통계량에 대한 P-value를 구하시오
# 4. 유의수준 0.05하에서 귀무가설을 기준으로 검정의 결과를 채택/기각 중 선택해 입력하시오

import pandas as pd

df = pd.DataFrame({
    'User': list(range(1, 11)),
    '기존방법': [60.4, 60.7, 60.5, 60.3, 60.8, 60.6, 60.2, 60.5, 60.7, 60.4],
    '새로운방법': [59.8, 60.2, 60.1, 59.9, 59.7, 58.4, 57.0, 60.3, 59.6, 59.8]
})

# print(df["기존방법"].mean())
# print(df["새로운방법"].mean())

mean = (df["새로운방법"] - df["기존방법"]).mean()
# print(mean) # 1.0300000000000005

# 1. 정규성 검증(샤피로) - 문제에서는 생략 가능하지만 연습함
from scipy.stats import shapiro

nomalize = shapiro(df["새로운방법"] - df["기존방법"])
# print(nomalize.pvalue < 0.05) # True, 정규성을 만족하지않음

# shapiro, ttest_rel, wilcoxon

# print(dir(scipy.stats))

# 2. t-test 검증
from scipy.stats import ttest_rel

statistic, pvalue = ttest_rel(df["새로운방법"], df["기존방법"], alternative="less")
# print(statistic, pvalue) # 3.407973078114844 0.0038872633380070652

print(mean)
print(statistic)
print(pvalue)
print(pvalue < 0.05) # True, 기각

# 1. -1.0300000000000005
# 2. -3.407973078114844
# 3. 0.0038872633380070652
# 4. 기각