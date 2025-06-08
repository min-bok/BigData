# 동질성 검정은 2개 이상의 집단에서 분산의 동질성을 가졌는지 검정하는데 사용
# scipy.stats.chi2_contigency(table, correction=True)
    # table: 교차표
    # correction: 연속성 보정 여부(기본값 True), 연속성 수정을 하지 않는다 라는 조건이 있을시 False

# === 문제 =================================
# 학과에 따라 학교 공식 동아리에 가입한 학생의 수와 가입하지 않은 학생의 수를 비교하는 동질성 검사를 실시하고,
# 유의수준에 따른 검정 결과를 작성하시오. (유의수준 0.05)
    # 귀무가설: 두 학과의 동아리 가입 비율은 동일하다
    # 대립가설: 두 학과의 동아리 가입 비율은 동일하지 않다

# --- 1. 교차표 데이터가 주어졌을때 -----------------------------
# import pandas as pd

# df = pd.DataFrame({
#     "가입": [50, 30],
#     "미가입": [50, 70]
# }, index=["통계학과", "컴퓨터공학과"])

# # print(df)

# from scipy.stats import chi2_contingency
# print(chi2_contingency(df))

# --- 2. 로우 데이터가 주어졌을때 -----------------------------
import pandas as pd
data = {
    '학과': ['통계학과']*100 + ['컴퓨터공학과']*100,
    '동아리가입여부': ['가입']*50 + ['미가입']*50 + ['가입']*30 + ['미가입']*70
}
df = pd.DataFrame(data)
# print(df.sample(5))

df = pd.crosstab(df["학과"], df["동아리가입여부"])

from scipy.stats import chi2_contingency
print(chi2_contingency(df))
# print(df.head())