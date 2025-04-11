# 02. 데이터 저장 및 불러오기
import pandas as pd

df = pd.DataFrame({
    "메뉴": ["아메리카노", "카페라떼", "카페모카", "카푸치노"],
    "가격" : [4500, 5000, 5500, 5000],
    "칼로리": [10, 110, 250, 110]
})

# df.to_csv('temp_csv') # csv로 저장, 동일 경로에 생김
# temp_df = pd.read_csv("temp_csv")
# temp_df.head()

# 아래와 같이 새로 생성된 인덱스 포함하여 저장됨

#    Unnamed: 0     메뉴    가격  칼로리
# 0           0  아메리카노  4500   10
# 1           1   카페라떼  5000  110
# 2           2   카페모카  5500  250
# 3           3   카푸치노  5000  110

# df.to_csv("cafe_csv", index=False) # 인덱스 제외하고 저장
# df = pd.read_csv("cafe_csv")
# print(df.head()) # 5번째 행까지 출력 (default)
# print(df.head(1)) # 1번째 행까지 출력

#       메뉴    가격  칼로리
# 0  아메리카노  4500   10
# 1   카페라떼  5000  110
# 2   카페모카  5500  250
# 3   카푸치노  5000  110

