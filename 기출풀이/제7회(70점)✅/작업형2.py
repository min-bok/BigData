import pandas as pd

# total
train = pd.read_csv("mart_train.csv")
test = pd.read_csv("mart_test.csv")

# print(train.head())
# print(test.head())
# print(train.shape, test.shape) # (700, 10) (300, 9)
# print(train.info())
# print(test.info())

X = train.drop("total", axis=1)
y = train["total"]

X_full = pd.concat([X, test], axis=0)
# print(X_full.shape)
# print(X_full.isnull().sum())

X_full = X_full.fillna(0)
X_full = pd.get_dummies(X_full)
# print(X_full.shape)

X_train = X_full[:train.shape[0]]
X_test = X_full[train.shape[0]:]
# print(X_train.shape, X_test.shape) # (700, 30) (300, 30)

from sklearn.model_selection import train_test_split
X_train, X_val, y_train, y_val = train_test_split(X_train, y, test_size=0.2)
# print(X_train.shape, X_val.shape, y_train.shape, y_val.shape) # (560, 30) (140, 30) (560,) (140,)

from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor()
model.fit(X_train, y_train)
y_val_pred = model.predict(X_val)

from sklearn.metrics import root_mean_squared_error
rmse = root_mean_squared_error(y_val, y_val_pred)
# print(rmse)

pred = model.predict(X_test)
result = pd.DataFrame(pred, columns=["pred"])
result.to_csv("result.csv", index=False)

test = pd.read_csv("result.csv")
print(test.head())

# 36~38점 예상 ✅