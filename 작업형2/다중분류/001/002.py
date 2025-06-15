# 은행 정보로 신용 등급을 예측하시오
    # - 제공된 데이터 목록: score_train.csv, score_test.csv
    # - 예측할 컬럼: Credit_Score(Good, Standard, Poor)
# 학습용 데이터(train)를 이용해 신용 등급을 예측하는 모델을 만든 후 이를 평가용 데이터(test)에 적용해 얻은 예측값을 다음과 같은 형식의 CSV 파일로 생성하시오
    # 제출 파일은 다음 2개의 컬럼을 포함해야한다
        # - pred: 예측값
        # - 제출 파일명: result.csv
    # 제출한 모델의 성능은 f1-macro 평가지표에 따라 채점한다

import pandas as pd

train = pd.read_csv("score_train.csv")
test = pd.read_csv("score_test.csv")

# print(train.head())
# print(test.head())
# print(train.isnull().sum()) # 결측치없음
# print(test.isnull().sum()) # 결측치없음
# print(train.shape, test.shape) # (4198, 21) (1499, 20)
# print(train.info())

X = train.drop("Credit_Score", axis=1)
y = train["Credit_Score"]
# print(X.head())
# print(y.head())

X_full = pd.concat([X, test], axis=0)
# print(X_full.head())
# print(X_full.shape, 4198+1499)

# X_full = X_full.fillna(0) # 결측치 없지만 결측치 제거 연습

from sklearn.preprocessing import LabelEncoder

for col in X_full:
    if X_full[col].dtypes == "object":
        le = LabelEncoder()
        X_full[col] = le.fit_transform(X_full[col])

# print(X_full.info())

X_train = X_full[:train.shape[0]]
X_test = X_full[train.shape[0]:]
# print(X_train.shape, X_test.shape) # (4198, 20) (1499, 20)

from sklearn.model_selection import train_test_split
X_train, X_val, y_train, y_val = train_test_split(X_train, y, test_size=0.2)
# print(X_train.shape, X_val.shape, y_train.shape, y_val.shape) # (3358, 20) (840, 20) (3358,) (840,)

from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
model.fit(X_train, y_train)
y_val_pred = model.predict(X_val)

from sklearn.metrics import f1_score
f1 = f1_score(y_val, y_val_pred, average="macro")

pred = model.predict(X_test)
result = pd.DataFrame(pred, columns=["pred"])
result.to_csv("result.csv", index=False)

test = pd.read_csv("result.csv")
print(test.head())

# print(help(sklearn))
# print(dir(sklearn.metrics))

# LabelEncoder, RandomForestClassifier, train_test_split, f1_score
# ensemble, metrics, model_selection, preprocessing

