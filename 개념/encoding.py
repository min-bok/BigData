# 범주형(텍스트)데이터를 숫자로 변환하는 과정으로 머신러닝 모델에 입력 데이터로 사용하기 위한 필수과정

import pandas as pd

train = pd.read_csv("train.csv")
# print(train.head())
# print(train.shape) # (29304, 16)

# (1) 원-핫 인코딩 ⭐이것만 알아두기⭐
# train = pd.get_dummies(train)
# print(train.shape) # (29304, 108)

# (2) 레이블 인코딩
# from sklearn.preprocessing import LabelEncoder

# cols = train.select_dtypes(include="object").columns.tolist()

# for col in cols:
#     le = LabelEncoder()
#     train[col] = le.fit_transform(train[col])

# print(train.head())