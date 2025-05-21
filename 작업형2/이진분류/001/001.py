# 환자의 당뇨병 여부를 예측하시오
    # 예측할 컬럼: Outcome(0: 정상, 1: 당뇨병)
# 학습용 데이터(train)를 이용해 환자의 당뇨병을 예측하는 모델을 만든 후 이를 평가용 데이터(test)에 적용해 얻은 예측값을 다음과 같은 형식의 CSV 파일로 생성하시오
# 제출 파일은 다음 1개의 컬럼을 포함해야한다
# pred: 예측값(당뇨병일 확률)
# 제출파일명: result.csv
# 제출한 모델의 성능은 ROC-AUC 평가지표에 따라 채점한다.

# 1. 데이터 유형 파악
import pandas as pd

train = pd.read_csv("./diabetes_train.csv")
test = pd.read_csv("./diabetes_test.csv")

# print(train.head())
# print(test.head())
# print(train.info())
# print(train.info())
# print(train.shape, test.shape)

# 2. 전처리
# (1) X, y 및 train/test 데이터 set 분리
X = train.drop(["Outcome"], axis=1)
y = train["Outcome"]

# print(x)
# print(y)

X_full = pd.concat([X, test], axis=0)

# (2) 결측치 제거
X_full = X_full.fillna(0)
# print(X_full.isnull().sum())

# (3) 수치형 변수 스케일링: 랜덤포레스트 사용할거니까 skip

# (4) 범주형 변수 인코딩(원-핫 인코딩) → 지금은 데이터에 범주형 변수가 없음
# print(X_full.shape)
# X_full = pd.get_dummies(X_full)
# print(X_full.shape) # 개수가 늘어남

# 3. 데이터 분리
# print(train.shape[0])
# print(X_full.shape)

X_train = X_full[:train.shape[0]]
X_test = X_full[train.shape[0]:]
# print(X_train.shape, X_test.shape)

# (1) 학습데이터와 검증 데이터 분리
# ensemble
import sklearn
from sklearn.model_selection import train_test_split
# print(help(sklearn))
# print(dir(sklearn.model_selection))
X_train, X_val, y_train, y_val = train_test_split(X_train, y, test_size=0.2)
# print(X_train.shape, X_val.shape, y_train.shape, y_val.shape) # (491, 8) (123, 8) (491,) (123,)

# 4. 모델 학습 및 검증
# print(dir(sklearn.ensemble))
from sklearn.ensemble import RandomForestClassifier # 회귀일때: RandomForestRegressor 사용
model = RandomForestClassifier()
model.fit(X_train, y_train)
y_val_pred = model.predict(X_val)


# 5. 평가

# print(help(sklearn))
print(dir(sklearn.metrics))
from sklearn.metrics import roc_auc_score, accuracy_score # 회귀일때: root_mean_squared_error 사용

roc_score = roc_auc_score(y_val, y_val_pred)
acc = accuracy_score(y_val, y_val_pred)

# print(roc_score, acc)

# 6. 결과 저장
y_pred = model.predict(X_test)
result = pd.DataFrame(y_pred, columns=["pred"])
# print(result)
result.to_csv("result.csv", index=False)

# 다중분류일때는?
# LabelEncoder -> A B C D E -> 0 1 2 3 4 5로 바꿔서 학습 및 평가가
# 0 1 2 3 4 5 -> A B C D E (inverser_transform 사용)

# from sklearn.preprocessing import LabelEncoder

# # 인코딩
# le = LabelEncoder()
# y_encoded = le.fit_transform(y)   # ['A', 'B', 'C'] → [0, 1, 2]

# # 모델 학습
# model.fit(X_train, y_encoded)

# # 예측
# y_pred = model.predict(X_test)

# # 다시 문자형 라벨로 변환 (제출할 때 등)
# y_pred_label = le.inverse_transform(y_pred)  # [0, 2, 1] → ['A', 'C', 'B']