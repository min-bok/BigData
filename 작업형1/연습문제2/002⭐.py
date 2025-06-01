# 1. subscribed 컬럼에서 가장 빈도수가 많은 날짜를 구하시오
# 2. 앞에서 구한 날짜의 일(day)값을 정수로 구하시오
import pandas as pd

df = pd.read_csv("type1_data1.csv")
# print(df.head())

mode = df["subscribed"].mode()[0]
# print(df["subscribed"].value_counts())

print(mode.split("-")[-1]) # 17
# print(mode.dt.days)