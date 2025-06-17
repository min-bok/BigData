# 기출 제7회
# DE1 ~ DE77 컬럼 중 주가지수의 종가 "close"와 가장 상관 관계가 높은 변수를 찾아 
# 해당 변수의 평균값을 구하시오 (반올림하여 소수 넷째자리까지 계산)
import pandas as pd

df = pd.read_csv("stock_market.csv")
# print(df.sample(5))

corrmax = abs(df.corr()["close"]).loc["DE1":"DE77"].idxmax() # ⭐abs, 양의 상관관계든, 음의 상관관계든 관계의 세기(강도)가 중요
m = df[corrmax].mean()

print(round(m, 4)) # -0.0004
