# 17. 시계열 데이터(datetime) : 특정 시점의 날짜와 시간을 나타냄
import pandas as pd

df = pd.DataFrame({"Date1": ["2024-02-17"], "Date2": ["24/02/17"], "Date3": ["02/17/2024 01:50:30 PM"]})
#         Date1     Date2                   Date3
# 0  2024-02-17  24/02/17  02/17/2024 01:50:30 PM

# print(df)

df["Date1"] = pd.to_datetime(df["Date1"])
df["Date2"] = pd.to_datetime(df["Date2"], format="%y/%m/%d")
df["Date3"] = pd.to_datetime(df["Date3"], format="%m/%d/%Y %I:%M:%S %p")
# print(df)

# 2. 날짜와 시간 데이터 분할 ---------------------
# print(df.info())
# datetime 자료형에서만 사용가능

df["year"] = df["Date3"].dt.year

# print(df)

# 3. 요일 찾기 ---------------------
# 0: 월요일 ~ 6: 일요일
# print(df["Date3"].dt.dayofweek) # 5 (즉, 토요일)

# 4. 특정 시점과 특정 구간 (심화) ---------------------
# Y: 연도, Q: 분기, M: 월, D: 일, H: 시간

print(df["Date3"].dt.to_period("Y"))
print(df["Date3"].dt.to_period("Q"))
print(df["Date3"].dt.to_period("D"))
print(df["Date3"].dt.to_period("H"))

