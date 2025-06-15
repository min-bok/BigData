import pandas as pd

# 예제 데이터프레임
df = pd.DataFrame({
    'height': [150, 160, 170, 180, 190],
    'weight': [50, 60, 70, 80, 90]
})

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()

df = scaler.fit_transform(df)

# print(df)
# # 스케일러 생성
# scaler = MinMaxScaler()

# # fit + transform
# df_scaled = scaler.fit_transform(df)

# # 다시 DataFrame으로 변환
# df_scaled = pd.DataFrame(df_scaled, columns=df.columns)

# print(df_scaled)