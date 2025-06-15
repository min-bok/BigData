# 1. subscribed 컬럼에서 가장 빈도수가 많은 날짜를 구하시오
# 2. 앞에서 구한 날짜의 일(day)값을 정수로 구하시오
import pandas as pd

df = pd.read_csv("type1_data1.csv")

print(int(df["subscribed"].value_counts().idxmax().split("-")[-1])) # 17
# print(pd.to_datetime(df["subscribed"].value_counts().idxmax()).day)