# 1. 과목에 상관없이 점수가 가장 작은 점수 25개를 찾으시오
# 2. 찾은 점수 25개의 합을 정수로 구하시오

import pandas as pd

df = pd.read_csv("school_data.csv")
df = df.melt(id_vars="이름", value_vars=["수학", "영어", "국어"], value_name="점수", var_name="과목명") # ⭐

filtered = df.sort_values("점수", ascending=True).iloc[:25]
print(int(filtered["점수"].sum())) # 420