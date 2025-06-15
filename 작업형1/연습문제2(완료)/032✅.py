# 1. 수학, 영어, 국어 점수의 합을 구하시오
# 2. 합이 가장 큰 상위 10명을 찾으시오
# 3. 찾은 10명의 수학 평균 점수를 구하시오(반올림 후 정수 출력)

import pandas as pd

df = pd.read_csv("school_data.csv")
df["과목합계"] = df["수학"] + df["영어"] + df["국어"]
df = df.sort_values("과목합계", ascending=False)

top10 = df.iloc[:10]["수학"].sum()
print(int(round(top10 / 10, 0))) # 82