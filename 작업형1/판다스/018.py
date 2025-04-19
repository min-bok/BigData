# 18. 시계열데이터(timedelta) : 두 시점 사이의 차이를 나타냄
# datetime 자료형을 빼거나 더하면 결괏값으로 timedelta 자료형이 됨
import pandas as pd

make_df = pd.DataFrame({'Date1': ["17 Feb 2024 13:50:30", "18 Feb 2024 14:55:45"], 'Date2': ["17 May 2024 13:50:30", "18 May 2024 14:55:45"]})
make_df.to_csv("date.csv")

df = pd.read_csv("./date.csv", usecols=["Date1"], parse_dates=["Date1"]) # Date1 컬럼만 가져오고, parse_dates를 사용해 datetime 자료형으로 변환함
# print(df)
#                 Date1
# 0 2024-02-17 13:50:30
# 1 2024-02-18 14:55:45

# 1. 특정 시간과의 차이 -----------------------------
# week, days, hours, minutes, seconds
# 사귄지 100일 구하기
day = pd.Timedelta(days=99) # 사귄날이 1일 이므로 99
df["100day"] = df["Date1"] + day
# print(df)
#                 Date1              100day
# 0 2024-02-17 13:50:30 2024-05-26 13:50:30
# 1 2024-02-18 14:55:45 2024-05-27 14:55:45

# 사귄지 100시간전 구하기
hour = pd.Timedelta(hours=100)
df["-100s"] = df["Date1"] - hour
# print(df) 

# 2. 두 시간 사이의 차이 -----------------------------
diff = df["Date1"] - df["100day"]
diff2 = df["Date1"] - df["-100s"]
# print(diff) # -99 days
# print(diff2) # 4 days 04:00:00

# 전체 시간을 초, 분, 시, 일 단위로 변경
# print(diff.dt.total_seconds()) # 초 -8553600.0
# print(diff.dt.total_seconds()/60) # 분 -142560.0
# print(diff.dt.total_seconds()/60/60) # 시간 -2376.0
# print(diff.dt.total_seconds()/60/60/24) # 일 -99.0

# 3. dt 속성 -----------------------------
# print(diff2.dt.seconds) # 14400 : diff2의 초만 반환
# print(diff2.dt.days) # 4 : diff2의 일수만 반환

# 4. 시간 반올림 -----------------------------
min = 5.41
# print(int(min), "분") # 5 분
# print(0.41*60, "초") # 24.599999999999998 초

print(diff.dt.total_seconds()) # 360000.0
print(round(diff.dt.total_seconds()))
