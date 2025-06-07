# 독립성 검정은 2개의 범주형 변수가 서로 독립적인지, 연관이 있는지 검정하는데 사용됨
# scipy.stats.chi2_contingency

# ==== 문제 ============================
# 성별에 따라 운동을 좋아하는지 조사한 결과다. 성별과 운동 선호도가 독립적인지 가설검정을 실시하시오 (유의수준 0.05)
    # 귀무가설: 성별과 운동 선호도는 독립적이다
    # 대립가설: 성별과 운도오 선호도는 독립적이지 않다

# --- 풀이1 : 교차표 데이터가 주어졌을때 ---------------
# 남자: 좋아함 80명, 좋아하지 않음 30명
# 여자: 좋아함 90명, 좋아하지 않음 10명

# 데이터프레임 만들기: 컬럼(열) 방향
# import pandas as pd

# df = pd.DataFrame(
#     {
#         "좋아함": [80, 90], 
#         "좋아하지 않음": [30, 10]
#     },
#     index=["남자", "여자"]
# )
# print(df.head())

# from scipy.stats import chi2_contingency
# print(chi2_contingency(df)) # expected_freq: 기대 빈도수(관찰된 데이터가 독립적일 경우 예상되는 빈도수)
# print(dir(scipy.stats))

# --- 풀이2 : 로우 데이터가 주어졌을때 ---------------
import pandas as pd
data = {
    '성별': ['남자']*110 + ['여자']*100,
    '운동': ['좋아함']*80 + ['좋아하지 않음']*30 + ['좋아함']*90 + ['좋아하지 않음']*10
}
df = pd.DataFrame(data)
# print(df.head(3))

df = pd.crosstab(df["성별"], df["운동"]) # 교차표로 변경
# print(df)

from scipy.stats import chi2_contingency
print(chi2_contingency(df))
# print(dir(scipy.stats))

