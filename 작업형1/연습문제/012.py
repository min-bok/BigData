# 1. 결측치가 가장 많은 두 컬럼을 찾으시오
# 2. 첫번째로 결측치가 많은 컬럼에서 결측치가 있는 데이터(행)를 삭제하시오
# 3. 두번째로 결측치가 많은 컬럼을 최빈값으로 대체하시오
# 4. "f3" 컬럼의 "gold"값을 가진 데이터의 수를 정수형으로 구하시오

import pandas as pd

df = pd.read_csv("./type1_data1.csv")
# print(df.head())
# print(df.isnull().sum())

# 결측치 제일 많음 f1: 31
# 두번째 f3: 29

df= df.dropna(subset=["f1"])
val = df["f3"].mode()[0]
# print(val)

df["f3"] = df["f3"].fillna(val)

print(int(sum(df["f3"] == "gold")))

# print(df.isnull().sum())