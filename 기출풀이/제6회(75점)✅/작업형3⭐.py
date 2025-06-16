# === 문제1 ===================================
import pandas as pd
df = pd.DataFrame({
    "항암약":[4,4,3,4,1,4,1,4,1,4,4,2,1,4,2,3,2,4,4,4]
    })
# print(df.head(3))

# === 문제2 ===================================
import pandas as pd

# solar   wind     o3  temperature
df = pd.read_csv("data6-3-2.csv")

from statsmodels.formula.api import ols

model = ols("temperature ~ solar + wind + o3", data=df).fit()
# print(model.params["o3"])
# print(model.pvalues["wind"])

new = pd.DataFrame({
    "solar":[100],
    "wind":[5],
    "o3": [30]
})

# print(model.predict(new))

# 1) 0.0749385437813658 ✅
# 2) 0.779717720207169 ✅
# 3) 21.56163 ✅
