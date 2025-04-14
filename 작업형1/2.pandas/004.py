# 04. 자료형 변환
# astype("변경할 자료형")
# 판다스에서 주로 볼 수 있는 자료형은 int(정수), float(실수), object(문자)

import pandas as pd

df = pd.DataFrame({
    "메뉴": ["아메리카노", "카페라떼", "카페모카", "카푸치노", "에스프레소", "밀크티", "녹차"],
    "가격" : [4500.0, 5000.0, 5500.0, 5000.0, 4000.0, 5900.0, 5300.0],
    "칼로리": ["10", "110", "250", "110", "20", "210", "0"]
})

# print(df["가격"])
# print(df.info())

# df["가격"] = df["가격"].astype("int") # int형으로 변환

# print(df["가격"])
# print(df.info())

# print(df["칼로리"])
# df["칼로리"] = df["칼로리"].astype("float")
# print(df["칼로리"])
# print(df.info)

# df["메뉴"] = df["메뉴"].astype("float") # ValueError: could not convert string to float: '아메리카노'