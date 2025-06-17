# p.539
# 1. 주어진 데이터에서 로지스틱 회귀 분석을 수행해 유의확률이 0.05 이상인 유의하지 않는 독립변수의 개수를 구하시오
# 2. 유의확률이 0.05 미만인 유의한 변수만을 사용해 다시 로지스틱 회귀 분석을 수행하시오. 이 회귀식의 유의한 회귀 계수(상수항 포함)의 합계를 구하시오 (반올림하여 소수 셋째자리까지 계산)
# 3. 문제 2에서 수행한 로지스틱 회귀식에서 "DataUsage" 변수가 5만큼 증가할때 오즈비를 구하시오 (반올림하여 소수 셋째자리까지 계산)
import pandas as pd

#  Churn  AccountWeeks  ContractRenewal  DataPlan  DataUsage  CustServCalls  DayMins  DayCalls  MonthlyCharge  OverageFee  RoamMins
df = pd.read_csv("churn.csv")
# print(df.head())

from statsmodels.formula.api import logit
# model = logit("Churn ~ AccountWeeks + ContractRenewal +  DataPlan +  DataUsage +  CustServCalls +  DayMins +  DayCalls +  MonthlyCharge +  OverageFee +  RoamMins", data=df).fit()

# print(sum(model.pvalues.iloc[1:] >= 0.05))
# print(model.pvalues.iloc[1:] < 0.05)

model = logit("Churn ~ DataUsage + DayMins", data=df).fit()
# print(round(sum(model.params),3))

import numpy as np

ozbi = np.exp(model.params["DataUsage"] * 5)
print(round(ozbi,3))

# 1) 8 ✅
# 2) -1.213 ✅
# 3) 0.428 ✅