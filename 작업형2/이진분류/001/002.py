import pandas as pd

import os
dir_path = os.path.dirname(os.path.abspath(__file__))
train_path = os.path.join(dir_path, "diabetes_train.csv")
test_path = os.path.join(dir_path, "diabetes_test.csv")

train = pd.read_csv(train_path)
test = pd.read_csv(test_path)

# print(train.head())
# print(test.head())
# print(train.info())
# print(test.info())
# print(train.shape)
# print(test.shape)
# print(train.isnull().sum()) # 결측치없음
# print(test.isnull().sum()) # 결측치없음

X = train.drop(["Outcome"], axis=1)
y = train["Outcome"]
# print(X.head())
# print(y.head())

X_full = pd.concat([X, test], axis=0)
# print(X_full.shape)

X_full = X_full.fillna(0) # 결측치 제거
X_full = pd.get_dummies(X_full) # 범주형 변수 원-핫 인코딩
# print(X_full.head())

# 데이터 분리
X_train = X_full[:train.shape[0]]
X_test = X_full[train.shape[0]:]
# print(X_train.shape, X_test.shape)

# 학습데이터와 검증데이터 분리
from sklearn.model_selection import train_test_split
X_train, X_val, y_train, y_val = train_test_split(X_train, y, test_size=0.2)
# print(X_train.shape, X_val.shape, y_train.shape, y_val.shape)

# 모델 학습 및 검증
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
model.fit(X_train, y_train)
y_val_pred = model.predict(X_val)

# 평가
from sklearn.metrics import roc_auc_score, accuracy_score

roc = roc_auc_score(y_val, y_val_pred)
acc = accuracy_score(y_val, y_val_pred)
# print(roc, acc)

# 파일저장
y_pred = model.predict(X_test)
result = pd.DataFrame(y_pred, columns=["pred"])
result.to_csv("result.csv", index=False)



# print(help(sklearn))
# print(dir(sklearn.metrics))

