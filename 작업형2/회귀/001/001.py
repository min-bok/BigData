# 항공권 티켓 가격을 예측하시오.
    # - 제공된 데이터 목록: flight_train.csv, flight_test.csv
    # - 예측할 컬럼: price
# 학습용 데이터(train)를 이용해 티켓 가격을 예측하는 모델을 만든 후 이를 평가용 데이터(test)에 적용해 얻은 예측값을 다음과 같은 형식의 csv 파일로 생성하시오
    # 제출 파일은 다음 1개의 컬럼을 포함해야한다.
        # - pred: 예측값(가격)
        # - 제출 파일명: result.csv
    # 제출한 모델의 성능은 RMSE 평가지표에 따라 채점한다

# price

import pandas as pd

train = pd.read_csv("./flight_train.csv")
test = pd.read_csv("./flight_test.csv")

# print(train.head())
# print(test.head())
# print(train.info())
# print(test.info())
# print(train.shape, test.shape) # (10505, 11) (4502, 10)

X = train.drop("price", axis=1)
y = train["price"]
# print(X.head())
# print(y.head())

# 1. 데이터 합쳐서 전처리
X_full = pd.concat([X, test], axis=0)
# print(X_full.shape) # (15007, 10)
# print(10505 + 4502)

# 1.1 결측지 제거 - 생략
# print(X_full.isnull().sum()) # 데이터에 결측치없음

# 1.2 수치형 스케일링 - 생략(랜덤포레스트 사용할거라)

# 1.3 범주형 원-핫 인코딩
X_full = pd.get_dummies(X_full)
# print(X_full.shape) # (15007, 1267)

# 1.4 데이터 분리
X_train = X_full[:train.shape[0]]
X_test = X_full[train.shape[0]:]

# print(X_train.shape, X_test.shape) # (10505, 1267) (4502, 1267)

# 1.5 학습용과 검증용 데이터 분리
from sklearn.model_selection import train_test_split
X_train, X_val, y_train, y_val = train_test_split(X_train, y, test_size=0.2)

# print(X_train.shape, X_val.shape, y_train.shape, y_val.shape) # (8404, 1267) (2101, 1267) (8404,) (2101,)

# 2. 모델 학습
from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor()
model.fit(X_train, y_train)
y_val_pred = model.predict(X_val)

# 3. 평가(RMSE)
# root_mean_squared_error 3547.6661167077427
from sklearn.metrics import mean_squared_error
rmse = mean_squared_error(y_val, y_val_pred) ** 0.5 # 3787.941980453744
# print(rmse)

# 4. 파일작성
y_pred = model.predict(X_test)
result = pd.DataFrame(y_pred, columns=["pred"])
result.to_csv("result.csv", index=False)

test = pd.read_csv("./result.csv")
print(test.head())

# print(help(sklearn))
# print(dir(sklearn.metrics))