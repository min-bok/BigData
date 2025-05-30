# 1. 각 결제 종류별로 실제 도착 시간이 예상 도착 시간보다 늦은 주문의 비율을 계산하시오
# 2. 비율 중 가장 큰 값을 반올림하여 소수 둘째 자리까지 구하시오

import pandas as pd

df = pd.read_csv("./delivery_time.csv")