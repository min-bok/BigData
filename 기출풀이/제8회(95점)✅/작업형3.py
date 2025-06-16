# === 문제1 ==============================
# 1. 주어진 데이터에서 로지스틱 회귀 분석을 수행해 유의확률이 0.05 이상인 유의하지 않는 독립변수의 개수를 구하시오
# 2. 유의확률이 0.05 미만인 유의한 변수만을 사용해 다시 로지스틱 회귀 분석을 수행하시오. 이 회귀식의 유의한 회귀 계수(상수항 포함)의 합계를 구하시오 (반올림하여 소수 셋째자리까지 계산)
# 3. 문제 2에서 수행한 로지스틱 회귀식에서 "DataUsage" 변수가 5만큼 증가할때 오즈비를 구하시오 (반올림하여 소수 셋째자리까지 계산)
# import pandas as pd

# # Churn  AccountWeeks  ContractRenewal  DataPlan  DataUsage  CustServCalls  DayMins  DayCalls  MonthlyCharge  OverageFee  RoamMins
# df = pd.read_csv("churn.csv")
# # print(df.head())

# from statsmodels.formula.api import logit
# model = logit("Churn ~ AccountWeeks + ContractRenewal + DataPlan + DataUsage + CustServCalls + DayMins + DayCalls + MonthlyCharge + OverageFee + RoamMins", data=df).fit()
# # print(sum(model.pvalues > 0.05))

# model = logit("Churn ~ DataUsage + DayMins", data=df).fit()
# # print(model.pvalues < 0.05)
# # print(round(sum(model.params),3))

# import numpy as np

# ozbi = np.exp(model.params["DataUsage"] * 5)
# print(round(ozbi, 3)) # 0.428

# --- 답 ------------
# 1) 8 ✅
# 2) -1.213 ✅
# 3) 0.428 ✅

# === 문제2 ==============================
# 1. 주어진 데이터를 이용해 종속변수(PIQ)와 독립변수(Brain, Height, Weight)로 다중 선형 회귀 분석을 수행하시오. 
#    이때 유의확률이 가장 작은 변수의 회귀 계수값을 구하시오 (반올림하여 소수 셋째자리까지 계산)
# 2. 문제 1에서 적합한 모델의 결정계수 값을 구하시오 (반올림하여 소수 셋째자리까지 계산)
# 3. 뇌 크기(Brain)가 90, 키(Height)가 70, 몸무게(Weight)가 150일 때의 PIQ를 예측하시오 (반올림하여 정수로 계산)

import pandas as pd

# PIQ  Brain  Height  Weight
df = pd.read_csv("piq.csv")
# print(df.head())
# print(df.shape) # (50, 4)
# print(df.info())

from statsmodels.formula.api import ols

model = ols("PIQ ~ Brain + Height + Weight", data=df).fit()
# print(round(model.params[model.pvalues.idxmin()],3))
# print(model.summary())

# print(round(model.rsquared,3))

new = pd.DataFrame({
    "Brain":[90],
    "Height": [70],
    "Weight": [150]
})

# print(int(model.predict(new)))

# --- 답 ------------
# 1) 2.343 ✅
# 2) 0.37 ✅
# 3) 106 ✅