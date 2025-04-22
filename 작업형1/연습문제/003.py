import pandas as pd

df = pd.read_csv("type1_data1.csv")

# print(df.head())

# 1. 결측치가 있는 데이터(행) 삭제
# print(df.isnull().sum())
df = df.dropna()
# print(df.isnull().sum())

# 2. views 컬럼을 f1컬럼으로 나눈 값을 새로운 컬럼으로 추가
new = df["views"] / df["f1"]
df["new"] = new

# print(df.head())

# 3. 새로운 컬럼 값 중 가장 큰 값을 가진 행의 age를 정수로 구하기
# print(df.sort_values("new", ascending=False)) # 내림차순 정렬
df = df.sort_values("new", ascending=False)
# print(df.head())
print(int(df.iloc[0]["age"]))

