# 1. school_data.csv와 school_data_science.csv의 학생 순서는 동일하다
# 2. 학생별로 수학, 영어, 국어, 과학 점수의 평균을 구하시오
# 3. 평균 점수가 60점 이상인 인원 수를 계산하시오

import pandas as pd

df = pd.read_csv("school_data.csv")
df_science = pd.read_csv("school_data_science.csv")

# 9