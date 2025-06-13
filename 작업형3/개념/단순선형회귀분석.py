# 단순 선형 회귀 분석이란 하나의 독립변수로부터 하나의 종속변수와의 관계를 분석하거나 예측하는 방법

# === 문제 =========================================
# 다음은 20명의 키와 몸무게에 관한 정보다. 이 데이터를 바탕으로 회귀 모델을 구축하고 각 소문제의 값을 구하시오
import pandas as pd

# 주어진 데이터
data = {
    '키': [150, 160, 170, 175, 165],
    '몸무게': [42, 50, 70, 64, 56]
}
df = pd.DataFrame(data)
# print(df.head())

from statsmodels.formula.api import ols
model = ols("키 ~ 몸무게", data=df).fit()

# 1. 주어진 데이터로 최소제곱법을 이용한 단순 선형 회귀 모델을 구축하고 통계적 요약을 출력하시오
# print(model.summary())

# 2. 회귀 모델의 결정 계수를 구하시오
# print(model.rsquared)

# 3. 회귀 모델에서 회귀 계수(기울기와 절편)를 구하시오
# print(model.params["몸무게"])
# print(model.params["Intercept"])

# 4. 회귀 모델에서 몸무게의 회귀 계수가 통계적으로 유의한지 검정했을 때의 p-value를 구하시오
# print("{:.10f}".format(model.pvalues["몸무게"]))

# 5. 회귀 모델을 사용해 몸무게가 67일 때의 예측 키를 구하시오
new_data = pd.DataFrame({"몸무게":[67]})
result = model.predict(new_data)
# print(result[0])

# 6. 회귀 모델의 잔차 제곱합을 구하시오
df["잔차"] = df["키"] - model.predict(df)
# print(sum(df["잔차"]**2))

# 7. 회귀 모델의 MSE를 구하시오
# print((df["잔차"]**2).mean())

# print(dir(statsmodels.formula.api))

# 8. 몸무게의 95% 신뢰 구간을 구하시오
# print(model.conf_int(alpha=0.05).loc["몸무게"])

# 9. 몸무게가 50일 때 예측 키의 신뢰 구간과 예측 구간을 구하시오
new = pd.DataFrame({"몸무게": [50]})
pred = model.get_prediction(new)
result = pred.summary_frame(alpha=0.05)
# print(result)