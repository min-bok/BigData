# 로지스틱 회귀는 범주형 종속변수를 대상으로 하는 통계적 분석 방법 (분류 모델)
# statsmodels의 logit() 함수 사용

# === 문제 ==========================
# 다음은 특정 질병의 유무를 나타내는 환자 데이터셋이다. 이 데이터를 바탕으로 각 소문제의 값을 구하시오
# 데이터
    # 독립변수: 나이(age), 체질량 지수(bmi), 흡연(smoker)여부, 활동 수준(activity_level)
    # 종속변수: 특정 질병(disease)의 유무

import pandas as pd

df = pd.read_csv("health_survey.csv")
# print(df.head())

# 1. 로지스틱 회귀 모델의 사용하여 age와 bmi를 독립변수로 활용해 질병의 발생 여부를 예측한다. 주어진 데이터셋을 바탕으로 bmi 변수의 계수 값은?
from statsmodels.formula.api import logit

model = logit("disease ~ age + bmi", data=df).fit()
# print(model.summary())

# 2. 1번 문제에서 추정된 로지스틱 회귀 모델에서 bmi 변수가 한 단위 증가할 때 질병 발생의 오즈비 값은?
import numpy as np
# print(np.exp(model.params["bmi"]))

# 3. 로그 우도(Log-Likehood)를 구하는 방법과 잔차이탈도를 계산하는 방법
llf = model.llf # 로그 우도
# print(llf)

print(-2 * llf) # 잔차이탈도

# 4. 정확도와 오류율
