# 1. index "2001" 데이터(행)에서 평균보다 큰 값의 개수를 구하시오
# 2. index "2003" 데이터(행)에서 평균보다 작은 값의 개수를 구하시오
# 3. 두 개수를 더하시오
import pandas as pd

df = pd.read_csv("./type1_data2.csv", index_col="year")
# print(df.head())

cond1 = df.loc[2001] > df.loc[2001].mean()
cond2 = df.loc[2003] < df.loc[2003].mean()


# print(cond1)
# print(df.loc[2003] < df.loc[2003].mean())
# print(cond1.sum())
# print(cond2.sum())

print(cond1.sum() + cond2.sum())


