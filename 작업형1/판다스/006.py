# 06. 데이터 삭제
    # - axis=0 : 행 삭제
    # - axis=1 : 열 삭제

import pandas as pd

df = pd.read_csv("작업형1/2.pandas/cafe_csv")
print(df.head())

#       메뉴    가격  칼로리
# 0  아메리카노  4500   10
# 1   카페라떼  5000  110
# 2   카페모카  5500  250
# 3   카푸치노  5000  110

# 1. 행(로우) 삭제 --------------------------------------
# df.drop(1, axis=0, inplace=True) # 인덱스 1번인 행 삭제하고 저장 (기본값은 False)

# print(df.head())

# 2. 열(컬럼) 삭제 --------------------------------------
# df = df.drop("칼로리", axis=1)
# print(df.head())

#       메뉴    가격  칼로리
# 0  아메리카노  4500   10
# 1   카페라떼  5000  110
# 2   카페모카  5500  250
# 3   카푸치노  5000  110
#       메뉴    가격
# 0  아메리카노  4500
# 1   카페라떼  5000
# 2   카페모카  5500
# 3   카푸치노  5000

# 3. 삭제 후 저장하기 --------------------------------------
# 결과를 저장하는 경우 inplace 또는 대입 연산자 사용, 대신 둘 중 하나만 사용해야함
# inplace는 반환 값이 없고, 사용하지않으면 반환 값으로 대입이 가능함
# 삭제 실수를 방지하기 위해 삭제 전후 데이터 크기를 df.shape로 확인하는 방법을 추천

# print("삭제전:", df.shape)
# df.drop(1, axis=0, inplace=True)
# print("삭제후:", df.shape)

#       메뉴    가격  칼로리
# 0  아메리카노  4500   10
# 1   카페라떼  5000  110
# 2   카페모카  5500  250
# 3   카푸치노  5000  110
# 삭제전: (4, 3)
# 삭제후: (3, 3)