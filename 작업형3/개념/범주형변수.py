# 범주형 변수는 통상적으로 원-핫 인코딩과 같은 방법을 사용해 수치화 한 후 회귀 모델에서 독립변수로 사용할 수 있음

import pandas as pd
from statsmodels.api import ols

df = pd.read_csv("study.csv")

model = ols("score ~ study_hours + material_type", data=df).fit()
print(model.summary)
# print(df.head())