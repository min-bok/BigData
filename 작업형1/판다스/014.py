# 14. 문자열
import pandas as pd

df = pd.DataFrame({"A": ["데이터 분석", "기본 학습서", "퇴근 후 열공"], 
                   "B": [10, 20, 30],
                   "C": ["ab cd", "AB CD", "ab cd"]
                   })
# print(df)

# 1. 문자열 변경(치환) ---------------------------------
df["A"] = df["A"].replace("분석", "시각화") # 변경할 수 없음
# print(df)
#            A   B      C
# 0     데이터 분석  10  ab cd
# 1   [기본 학습서]  20  AB CD
# 2  [퇴근 후 열공]  30  ab cd

df["A"] = df["A"].str.replace("분석", "시각화") # 문자열에만 사용가능
# print(df)
#          A   B      C
# 0  데이터 시각화  10  ab cd
# 1   기본 학습서  20  AB CD
# 2  퇴근 후 열공  30  ab cd

df["B"] = df["B"].replace(10, 100)
# print(df)
#          A    B      C
# 0  데이터 시각화  100  ab cd
# 1   기본 학습서   20  AB CD
# 2  퇴근 후 열공   30  ab cd

# df["B"] = df["B"].str.replace(20, 200)
# print(df) # Error

# 2. 문자열 분리 ---------------------------------
# print(df["A"].str.split())
# 0     [데이터, 시각화]
# 1      [기본, 학습서]
# 2    [퇴근, 후, 열공]

# print(df["A"].str.split()[0]) # ['데이터', '시각화']

df["D"] = df["A"].str.split().str[0]

# print(df["A"].str.split().str[0])
# 0    데이터
# 1     기본
# 2     퇴근

# print(df)
#          A    B      C    D
# 0  데이터 시각화  100  ab cd  데이터
# 1   기본 학습서   20  AB CD   기본
# 2  퇴근 후 열공   30  ab cd   퇴근

# 3. 특정 문자열 검색 ---------------------------------
# print(df["A"].str.contains("기본"))
# 0    False
# 1     True
# 2    False

df["기본포함유무"] = df["A"].str.contains("기본")
# print(df)
#          A    B      C    D  기본포함유무
# 0  데이터 시각화  100  ab cd  데이터   False
# 1   기본 학습서   20  AB CD   기본    True
# 2  퇴근 후 열공   30  ab cd   퇴근   False

# 4. 문자열 길이 ---------------------------------
df["문자길이"] = df["A"].str.len()
# print(df)
#          A    B      C    D  기본포함유무  문자길이
# 0  데이터 시각화  100  ab cd  데이터   False     7 # 띄어쓰기도 문자로 포함
# 1   기본 학습서   20  AB CD   기본    True     6
# 2  퇴근 후 열공   30  ab cd   퇴근   False     7

# 5. 문자열 대소문자 변경 ---------------------------------
# print("AB cd" == "ac CD") # False, 파이썬은 대소문자 구분함
# df["C"] = df["C"].str.lower() # 소문자로 변경
# print(df["C"])
# 0    ab cd
# 1    ab cd
# 2    ab cd
# Name: C, dtype: object

# df["C"] = df["C"].str.upper() # 대문자로 변경
# print(df["C"])
# 0    AB CD
# 1    AB CD
# 2    AB CD
# Name: C, dtype: object

# 5.1. 공백제거 ---------------------------------
df["C"] = df["C"].str.lower().str.replace(" ",  "")
# print(df["C"])
# 0    abcd
# 1    abcd
# 2    abcd
# Name: C, dtype: object

# 6. 문자열 인덱싱 ---------------------------------
# print(df["C"].str[1:3]) # 문자열 인덱싱
# 0    bc
# 1    bc
# 2    bc

print(df["C"][1:3]) # 행 인덱싱
# 1    abcd
# 2    abcd
