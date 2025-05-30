# 신용카드 신청자의 채무 불이행을 예측하시오
    # 제공된 데이터 목록: creditcard_train.csv, creditcard_test.csv
    # 에측할 컬럼: target(0: 채무 이행, 1: 채무 불이행)
# 학습용 데이터(train)를 이용해 신용카드 신청자의 데이터를 바탕으로 미래의 채무 불이행을 예측하는 모델을 만든 후 이를 평가용 데이터(test)에 적용해 얻은 예측값을 다음과 같은 형식의 CSV 파일로 생성하시오

# 제출 파일은 다음 1개의 컬럼을 포함해야 한다
    # - pred: 예측값
    # - 제출파일명: result.csv
# 제출한 모델의 성능은 f1 평가지표에 따라 채점한다.

import pandas as pd

train = pd.read_csv("creditcard_train.csv")
test = pd.read_csv("creditcard_test.csv")

# print(train.shape, test.shape) # (25519, 19) (7591, 18)
# print(set(train.columns) - set(test.columns)) # STATUS
# print(train.isnull().sum())
# print(test.isnull().sum())

# 1. 데이터 전처리
X = train.drop("STATUS", axis=1)
y = train["STATUS"]
# print(X.shape, y.shape) # (25519, 18) (25519,)

X_full = pd.concat([X, test], axis=0)
# print(X_full.shape, 25519+7591) # (33110, 18) 33110

# 1.1 결측치 제거
# print(X_full.isnull().sum())
X_full = X_full.fillna(0)
# print(X_full.isnull().sum())

# 1.2 스케일링 (생략)
# 1.3 인코딩
# print(X_full.shape) # (33110, 18)
X_full = pd.get_dummies(X_full)
# print(X_full.shape) # (33110, 56)

# 1.4 데이터 분리
X_train = X_full[:train.shape[0]]
X_test = X_full[train.shape[0]:]
# print(X_train.shape, X_test.shape) # (25519, 56) (7591, 56)

# 2. 학습용, 테스트용 데이터 분리
from sklearn.model_selection import train_test_split

X_train, X_val, y_train, y_val = train_test_split(X_train, y, test_size=0.2)
# print(X_train.shape, X_val.shape, y_train.shape, y_val.shape)  # (20415, 56) (5104, 56) (20415,) (5104,)

# 3. 모델 학습
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
model.fit(X_train, y_train)
y_val_pred = model.predict(X_val)

# 4. 성능평가
from sklearn.metrics import f1_score
f1 = f1_score(y_val, y_val_pred)

# print(f1) # 0.2631578947368421

# 5. 파일작성 및 확인
pred = model.predict(X_test)
result = pd.DataFrame(pred, columns=["pred"])
result.to_csv("result.csv", index=False)

test = pd.read_csv("result.csv")
print(test.head())

# print(help(sklearn))
# print(dir(sklearn.metrics))

# model_selection
# ensemble
# metrics