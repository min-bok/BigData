# 1. 결측치가 있는 행을 삭제하시오
# 2. 결측치가 삭제된 데이터를 사용하여 지역별(city) 평균을 계산하시오
# 3. 앞에서 계산한 지역별 평균 데이터에서 f2 컬럼 값이 가장 큰 지역을 구하시오
import pandas as pd

df = pd.read_csv("./type1_data1.csv")
# print(df.head())
# print(df.isnull().sum())
# print(df.shape)
df = df.dropna()
# print(df.shape)
# print(df.isnull().sum())

filtered = df.groupby(["city"]).mean(numeric_only=True)
print(filtered["f2"].idxmax()) # 서울
# print(df.head())
# print(df["city"].mean())