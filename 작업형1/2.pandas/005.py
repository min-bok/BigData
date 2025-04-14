# 05. 새로운 컬럼 추가
import pandas as pd

df = pd.read_csv("작업형1/2.pandas/cafe_csv")
# print(df.head(2))

df["new"] = 0
# print(df.head(2))

#       메뉴    가격  칼로리  new
# 0  아메리카노  4500   10    0
# 1   카페라떼  5000  110    0

discount = 0.2
df["할인가"] = df["가격"] * (1-discount)
print(df.head(2))

#       메뉴    가격  칼로리  new     할인가
# 0  아메리카노  4500   10    0  3600.0
# 1   카페라떼  5000  110    0  4000.0