# 자동차 정보로 중고차 가격을 예측하시오
    # 제공된 데이터 목록: car_train.csv, car_test.csv
    # 예측할 컬럼: price
# 학습용 데이터(train)를 이용해 중고차 가격을 예측하는 모델을 만든 후 이를 평가용 데이터(test)에 적용해 얻은 예측값을 다음과 같은 형식의 csv 파일로 생성하시오
# 제출 파일은 다음 1개의 컬럼을 포함해야 한다
    # pred: 에측값(가격)
    # 제출 파일명: result.csv
# 제출한 모델의 성능은 RMSLE 평가지표에 따라 채점한다.

import pandas as pd

train = pd.read_csv("car_train.csv")
test = pd.read_csv("car_test.csv")

# print(train.head())
# print(test.head())
# print(train.shape, test.shape) # (6732, 17) (5772, 16)
# print(train.info())
# print(test.info())
# print(train.isnull().sum()) # 데이터에 결측치 없음
# print(test.isnull().sum()) # 데이터에 결측치 없음

# 1. 데이터 합치기
X_train = train.drop(["Price"], axis=1)
y = train["Price"]
# print(X_train.head())
# print(X_train.shape)
# print(X_test.head())
# print(X_test.shape)

X_full = pd.concat([X_train, test], axis=0)

# print(X_full.shape, 6732+5772) # (12504, 16)

# 1.1 결측치 처리 (생략)
# print(X_full.isnull().sum())

# 1.2 스케일링 (생략)

# 1.3 인코딩
X_full = pd.get_dummies(X_full)
# print(X_full.shape) # (12504, 7501)

# 2. 데이터 분리

X_train = X_full[:train.shape[0]]
X_test = X_full[train.shape[0]:]

# print(X_train.shape, X_test.shape) # (6732, 7501) (5772, 7501)

from sklearn.model_selection import train_test_split
X_train, X_val, y_train, y_val = train_test_split(X_train, y, test_size=0.2)
# print(X_train.shape, X_val.shape, y_train.shape, y_val.shape) # (5385, 7501) (1347, 7501) (5385,) (1347,)

# 3. 모델 학습
from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor()
model.fit(X_train, y_train)
y_val_pred = model.predict(X_val)

# 4. 성능평가
from sklearn.metrics import mean_squared_log_error
msle = mean_squared_log_error(y_val, y_val_pred) ** 0.5
# print(msle) # 1.1885337369832751

# 5. 파일작성
pred = model.predict(X_test)
result = pd.DataFrame(pred, columns=["pred"])
result.to_csv("result.csv", index=False)

test = pd.read_csv("result.csv")
print(test.head())

# print(help(sklearn))
# print(dir(sklearn.metrics))

# ensemble, metrics(RMSLE)