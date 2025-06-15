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
# print(df.head())
# print(df.shape) # (800, 5)
# print(df.info())

a = df.iloc[:int(df.shape[0]/2)]
b = df.iloc[int(df.shape[0]/2):]
# print(a.shape, b.shape) # (400, 5) (400, 5)

from statsmodels.formula.api import logit

model = logit("target ~ age + service + social + booked", data=df).fit()
model2 = logit("target ~ age + service + booked", data=df).fit()

# age          3.461939e-04 → 0.00034619390
# service      9.221241e-03 → 0.00922124100
# social       6.744710e-02 → 0.06744710000
# booked       1.993372e-09 → 0.00000000199

# print("{:.11f}".format(1.993372e-09))

# print(model2.params) # 회귀계수
# age         -0.093421
# service      0.136369
# booked      -1.243477

llf = model2.llf
# print(llf) # 로그 우도
# print(-2 * llf) # 잔차이탈도
import numpy as np
# print(np.exp(model2.params["booked"]) * 3) # 0.8894844480113174 # 오즈비

# print(model2.params[model2.pvalues < 0.05].sum()) # 0.6805839314625097

# 8. 수정된 모델로 b 데이터를 사용해 예측한 후, b 데이터의 target과 비교해 정확도를 계산하시오. 정확도 0과 1사이의 값이다
pred = model2.predict(b)
pred = (pred>0.5).astype(int)

from sklearn.metrics import accuracy_score
acc = accuracy_score(b["target"], pred)

# print(acc)

# print(1-acc)

# 1) 2
# 2) social
# 3) 0.136369
# 4) -411.60258195174384
# 5) 823.2051639034877
# 6) 0.8651389156692626
# 7) 0.6805839314625097
# 8) 0.77
# 9) 0.22999999999999998