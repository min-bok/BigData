# 1. views 컬럼의 1사분위수, 3사분위수, 그리고 IOR을 계산하시오
# 2. 이상치 조건에 맞는 데이터를 찾으시오. (이상치는 1사분위수 - (IQR * 1.5)보다 작은 값과 3사분위수 + (IQR * 1.5)보다 큰 값)
# 3. 이상치 데이터의 views 컬럼 합을 정수로 구하시오

import pandas as pd

df = pd.read_csv("./type1_data1.csv")