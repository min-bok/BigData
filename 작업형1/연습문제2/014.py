# 1. 중복 데이터를 제거하시오
# 2. f3 컬럼의 결측치는 0 "silver"는 1 "gold"는 2 "vip"는 3으로 변환하시오
# 3. 변환된 f3 컬럼의 총합을 정수형으로 구하시오

import pandas as pd

df = pd.read_csv("./type1_data1.csv")