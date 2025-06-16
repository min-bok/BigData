# === 문제1 ================================
# import pandas as pd

#    age    length  diameter    height     weight  gender
# df = pd.read_csv("clam.csv")
# print(df.head())
# print(df.info())

# train = df[:210]
# test = df[210:]
# print(train.shape, test.shape) # (210, 6) (90, 6)

# from statsmodels.formula.api import logit

# model = logit("gender ~ weight", data=train).fit()

# import numpy as np
# print(round(np.exp(model.params["weight"] * 1),4))

# model = logit("gender ~ age + length + diameter +  height + weight", data=train).fit()
# llf = model.llf
# print(round(-2 * llf, 2))

# pred = model.predict(test)

# print(round(np.exp(pred),3))

# 1) 1.0047 ✅
# 2) 286.93 ✅
# 3) 모르겠음

# === 문제2 ================================
import pandas as pd

# ERP  Feature1  Feature2  Feature3    CPU
df = pd.read_csv("system_cpu.csv")
# print(df.head())
# print(df.shape) # (115, 5)

cond = df["CPU"] < 100
df = df[cond]

from statsmodels.formula.api import ols

df_corr = df.corr()["ERP"].iloc[1:].max()
# print(round(df_corr, 3))

model = ols("ERP ~ Feature1 + Feature2 + Feature3 + CPU", data=df).fit()
# print(round(model.rsquared,3))
print(round(model.pvalues.iloc[1:].max(),3))


# 1) 0.882 ✅
# 2) 0.755 ✅
# 3) 0.684 ✅