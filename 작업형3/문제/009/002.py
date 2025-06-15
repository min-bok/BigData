# 주어진 데이터를 사용하여 데이터를 앞 50%의 a와 나머지 50%의 b로 나누십시오.
# a 데이터로 로지스틱 회귀 모델을 적합하고, 다음 문제에 답하시오

# 1. 종속변수 target과 모든 독립변수를 사용하여 로지스틱 회귀 모델을 적합하고, 유의하지 않은 독립변수의 개수를 구하시오 (유의수준 0.05)
# 2. p-value가 0.05보다 작은 유의한 변수만 사용하여 수정된 모델을 만들고 적합하시오. 이 수정된 모델에서 가장 큰 p-value를 가진 변수의 이름을 구하시오
# 3. 수정된 모델에서 독립변수 중 가장 큰 양의 회귀계수를 가진 변수의 이름을 구하시오
# 4. 수정된 모델에서 로그 우도를 구하시오
# 5. 수정된 모델에서 잔차이탈도를 구하시오
# 6. 수정된 모델에서 booked 변수가 3 증가할 때 오즈비를 계산하시오
# 7. 수정된 모델에서 p-value가 0.05보다 작은 회귀계수의 총합을 구하시오. 단 상수항(절편) 회귀게수도 유의할 경우 포함하시오
# 8. 수정된 모델로 b 데이터를 사용해 예측한 후, b 데이터의 target과 비교해 정확도를 계산하시오. 정확도 0과 1사이의 값이다
# 9. 8에서 계산된 정확도를 바탕으로 오류율을 계산하시오

import pandas as pd

# age  service  social  booked  target
df = pd.read_csv("customer_travel.csv")
# print(df.sample())
# print(df.shape) # (800, 5)

midpoint = len(df)//2
a = df.iloc[:midpoint]
b = df.iloc[midpoint:]
# print(a.shape, b.shape) # (400, 5) (400, 5)

from statsmodels.formula.api import logit
model = logit("target ~ age + service + social + booked", data=a).fit()
# print(sum(model.pvalues[1:] >= 0.05))

model = logit("target ~ age + service + booked", data=a).fit()
# print(model.pvalues[1:].idxmax())

# print(model.params[1:].idxmax())

llf = model.llf
# print(llf)
# print(-2*llf)

import numpy as np
# print(np.exp(model.params["booked"] * 3))

# print(sum(model.params[model.pvalues < 0.05]))

pred = model.predict(b)
pred = (pred>0.5).astype(int)

from sklearn.metrics import accuracy_score
acc = accuracy_score(b["target"] ,pred)
# print(acc) # 0.765

print(1-acc)

# 1) 2
# 2) service
# 3) service
# 4) -211.31019836322204
# 5) 422.6203967264441
# 6) 0.05475575748985911
# 7) 1.292605228739193
# 8) 0.765
# 9) 0.235