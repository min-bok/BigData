# 두 개의 독립된 그룹의 평균을 비교할때 ⭐
# 두 그룹 사이에 통계적으로 유의미한 차이가 있는지 없는지 결론을 내리는 것
# 정규성 검사 후, 데이터가 정규 분포를 따르지 않으면 비모수 검정(mannwhitneyu)을, 그렇지 않으면 t-검정을 사용

# import pandas as pd

# class1 = [85, 90, 92, 88, 86, 89, 83, 87]
# class2 = [80, 82, 88, 85, 84]

# from scipy.stats import ttest_ind

# 1. 양측 검정
    # 귀무가설: 반별 수학 평균 점수는 같다
    # 대립가설: 반별 수학 평균 점수는 다르다
# statistic, pvalue = ttest_ind(class1, class2)
# print(statistic, pvalue)

# 2. 단측 검정 (모분산은 동일하다)
    # 귀무가설: 반별 수학 평균 점수는 같다
    # 대립가설: 2반 수학 평균 점수가 더 높다(u1 < u2)
# statistic, pvalue = ttest_ind(class1, class2, alternative="less")
# print(statistic, pvalue)

# 3. 단측 검정 (모분산은 동일하다)
    # 귀무가설: 반별 수학 평균 점수는 같다
    # 대립가설: 1반 수학 평균 점수가 더 높다 (u1 > u2)
# statistic, pvalue = ttest_ind(class1, class2, alternative="greater")
# print(statistic, pvalue)

# --------------------------
# 다음은 어느 학교의 반별 수학 시험 점수다. 1반과 2반의 평균 점수가 차이가 있는지 유의 수준 0.05하에서 가설감정하시오 (u1: 1반평균, u2: 2반평균)
    # 귀무가설: 반별 수학 평균 점수는 같다 (u1 = u2)
    # 대립가설: 2반 수학 평균 점수가 더 높다 (u1 < u2)

# from scipy.stats import shapiro, levene, ttest_ind

# 1. 모수 검정 =================================================================================

# 정규성 검정
# print(shapiro(class1)) # pvalue=np.float64(0.999986994137081) → > 0.05 정규성 만족
# print(shapiro(class2)) # pvalue=np.float64(0.9854182266624983) → > 0.05 정규성 만족

# 등분산성 검정 (레빈)
# print(levene(class1, class2)) # pvalue=np.float64(0.958802951766629) → > 0.05 등분산성 만족

# print(ttest_ind(class1, class2, alternative="less")) # pvalue=np.float64(0.9754257110537391) → 귀무가설 채택

# print(help(scipy))
# print(dir(scipy.stats))

# 2. 비모수 검정 =================================================================================
import pandas as pd

class1 = [85, 90, 92, 88, 86, 89, 83, 87]
class2 = [80, 82, 88, 85, 130]

from scipy.stats import shapiro, mannwhitneyu
# print(shapiro(class1)) # pvalue=np.float64(0.999986994137081)) → 정규성 만족
# print(shapiro(class2)) # pvalue=np.float64(0.007151570728885509)) → 정규성 가정 위배

# print(mannwhitneyu(class1, class2, alternative="less")) # pvalue=np.float64(0.8299904236851448) → 귀무가설 채택



# print(dir(scipy.stats))