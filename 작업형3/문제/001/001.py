# 단일 표본 검정
# 한 커피 제조회사에서는 새로 출시한 커피의 카페인 함량이 평균 95mg 미만이라고 주장했다.
# 그 주장이 사실인가를 알아보기 위해 25개의 커피 샘플을 무작위(랜덤)로 추출했다. 커피 제조회사의 주장이 타당한지를 유의수준 5%에서 검정하시오
    # 귀무가설: 뮤 >= 95mg
    # 대립가설: 뮤 < 95mg

# 1. 표본 데이터의 평균을 구하시오
# 2. Shapiro-Wilk 검정의 p-value를 구하시오
# 3. 단일 표본 t-검정의 검정 통계량을 구하시오
# 4. 단일 표본 t-검정의 p-value를 구하시오
# 5. 유의수준 0.05이하에서 귀무가설을 기준으로 검정 결과를 채택/기각 중 선택해 입력하시오

import pandas as pd
df = pd.DataFrame({
    'Caffeine(mg)': [
        94.2, 93.7, 95.5, 93.9, 94.0, 95.2, 94.7, 93.5, 92.8, 94.4,
        93.8, 94.6, 93.3, 95.1, 94.3, 94.9, 93.9, 94.8, 95.0, 94.2,
        93.7, 94.4, 95.1, 94.0, 93.6
    ]
})

# print(df["Caffeine(mg)"].mean()) # 1. 94.264
from scipy.stats import shapiro, ttest_1samp, wilcoxon
shapiroResult = shapiro(df["Caffeine(mg)"])
# print(shapiroResult.pvalue) # 2. 0.9322031137746971

ttest_statistic, ttest_pvalue = ttest_1samp(df["Caffeine(mg)"], 95, alternative="less")
# print(ttest_statistic, ttest_pvalue)

# print(ttest_pvalue < 0.05) # True

# 비모수 검정 연습 -------------------
# print(df["Caffeine(mg)"].median())
print(wilcoxon(df["Caffeine(mg)"] - df["Caffeine(mg)"].median(), alternative="less")) # ⭐

# print(dir(scipy.stats))

# shapiro
# ttest_1samp

# --- 답 -----------
# 94.264
# 0.9322031137746971
# -5.501737036221897
# 5.8686553916715e-06
# 기각