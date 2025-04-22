# 머신러닝 실습(분류)
import pandas as pd

train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")

# 탐색적 데이터 분석(EDA) ---------------------------------------------------

# 1. 데이터 샘플 확인
# print(train.head())

# 2. 데이터 크기 확인
# print(train.shape, test.shape) # (29304, 16) (3257, 15) 3257개의 행(레코드), 16개의 컬럼

# 3. 자료형 확인
# print(train.info()) # 머신러닝의 입력 데이터로 활용하기 위해서는 object형을 반드시 수치형(float, int)으로 변환 필요

# 4. 수치형 컬럼의 기초 통계 값 확인
# print(train.describe())
# print(test.describe())

# 5. 범주형 컬럼의 기초 통계 값 확인
# print(train.describe(include="object"))
# print(test.describe(include="object"))

# 6. 결측치 확인
# print(train.isnull().sum())
# print(test.isnull().sum())

# 6. target(카테고리)의 빈도수 확인
    # - 이진 분류 인지 / 불균형 데이터인지 확인
# print(train["income"].value_counts())

# 데이터 전처리 ---------------------------------------------------
    # 머신러닝의 입력데이터로 만들려면 1. 결측치 채우거나 삭제 2. 중복값 제거 3. 모든 데이터를 숫자형태로 변경
    # 이상치는 문제에서 명시할시 처리, 데이터정규화(스케일링)은 선택사항

# 1. 결측치 처리 -------------------
    # 데이터 전처리 시 train과 test 모두에 적용 필요함 
    # 삭제: 
      # - 행 삭제: dropna(), dropna(subset=["컬럼명", "컬럼명"])
      # - 열 삭제: dropna(axis=1), dropna(["컬럼명", "컬럼명"], axis=1)
    # 채우기
      # - 범주형 : 주로 최빈값으로 대체(mode(),fillna()), 유니크한 값으로 대체 ex) X 
      # - 수치형 : 중앙값(median()), 평균값(mean())으로 대체

# 2. 이상치 처리 -------------------
# print(train.shape)
# train = train[train["age"] > 0]
# print(train.shape)
# print(train[train["age"]<0])

# 3. 인코딩 -------------------
  # 범주형 데이터를 숫자로 변환 (필수과정)
  # 1. 원-핫 인코딩, 2. 레이블 인코딩

y_train = train.pop("income") # 인코딩, 스케일링 전에 label 컬럼을 변수에 옯겨 두기 (대입 및 기존에서 삭제 처리)

# 1. 원-핫 인코딩
# train_oh = pd.get_dummies(train)
# test_oh = pd.get_dummies(test)
# print(train.shape, test.shape, train_oh.shape, test_oh.shape) # 인코딩 후 컬럼 갯수 불일치 발생 -> 데이터 합쳐서 인코딩 필요
# (심화) 데이터 합치기
# print(train.shape, test.shape)
# data = pd.concat([train, test], axis=0) # 열로 붙임
# data_oh = pd.get_dummies(data)
# trian_oh = data_oh.iloc[:len(train)].copy()
# test_oh = data_oh.iloc[len(train):].copy()
# print(trian_oh.shape, test_oh.shape)

# 2. 레이블 인코딩
    # 레이블 인코딩할 object 자료형 컬럼명을 리스트 형태로 만든다
cols = train.columns[train.dtypes == object]

from sklearn.preprocessing import LabelEncoder

for col in cols:
    le = LabelEncoder()
    train[col] = le.fit_transform(train[col])
    test[col] = le.fit_transform(test[col])

# print(cols)
print(train.info())