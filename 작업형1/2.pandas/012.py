# 12. 결측치 처리
import pandas as pd

df = pd.read_csv("./cafe2.csv")
# print(df)

# 1. 결측치 탐색 -------------------------------------------------------

# print(df.isnull()) # 결측치 확안, 결측치이면 True 반환
#       메뉴     가격    칼로리    원산지
# 0  False  False  False  False
# 1  False  False  False   True
# 2  False  False  False  False
# 3  False  False  False  False
# 4  False  False   True   True

# print(df.isnull().sum()) # 컬럼별 결측치 수 확인
# 메뉴     0
# 가격     0
# 칼로리    1
# 원산지    2 # 원산지 컬럼에 결측치 2개 있음
# dtype: int64

# print(df.isna()) # isnull과 동일한 결과
#       메뉴     가격    칼로리    원산지
# 0  False  False  False  False
# 1  False  False  False   True
# 2  False  False  False  False
# 3  False  False  False  False
# 4  False  False   True   True

# 2. 결측치 채우기 -------------------------------------------------------
df["원산지"].fillna("코스타리카", inplace=True) # 원산지 컬럼의 결측치를 코스타리카로 채우기
df["칼로리"].fillna("100", inplace=True)
# print(df.isna().sum())
# print(df)

df.to_csv("cafe3.csv", index=False) # 결측치 처리된 값을 cafe3.csv로 저장