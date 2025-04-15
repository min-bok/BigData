# 08. 인덱싱/슬라이싱
import pandas as pd

# 01. 인덱싱 ----------------------------------
df = pd.read_csv("작업형1/2.pandas/cafe_csv")
df.drop(0, axis=0, inplace=True)
# print(df.head(2))

# print(df.iloc[0]) # 순서 0번 가져옴
# print(df.loc[0]) # 0번 인덱스를 가진게 없어서 에러

# print(df.loc[1, "메뉴"]) # 카페라떼
# print(df.iloc[0, 0]) # 카페라떼