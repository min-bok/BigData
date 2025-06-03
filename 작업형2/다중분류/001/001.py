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
# print(train.info())
# print(test.info())
# print(train.shape, test.shape) # (4198, 21) (1499, 20)
# print(train.isnull().sum())
# print(test.isnull().sum())

# 1. 데이터 전처리
X = train.drop(["Credit_Score"], axis=1)
y = train["Credit_Score"]
# print(X.shape, y.shape) # (4198, 20) (4198,)

X_full = pd.concat([X, test], axis=0)
# print(X_full.shape, 4198+1499) # (5697, 20) 5697

# 1.1 결측치 제거(결측치 없어서 생략)
# 1.2 스케일링(랜덤포레스트 사용할거라 생략)
# 1.3 인코딩(다중분류라서 label 인코딩 사용)
from sklearn.preprocessing import LabelEncoder

for col in X_full.columns:
    if X_full[col].dtypes == "object":
        # print(col)
        le = LabelEncoder()
        X_full[col] = le.fit_transform(X_full[col])

# print(X_full["Credit_Mix"].head())

X_train = X_full[:train.shape[0]]
X_test = X_full[train.shape[0]:]

# print(X_train.shape, X_test.shape)

# 2. 학습/테스트 데이터 분리
from sklearn.model_selection import train_test_split
X_train, X_val, y_train, y_val = train_test_split(X_train, y, test_size=0.2)
# print(X_train.shape, X_val.shape, y_train.shape, y_val.shape) # (3358, 20) (840, 20) (3358,) (840,)

# 3. 모델 학습 및 평가
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier()
model.fit(X_train, y_train)
y_val_pred = model.predict(X_val)

from sklearn.metrics import f1_score

f1 = f1_score(y_val, y_val_pred, average="macro")
# print(f1) # 0.6883902505350491

# 4. 파일 작성 및 제출
pred = model.predict(X_test)
result = pd.DataFrame(pred, columns=["pred"])
result.to_csv("result.csv", index=False)

test = pd.read_csv("result.csv")
print(test.head())

# print(help(f1_score))

# print(help(sklearn))
# print(dir(sklearn.metrics))

# ensemble
# model_selection
# metrics
