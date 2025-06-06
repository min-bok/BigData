# 1. school_data.csv와 school_data_social.csv 파일을 이름 기준으로 합치시오
# 2. 영어교사가 장선생이면서 사회교사가 오선생인 학생들을 필터링하시오
# 3. 필터링된 학생들의 수학 점수를 모두 더한 후 정수로 구하시오

import pandas as pd

df = pd.read_csv("school_data.csv")
df_social = pd.read_csv("school_data_social.csv")

new = df.merge(df_social, on="이름") # ⭐on

cond1 = new["영어교사"] == "장선생"
cond2 = new["사회교사"] == "오선생"

new = new[cond1 & cond2]

print(int(new["수학"].sum())) # 602

# print(new.shape) # (30, 9)
# print(help(df.merge))
