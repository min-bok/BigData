# === 문제1 ===================================
import pandas as pd

df = pd.DataFrame({
    "항암약":[4,4,3,4,1,4,1,4,1,4,4,2,1,4,2,3,2,4,4,4]
    })
# print(len(df)) # 20

cond = df["항암약"] == 4
# len(df[cond])
# print(len(df[cond])/len(df))

from scipy.stats import chisquare

관찰빈도 = df["항암약"].value_counts().sort_index().tolist()
기대빈도 = [0.1*20, 0.05*20, 0.15*20, 0.7*20]
# print(관찰빈도, 기대빈도)

stats, pvalue = chisquare(관찰빈도, 기대빈도)
print(stats, pvalue)

# 1) 0.55
# 2) 6.976190476190476
# 3) 0.07266054733847571

# === 문제2 ===================================
# import pandas as pd

# # solar   wind     o3  temperature
# df = pd.read_csv("data6-3-2.csv")

# from statsmodels.formula.api import ols

# model = ols("temperature ~ solar + wind + o3", data=df).fit()
# # print(model.params["o3"])
# # print(model.pvalues["wind"])

# new = pd.DataFrame({
#     "solar":[100],
#     "wind":[5],
#     "o3": [30]
# })

# print(model.predict(new))

# 1) 0.0749385437813658 ✅
# 2) 0.779717720207169 ✅
# 3) 21.56163 ✅
