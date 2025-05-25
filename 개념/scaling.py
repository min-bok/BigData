# 스케일링은 수치형 데이터의 범위를 조정하는 작업, 트리 기반 모델에서는 큰 개선 효과를 보기 어려움
import pandas as pd

train = pd.read_csv("train.csv")
# print(df.head())

cols = train.select_dtypes(include="number").columns.tolist()
# print(cols)

# (1) 민맥스 스케일링 : 데이터를 0과 1 사이로 변환
# print(train.head())
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
train[cols] = scaler.fit_transform(train[cols])

# print(train.head())