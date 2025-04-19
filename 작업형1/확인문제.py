import pandas as pd
import numpy as np

df = pd.DataFrame({
    "메뉴": ["아메리카노", "카페라떼", "에스프레소", "카페모카", "바닐라라떼"],
    "가격" : [4500, 5000, 4000, 5900, 5300],
    "칼로리" : [10, 110, np.NaN, 210, np.NaN],
    "원산지" : ["과테말라", "브라질", "과테말라", np.NaN, np.NaN]
})

# print(df)

# Q1 -------------
cal_min = df["칼로리"].min()
# print(cal_min)
# print(df["칼로리"].isnull())
df["칼로리"].fillna(cal_min, inplace=True)
# df["칼로리"] = df["칼로리"].fillna(cal_min)

# Q2 -------------
type = df["원산지"].mode()[0]
# print(type)
df["원산지"].fillna(type, inplace=True)

# Q3 -------------
price_cond = df["가격"]  >= 5000
# print(len(df[price_cond])) # 3

# Q4 -------------
df["이벤트가"] = df["가격"]/2 # *0.5

# Q5 -------------
df.drop("칼로리", axis=1, inplace=True)

# Q6 -------------
# print(df.loc[:2])

# Q7 -------------
# print(df.iloc[:3])

# Q8 -------------
# temp = df.loc[1:2, ["메뉴", "가격"]] # temp = df.loc[1:2, :"가격"]

# print(temp.info())
# print(df.loc[1:2, ["메뉴", "가격"]])

# Q9 -------------
temp2 = df.iloc[1:3, :2]
# print(temp.info())
# print(temp2)

# Q10 -------------
df.sort_values("가격", ascending=False, inplace=True)
# print(df.reset_index(drop=True).head(3)) # df.iloc[:3]

# print(df)
