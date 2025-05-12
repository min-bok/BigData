# ------ 머신러닝 실습(분류) ---------------------
import pandas as pd

train = pd.read_csv("./train.csv")
test = pd.read_csv("./test.csv")

# 1. --- 탐색적 데이터 분석 ------------
# print(train.head())
# print(test.head())

# print(train.shape, test.shape) # 데이터 크기 확인

# print(train.info()) # 데이터 형식 확인 (object형은 반드시 수치형으로 변경 필요)
# print(test.info())

# print(train.describe()) # 수치형 데이터의 기초 통계값 확인
# print(test.describe())

# print(train.describe(include="object")) # 범주주형 데이터의 기초 통계값 확인
# print(test.describe(include="object"))

# print(train.isnull().sum()) # 결측치 확인
# print(test.isnull().sum())

# print(train["income"].value_counts()) # target의 빈도 확인(1. 이진 분류인지 2. 불균형 데이터인지)
# <=50K    22263
# >50K      7041

# 2. --- 데이터 전처리 ------------
# 2-1. 결측치가 있다면 채우거나 삭제 (삭제 후 모델 성능 확인하고 채우기 추천, 범주형은 최빈값/수치형은 평균이나 중앙값)
# train = train.dropna() # 삭제
# test = test.dropna()

train["workclass"] = train["workclass"].fillna(train["workclass"].mode()[0]) # 범주형
train["occupation"] = train["occupation"].fillna(train["occupation"].mode()[0]) # 범주형
train["native.country"] = train["native.country"].fillna(train["native.country"].mode()[0]) # 범주형
train["age"] = train["age"].fillna(train["age"].mean()) # 수치형
train["hours.per.week"] = train["hours.per.week"].fillna(train["hours.per.week"].mean()) # 수치형

test["workclass"] = test["workclass"].fillna(test["workclass"].mode()[0]) # 범주형
test["occupation"] = test["occupation"].fillna(test["occupation"].mode()[0]) # 범주형
test["native.country"] = test["native.country"].fillna(test["native.country"].mode()[0]) # 범주형
test["age"] = test["age"].fillna(test["age"].mean()) # 수치형
test["hours.per.week"] = test["hours.per.week"].fillna(test["hours.per.week"].mean()) # 수치형
# print(train.isnull().sum()) # 결측치 확인
# print(test.isnull().sum())

# 2-2-1. 중복값 제거
# 2-2-2. 이상치 제거 (문제에서 명시한 경우에만)
# print(train.describe()) # age의 최소값이 음수임
# print(train[train["age"]<=0]) # 이상치 3개 존재
# print(test[test["age"]<=0]) # 없음

# print(train.shape) # (29304, 16)
train = train[train["age"]>0]
# print(train.shape) # (29301, 16), 이상치 처리 후 데이터 크기 변경됨

# 2-3. 모든 데이터를 숫자 형태로 변경(인코딩)
y_train = train.pop("income") # target(label)이 범주형이므로 인코딩,스케일링 방지를 위해 변수에 담아둠

# 2-3-1. 원-핫 인코딩 (일단 이것만 알고 넘어가자)
# train_oh = pd.get_dummies(train)
# test_oh = pd.get_dummies(test)
# print(train.shape, test.shape, train_oh.shape, test_oh.shape) # (29301, 15) (3257, 15) (29301, 106) (3257, 102)

# train과 test의 컬럼갯수가 다르면 사용불가 → 데이터를 합쳐서 인코딩 필요
# print(train.shape, test.shape) # (29301, 15) (3257, 15)
data = pd.concat([train, test], axis=0) # 위아래로 합침
data_oh = pd.get_dummies(data)
train_oh = data_oh.iloc[:len(train)].copy()
test_oh = data_oh.iloc[len(train):].copy()
# print(train_oh.shape, test_oh.shape) # (29301, 106) (3257, 106)

# 2-3-2. 레이블 인코딩

# 데이터 스케일링: 수치형 데이터의 범위 조정 (시간적 여유가 있다면하기 필수는 아님)

# 3. --- 검증 데이터 나누기: 모델의 성능평가 및 개선 ------------
from sklearn.model_selection import train_test_split

X_train, X_val, y_train, y_val = train_test_split(train_oh, y_train, test_size=0.2, random_state=0)

# print(X_train.shape, X_val.shape, y_train.shape, y_val.shape) # (23440, 15) (5861, 15) (23440,) (5861,) / 앞두개 컬럼 수 일치, 뒤두개 컬럼에 1없는 시리즈 형태여야함

# 4. --- 머신러닝 학습 및 평가 ------------
# 랜덤포레스트
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(random_state=0) # 모델선택
rf.fit(X_train, y_train) # 학습진행

# print(rf.classes_) # 컬럼순서확인, ['<=50K' '>50K']
# print(pred[:10])

# 평가지표: 제대로 학습이 되었고 예측을 하고있는지 검증데이터로 평가 필요
# 1. ROC_AUC : 1에 가까울수록 좋음
from sklearn.metrics import roc_auc_score
pred = rf.predict_proba(X_val)
roc_auc = roc_auc_score(y_val, pred[:,1])
print("roc_auc:", roc_auc) # roc_auc: 0.915069936847391

# 2. 정확도(Accuracy) : 1에 가까울수록 좋음
# pred = rf.predict(X_val)
# print(pred[:10])
# from sklearn.metrics import accuracy_score
# pred = rf.predict(X_val)
# accuracy = accuracy_score(y_val, pred)
# print("accuracy:", accuracy) # 0.8677700051185805

# 3. F1 스코어
# from sklearn.metrics import f1_score
# pred = rf.predict(X_val)
# f1 = f1_score(y_val, pred, pos_label=">50K")
# print("f1:", f1) # 0.6920937624155741

# 5. --- 예측 및 결과 파일 생성 ------------
pred = rf.predict_proba(test_oh)
# print(pred)
submit = pd.DataFrame({"pred":pred[:,1]})
submit.to_csv("result.csv", index=False)
