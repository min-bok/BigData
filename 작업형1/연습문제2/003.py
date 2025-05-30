# 1. 결측치가 있는 데이터(행) 삭제
# 2. views 컬럼을 f1컬럼으로 나눈 값을 새로운 컬럼으로 추가
# 3. 새로운 컬럼 값 중 가장 큰 값을 가진 행의 age를 정수로 구하기

import pandas as pd

df = pd.read_csv("type1_data1.csv")


