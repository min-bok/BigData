# 예측할컬럼: TotalCharges
import pandas as pd

train = pd.read_csv("churn_train.csv")
test = pd.read_csv("churn_test.csv")

# print(train.shape, test.shape) # (4116, 19) (1764, 18)

X = train.drop("TotalCharges", axis=1)
y = train["TotalCharges"]
# print(X.shape, y.shape) # (4116, 18) (4116,)

X_full = pd.concat([X, test], axis=0)
# print(X_full.shape)
# print(X_full.isnull().sum())

from sklearn.preprocessing import LabelEncoder

for col in X_full:
    if X_full[col].dtypes == "object":
        le = LabelEncoder()
        X_full[col] = le.fit_transform(X_full[col])

X_train = X_full[:train.shape[0]]
X_test = X_full[train.shape[0]:]

from sklearn.model_selection import train_test_split
X_train, X_val, y_train, y_val = train_test_split(X_train, y, test_size=0.2)
print(X_train.shape, X_val.shape, y_train.shape, y_val.shape) # (3292, 18) (824, 18) (3292,) (824,)

from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor()
model.fit(X_train, y_train)
y_val_pred = model.predict(X_val)

from sklearn.metrics import mean_absolute_error
mae = mean_absolute_error(y_val, y_val_pred)
# print(mae) # 918.213502791262

pred = model.predict(X_test)
result = pd.DataFrame(pred, columns=["pred"])
result.to_csv("result.csv", index=False)

# test = pd.read_csv("result.csv")
# print(test.head())