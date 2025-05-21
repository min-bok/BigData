# 새로운 일자리를 찾을지 예측하시오
    # - 제공된 데이터 목록: hr_train.csv, hr_test.csv
    # - 예측할 컬럼: target(0: 새 일자리를 찾지 않음, 1: 새 일자리를 찾음)
# 학습용 데이터(train)를 이용해 새 일자리를 찾을지 예측하는 모델을 만든 후 이를 평가용 데이터(test)에 적용해 얻은 예측값을 다음과 같은 형식의 CSV 파일로 생성하시오
    # - 제출 파일은 다음 1개의 컬럼을 포함해야한다.
    # - pred: 예측값(이직할 확률)
    # - 제출 파일명: result.csv
# 제출한 모델의 성능은 ROC-AUC 평가지표에 따라 채점한다.

import pandas as pd
import os
dir_path = os.path.dirname(os.path.abspath(__file__))
train_path = os.path.join(dir_path, "hr_train.csv")
test_path = os.path.join(dir_path, "hr_test.csv")

train = pd.read_csv(train_path)
test = pd.read_csv(test_path)
# print(train.head())
# print(test.head())
# print(train.info())
# print(test.info())
# print(train.shape, test.shape)

# 데이터 합쳐서 전처리
X = train.drop(["enrollee_id","target"], axis=1)
y = train["target"]
# print(X.head())
# print(y.head())
X_full = pd.concat([X, test], axis=0)
# print(X_full.shape)
# print(X_full.isnull().sum())
X_full = X_full.fillna(0) # 1. 결측치 처리
# print(X_full.isnull().sum())

# 2. 수치형 변수 스케일링 생략
# 3. 범주형 변수 인코딩
# print(X_full.shape)
X_full = pd.get_dummies(X_full)
# print(X_full.shape)

# 데이터 나누기
X_train = X_full[:train.shape[0]]
X_test = X_full[train.shape[0]:]
# print(X_train.shape, X_test.shape)

# 학습 데이터와 검증 데이터 분리
from sklearn.model_selection import train_test_split
X_train, X_val, y_train, y_val = train_test_split(X_train, y, test_size=0.2)
# print(X_train.shape, X_val.shape, y_train.shape, y_val.shape) # (12260, 197) (3066, 197) (12260,) (3066,)

# 모델 학습 및 검증
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
model.fit(X_train, y_train)
y_val_pred = model.predict_proba(X_val)[:,1]
y_val_pred2 = model.predict(X_val)
# print(y_val_pred)

# 평가
from sklearn.metrics import roc_auc_score, accuracy_score
roc = roc_auc_score(y_val, y_val_pred)
acc = accuracy_score(y_val, y_val_pred2)
# print(roc, acc)

# print(help(sklearn))
# print(dir(sklearn.metrics))

# 파일저장
y_pred = model.predict_proba(X_test)[:,1]
result = pd.DataFrame(y_pred, columns=["pred"])
# print(result.head())
result.to_csv("result.csv", index=False)


