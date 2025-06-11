# 다중 선형 회귀 분석은 2개 이상의 독립변수와 하나의 종속변수 간의 관계를 분석하는 방법

# === 문제 ==========================
# 다음은 매출액, 광고비, 직원 수에 관한 데이터다. 광고비와 직원 수는 독립변수고, 매출액은 종속변수다.
# 다중 선형 회귀 모델을 구축하고 각 소문제의 값을 구하시오

import pandas as pd
data = {
    '매출액': [300, 320, 250, 360, 315, 328, 310, 335, 326, 280,
            290, 300, 315, 328, 310, 335, 300, 400, 500, 600],
    '광고비': [70, 75, 30, 80, 72, 77, 70, 82, 70, 80,
            68, 90, 72, 77, 70, 82, 40, 20, 75, 80],
    '직원수': [15, 16, 14, 20, 19, 17, 16, 19, 15, 20,
            14, 5, 16, 17, 16, 14, 30, 40, 10, 50]
    }
df = pd.DataFrame(data)
# print(df.head())

# 1. 주어진 데이터로 최소제곱법을 이용한 다중 선형 회귀 모델을 구축하고 통계적 요약을 출력하시오
from statsmodels.formula.api import ols
model = ols("매출액 ~ 광고비 + 직원수", data=df).fit()
# print(model.summary())

# 2. 광고비와 매출액의 상관 계수를 구하시오
# print(df["광고비"].corr(df["매출액"]))

# 3. 광고비와 매출액의 t-검정의 p-value를 구하시오
from scipy.stats import pearsonr
# print(pearsonr(df["광고비"], df["매출액"]))
# print(dir(scipy.stats))

# 4. 회귀 모델의 결정 계수를 구하시오
# print(model.rsquared)

# 5. 회귀 모델에서 회귀 계수(기울기와 절편)를 구하시오
# print(model.params)

# 6. 회귀 모델에서의 광고비의 회귀 계수가 통계적으로 유의한지 검정했을 때의 p-value를 구하시오
# print(model.pvalues)
# print(model.pvalues["광고비"])

# 7. 광고비 50, 직원 수 20인 데이터가 있을 때, 구축한 회귀 모델에서의 예상 매출액을 구하시오
new_data = pd.DataFrame({"광고비": [50], "직원수": [20]})
# print(model.predict(new_data))

# 8. 회귀 모델의 잔차의 제곱합을 구하시오
# df["잔차"] = df["매출액"] - model.predict(df)
# print(sum(df["잔차"] ** 2))

# 9. 회귀 모델의 MSE를 구하시오
df["잔차"] = df["매출액"] - model.predict(df)
# print((df["잔차"] ** 2).mean())

# 10. 각 변수별 95%의 신뢰 구간을 구하시오
# print(model.conf_int(alpha=0.05))

# 11. 광고비 45, 직원 수 22일때 95% 신뢰 구간과 예측 구간을 구하시오
new = pd.DataFrame({"광고비": [45], "직원수": [22]})
pred = model.get_prediction(new)
result = pred.summary_frame(alpha=0.05)
# print(result)