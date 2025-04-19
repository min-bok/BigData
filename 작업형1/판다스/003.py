# 03. 탐색적 데이터 분석(EDA)
import pandas as pd

df = pd.DataFrame({
    "메뉴": ["아메리카노", "카페라떼", "카페모카", "카푸치노"],
    "가격" : [4500, 5000, 5500, 5000],
    "칼로리": [10, 110, 250, 110]
})

# 1. 데이터 프레임 샘플 확인 ------------------------------------------------------------
# print(df.head(2))
# print(df.tail(2))
# print(df.sample(2)) # 기본값 1, 실행할때마다 달라짐, 순서없는듯

# 2. 데이터 프레임의 크기 ------------------------------------------------------------
# print(df.shape) # (4, 3), 전체 데이터의 크기 확인


# 3. 컬럼별 자료형 ------------------------------------------------------------
# print(df.info())

#  #   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   메뉴      4 non-null      object # object = 문자
#  1   가격      4 non-null      int64  # int = 숫자, 비트는 무시해도 됨
#  2   칼로리     4 non-null      int64

# 4. 상관 관계------------------------------------------------------------

# print(df.corr(numeric_only=True)) # 상관 관계 분석, numeric_only=True은 숫자형 데이터에만 적용되도록 하는 옵션션

#            가격       칼로리
# 가격   1.000000  0.993127
# 칼로리  0.993127  1.000000

# 5. 범주형 데이터 탐색 ------------------------------------------------------------
df_car = pd.DataFrame({
    "car": ['Sedan', 'SUV', 'Sedan', 'SUV', 'SUV', 'SUV', 'Sedan', 'Sedan', 'Sedan', 'Sedan', 'Sedan'],
    "size": ["S", "M", "S", "S", "M", "M", "L", "S", "S", "M", "S"]
})

# print(df_car.head(3))

# 6. 고유한 값의 개수 ------------------------------------------------------------
  # - nunique() : 컬럼별로 고유한 값의 개수를 찾을때
  # - unique() : 구체적인 항목 파악
  # - value_counts() : nunique와 unique의 결과 내용을 한번에 파악
  # - describe() : 수치형 데이터(int, float)의 기술통계
    #   - 범주형 데이터의 경우 include="object" 또는 include="O" 옵션 추가

# print(df_car.nunique()) # car의 종류는 2개, size의 종류는 3개

# car     2
# size    3
# dtype: int64

# print(df_car["car"].unique()) # ['Sedan' 'SUV']
# print(df_car["size"].unique()) # ['S' 'M' 'L']

# print(df_car["car"].value_counts())
# car
# Sedan    7
# SUV      4

# print(df_car["size"].value_counts())
# size
# S    6
# M    4
# L    1

# print(df.describe()) # 수치형 데이터(int, float)의 기술통계
#              가격       칼로리
# count     4.00000    4.000000 # 값이 있는 데이터 수
# mean   5000.00000  120.000000 # 평균
# std     408.24829   98.657657 # 표준편차
# min    4500.00000   10.000000 # 최솟값
# 25%    4875.00000   85.000000 # 백분위수 25%
# 50%    5000.00000  110.000000 # 백분위수 50%
# 75%    5125.00000  145.000000 # 백분위수 75%
# max    5500.00000  250.000000 # 최댓값

# print(df_car.describe(include="object")) # 범주형 데이터의 기술통계
#           car size
# count      11   11  # 값이 있는 데이터 수
# unique      2    3  # 고유한 데이터 수 (종류)
# top     Sedan    S  # 가장 많이 나오는 값 (최빈값)
# freq        7    6  # 가장 많이 나오는 값의 빈도수

