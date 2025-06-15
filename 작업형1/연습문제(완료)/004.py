import pandas as pd

df = pd.read_csv("./type1_data1.csv")
# print(df.head())

# print(df["views"].isna().sum())
df["views"] = df["views"].fillna(0) # 1. views 컬럼의 결측 데이터를 0으로 대체하시오
# print(df["views"].isna().sum())

df = df.sort_values("views", ascending=False)
# print(df.head())

print(df.iloc[9:10]) # 2. views 컬럼에서 상위 10번째 값을 구하시오

value = df.iloc[9]["views"]
# print("value:", value)
df.iloc[:10, df.columns.get_loc("views")] = value # 3. views 컬럼에서 상위 10개의 값을 상위 10번째 값으로 대체하시오

print(df.head(10))

print(int(df["views"].sum())) # 4. views 컬럼의 전체 합을 정수로 구하시오