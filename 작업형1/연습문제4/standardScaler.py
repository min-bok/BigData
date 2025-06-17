# 기출 제7회
# 결측치가 있는 행을 제거한 후 학생이 가장 많이 수강한 과목을 찾고, 
# 해당 과목 점수를 표준화(스탠더드 스케일)한 다음 가장 큰 표준화된 값을 구하시오 (반올림하여 소수 셋째자리까지 계산)
import pandas as pd

df = pd.read_csv("student_assessment.csv")
# 2.183
