# 로지스틱 회귀 p.523
import pandas as pd

# age    length  diameter    height     weight  gender
df = pd.read_csv("clam.csv")
# print(df.head())
# print(df.shape) # (300, 6)

train = df[:210]
test = df[210:]
# print(train.shape, test.shape) # (210, 6) (90, 6)

from statsmodels.formula.api import logit

model = logit("gender ~ weight", data=train).fit()

import numpy as np
# print(round(np.exp(model.params["weight"] * 1),4))

# model = logit("gender ~ age + length + diameter + height + weight", data=train).fit()

# llf = model.llf
# print(round(-2 * llf,2))
pred = model.predict(test)
pred = (pred > 0.5).astype(int)

from sklearn.metrics import accuracy_score
acc = accuracy_score(test["gender"], pred)

print(round(1 - acc, 3))

# 1) 1.0047 ✅
# 2) 286.93 ✅
# 3) 0.478 ✅

