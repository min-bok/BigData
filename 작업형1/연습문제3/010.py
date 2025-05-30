# 1. 결측치가 있는 행을 삭제하시오
# 2. 결측치가 삭제된 제이터를 사용하여 지역별(city) 평균을 계산하시오
# 3. 앞에서 계산한 지역별 평균 데이터에서 f2 컬럼 값이 가장 큰 지역을 구하시오
import pandas as pd

df = pd.read_csv("./type1_data1.csv")
