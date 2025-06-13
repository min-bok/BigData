# 1. 주문이 가장 많이 발생한 연-월을 찾으시오
# 2. 해당 연-월에 '배고팡'앱을 통한 주문 중 '앱결제'로 결제된 주문의 비율을 계산하시오(반올림 후 소수 둘째자리까지 계산)

import pandas as pd

df = pd.read_csv("delivery_time.csv")

# 0.31