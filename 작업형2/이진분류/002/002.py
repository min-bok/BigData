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

# print(train.head(), test.head())
# print(train.shape, test.shape) # (15326, 14) (3832, 13)

X = train.drop(["target"], axis=1)
y = train["target"]
# print(X.head())
# print(y.head())
# print(X.shape, y.shape)

X_full = pd.concat([X, test], axis=0)
# print(X_full.head())
# print(X_full.shape)

# 1. 결측치 채우기
# print(X_full.isnull().sum())
X_full= X_full.fillna(0)
# print(X_full.isnull().sum())

# 2. 수치형 변수 스케일링 생략
# 3. 범주형 변수 원-핫 인코딩
# print(X_full.shape)
X_full = pd.get_dummies(X_full)
# print(X_full.shape)

# 4. 데이터 분리
X_train = X_full[:train.shape[0]]
X_test = X_full[train.shape[0]:]
# print(X_train.shape, X_test.shape) # (15326, 195) (3832, 195)

# 5. 학습데이터와 테스트 데이터로 분리
from sklearn.model_selection import train_test_split
X_train, X_val, y_train, y_val = train_test_split(X_train, y, test_size=0.2)
# print(X_train.shape, X_val.shape, y_train.shape, y_val.shape) # (12260, 195) (3066, 195) (12260,) (3066,)

# 6. 모델 학습
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
model.fit(X_train, y_train)
y_val_pred = model.predict_proba(X_val)[:,1]

# 7. 평가
from sklearn.metrics import roc_auc_score
roc = roc_auc_score(y_val, y_val_pred)
# print(roc) # 0.799627613044814

# 8. 파일작성
y_pred = model.predict_proba(X_test)[:,1]
result = pd.DataFrame(y_pred, columns=["pred"])
# print(result.head())
result.to_csv("result.csv", index=False) # ⭐꼭 .csv 확장자 잊지말기!!!

# path = os.path.join(dir_path, "result.csv")
# test = pd.read_csv(path)
# print(test.head())

# print(help(sklearn))
# print(dir(sklearn.metrics))

# ensemble, metrics

