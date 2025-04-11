# 01. 데이터프레임과 시리즈

import pandas as pd

menu = pd.Series(["비빔밥", "김치찌개", "된장찌개"]) # 시리즈
price = pd.Series(["1000", "2000", "3000"])

df = pd.DataFrame({
    "menu": menu, 
    "price": price
}) # 데이터프레임

# print(df)

# print(df["menu"], type(df["menu"])) # 시리즈로 불러오기
# print(df[["menu"]], type(df[["menu"]])) # 데이터프레임으로 불러오기

cols = ["menu", "price"]

print(df[cols])