# 유리 식별 데이터에서 유리의 종류를 예측하시오
    # - 제공된 데이터 목록: glass_train.csv, glass_test.csv
    # - 예측할 컬럼: Type(1, 2, 3, 5, 6, 7)
# 학습용 데이터(train.csv)를 이용해 약물 종류를 예측하는 모델을 만든 후, 이를 평가용 데이터(test.csv)에 적용하여 얻은 예측값을 다음과 같은 형식의 csv 파일로 생성하시오
# 제출 파일은 다음 1개의 컬럼을 포함해야 한다
    # pred: 예측값
    # 제출 파일명: result.csv
# 제출한 모델의 성능은 f1-weighted 평가지표에 따라 채점한다

import pandas as pd

train = pd.read_csv("glass_train.csv")
test = pd.read_csv("glass_test.csv")
# print(train.head())
# print(test.head())
# print(train.shape, test.shape) # (149, 10) (65, 9)
# print(train.info()) # 범주형 없음
# print(test.info()) # 범주형 없음
# print(train.isnull().sum()) # 결측치없음
# print(test.isnull().sum()) # 결측치없음

X = train.drop("Type", axis=1)
y = train["Type"]

X_full = pd.concat([X, test], axis=0)
# print(X_full.shape, 149+65) # (214, 9)

# 결측치 제거(결측치 없음), 스케일링(랜덤포레스트 사용), 인코딩 생략(범주형 변수 없음)

X_train = X_full[:train.shape[0]]
X_test = X_full[train.shape[0]:]
# print(X_train.shape, X_test.shape) # (149, 9) (65, 9)

from sklearn.model_selection import train_test_split
X_train, X_val, y_train, y_val = train_test_split(X_train, y, test_size=0.2)
# print(X_train.shape, X_val.shape, y_train.shape, y_val.shape) # (119, 9) (30, 9) (119,) (30,)

from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
model.fit(X_train, y_train)
y_val_pred = model.predict(X_val)

from sklearn.metrics import f1_score
f1 = f1_score(y_val, y_val_pred, average="weighted")

pred = model.predict(X_test)
result = pd.DataFrame(pred, columns=["pred"])
result.to_csv("result.csv", index=False)

# test = pd.read_csv("result.csv")
# print(test.head())
# print(help(sklearn))
# print(dir(sklearn.metrics))

# ensemble, metrics, model_selection