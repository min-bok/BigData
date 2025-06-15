# 로지스틱 회귀
# 주어진 데이터를 사용하여 데이터를 앞 50%의 a와 나머지 50%의 b로 나누십시오.
# a 데이터로 로지스틱 회귀 모델을 적합하고, 다음 문제에 답하시오

import pandas as pd

df = pd.read_csv("customer_travel.csv")
# print(df.head())

midpoint = len(df) // 2
a = df.iloc[:midpoint]
b = df.iloc[midpoint:]
# print(a.shape, b.shape)

# 유의하다 = p < 0.05
# 1. 종속변수 target과 모든 독립변수를 사용하여 로지스틱 회귀 모델을 적합하고, 유의하지 않은 독립변수의 개수를 구하시오 (유의수준 0.05)
from statsmodels.formula.api import logit

model = logit("target ~ age + service + social + booked", data=a).fit()
# print("1)", sum(model.pvalues[1:] >= 0.05)) # 2
print(model.pvalues)



# 2. p-value가 0.05보다 작은 유의한 변수만 사용하여 수정된 모델을 만들고 적합하시오. 이 수정된 모델에서 가장 큰 p-value를 가진 변수의 이름을 구하시오
model = logit("target ~ age + service + booked", data=a).fit()
# print("2)", model.pvalues[1:].idxmax()) # service

# 3. 수정된 모델에서 독립변수 중 가장 큰 양의 회귀계수를 가진 변수의 이름을 구하시오
# print("3)", model.params[1:].idxmax()) # service

# 4. 수정된 모델에서 로그 우도를 구하시오
llf = model.llf
# print("4)", llf) # -211.31019836322204

# 5. 수정된 모델에서 잔차이탈도를 구하시오
# print("5)", -2 * llf) # 422.6203967264441

# 6. 수정된 모델에서 booked 변수가 3 증가할 때 오즈비를 계산하시오
# print("6)", model.params["booked"] * 3) # -2.9048727561822836

# 7. 수정된 모델에서 p-value가 0.05보다 작은 회귀계수의 총합을 구하시오. 단 상수항(절편) 회귀게수도 유의할 경우 포함하시오
# print("7)", model.params[model.pvalues<0.05].sum()) # 1.292605228739193

# 8. 수정된 모델로 b 데이터를 사용해 예측한 후, b 데이터의 target과 비교해 정확도를 계산하시오. 정확도 0과 1사이의 값이다
pred = model.predict(b)
pred = (pred>0.5).astype(int)

from sklearn.metrics import accuracy_score
acc = accuracy_score(b["target"], pred)
# print("8)", acc) # 0.765

# 9. 8에서 계산된 정확도를 바탕으로 오류율을 계산하시오
errRate = 1 - acc
# print("8)", errRate) # 0.235