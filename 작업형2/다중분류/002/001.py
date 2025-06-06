# 주어진 데이터에서 약물의 종류를 예측하시오
    # 제공된 데이터 목록: drug_train.csv, drug_test.csv
    # 예측할 컬럼: Drug(DrugY, drugX, drugA, drugC, drugB)
# 학습용 데이터(train.csv)를 이용해 약물의 종류를 예측하는 모델을 만든 후 이를 평가용 데이터(test.csv)에 적용해 얻은 예측값을 다음과 같은 형식의 csv 파일로 생성하시오
# 제출 파일은 다음 1개의 컬럼을 포함해야한다
    # pred: 예측값
    # 제출파일명: result.csv
# 제출한 모델의 성능은 f1-macro 평가지표에 따라 채점한다
import pandas as pd

train = pd.read_csv("drug_train.csv")
test = pd.read_csv("drug_test.csv")

# print(train.head())
# print(test.head())
# print(train.shape, test.shape) # (100, 6) (100, 5)
# print(train.info())
# print(test.info())
# print(train.isnull().sum())
# print(test.isnull().sum())

X = train.drop("Drug", axis=1)
y = train["Drug"]
# print(y.head())

X_full = pd.concat([X, test], axis=0)
# print(X_full.head())
# print(X_full.shape) # (200, 5)

# 1. 결측치 제거 (생략)
# print(X_full.isnull().sum()) # 결측치없음
# 2. 스케일링 (생략)
# 3. 인코딩
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

for col in X_full.columns:
    if X_full[col].dtypes == "object":
        X_full[col] = le.fit_transform(X_full[col])

X_train = X_full[:train.shape[0]]
X_test = X_full[train.shape[0]:]
# print(X_train.shape, X_test.shape) # (100, 5) (100, 5)

from sklearn.model_selection import train_test_split
X_train, X_val, y_train, y_val = train_test_split(X_train, y, test_size=0.2)
# print(X_train.shape, X_val.shape, y_train.shape, y_val.shape) # (80, 5) (20, 5) (80,) (20,)

from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
model.fit(X_train, y_train)
y_val_pred = model.predict(X_val)

from sklearn.metrics import f1_score
f1 = f1_score(y_val, y_val_pred, average="macro")
# print(f1) # 1.0

pred = model.predict(X_test)
result = pd.DataFrame(pred, columns=["pred"])
result.to_csv("result.csv", index=False)

# test = pd.read_csv("result.csv")
# print(test.head())

# print(help(sklearn))
# print(dir(sklearn.ensemble))

# ensemble, metrics, model_selection, preprocessing