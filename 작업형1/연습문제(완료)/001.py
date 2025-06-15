import pandas as pd
df = pd.read_csv("./type1_data1.csv")

# print(df.head(3))

cond1 = df["f5"] != 0
df = df[cond1]

min = df["views"].min()

# print("결측치 수정전:", df["views"].isnull().sum())
df["views"].fillna(min, inplace=True)
# print("결측치 수정후:", df["views"].isnull().sum())

print(int(df["views"].median()))

# print(df)