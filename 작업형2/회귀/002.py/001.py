# 노트북 정보로 가격을 예측하시오
    # - 제공된 데이터 목록: laptop_train.csv, laptop_test.csv
    # - 예측할 컬럼: Price
# 학습용 데이터(train)를 이용해 노트북 가격을 예측하는 모델을 만든 후 이를 평가용 데이터(test)에 적용해 얻은 예측값을 다음과 같은 형식의 csv 파일로 생성하시오

# 제출 파일은 다음 1개의 컬럼을 포함해야한다
    # pred: 예측값(가격)
    # 제출 파일명: result.csv
# 제출한 모델의 성능은 결정계수 평가지표에 따라 채점한다.

import pandas as pd

train = pd.read_csv("laptop_train.csv")
test = pd.read_csv("laptop_test.csv")

# print(train.head())
# print(test.head())
# print(train.shape, test.shape) # (91, 10) (39, 9)
# print(train.info())
# print(test.info())
# print(train.isnull().sum())
# print(test.isnull().sum())

X = train.drop("Price", axis=1)
y = train["Price"]
# print(X)
# print(y)

X_full = pd.concat([X, test], axis=0)
# print(X_full.shape) # (130, 9)

# 1. 데이터 전처리

# 1.1 결측치 제거
# print(X_full.isnull().sum())
X_full = X_full.fillna(0)
# print(X_full.isnull().sum())

# 1.2 수치형 스케일링 (생략)

# 1.3 범주형 인코딩
X_full = pd.get_dummies(X_full)
# print(X_full.shape) # (130, 119)

# 2. 테스트/검증용 데이터 분리
X_train = X_full[:train.shape[0]]
X_test = X_full[train.shape[0]:]
# print(X_train.shape, y_train.shape) # (91, 119) (39, 119)

from sklearn.model_selection import train_test_split
X_train, X_val, y_train, y_val = train_test_split(X_train, y, test_size=0.2)
# print(X_train.shape, X_val.shape, y_train.shape, y_val.shape) # (72, 119) (19, 119) (72,) (19,)

# 3. 모델 학습
from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor()
model.fit(X_train, y_train)
y_val_pred = model.predict(X_val)

# 4. 평가
from sklearn.metrics import r2_score
r2 = r2_score(y_val, y_val_pred)
print(r2) # 0.6507095023798211

# 5. 파일 작성
pred = model.predict(X_test)
result = pd.DataFrame(pred, columns=["pred"])
result.to_csv("result.csv", index=False)

test = pd.read_csv("result.csv")
print(test.head())

# print(help(sklearn))
# print(dir(sklearn.metrics))