# 1. 점심시간(10시부터 13시 전까지)에 주문된 배달 데이터를 찾으시오
# 2. 점심시간 주문 건 중 과속(평균 속도가 50km/h 이상)하는 주문 수를 정수로 구하시오
# 배달시간 = 실제도착시간 - 주문시간
# 속도(km/h) = 거리/시간(h)

import pandas as pd

df = pd.read_csv("delivery_time.csv")
