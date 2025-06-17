import pandas as pd

train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")

# price
# model  year  price transmission  mileage fuelType  tax   mpg  engineSize
# print(train.head())
# print(test.head())
# print(train.info())
# print(train.shape, test.shape) # (3759, 9) (1617, 8)

X = train.drop("price", axis=1)
y = train["price"]
# print(X.shape, y.shape)

X_full = pd.concat([X, test], axis=0)
# print(X_full.shape) # (5376, 8)
# print(X_full.isnull().sum())

X_full = pd.get_dummies(X_full)
# print(X_full.shape) # (5376, 30)

X_train = X_full[:train.shape[0]]
X_test = X_full[train.shape[0]:]
# print(X_train.shape, X_test.shape) # (3759, 30) (1617, 30)

from sklearn.model_selection import train_test_split
X_train, X_val, y_train, y_val = train_test_split(X_train, y, test_size=0.2)
# print(X_train.shape, X_val.shape, y_train.shape, y_val.shape) # (3007, 30) (752, 30) (3007,) (752,)

from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor()
model.fit(X_train, y_train)
y_val_pred = model.predict(X_val)

from sklearn.metrics import mean_squared_error
# rmse = root_mean_squared_error(y_val, y_val_pred)
mse = mean_squared_error(y_val, y_val_pred)
rmse2 = mse ** 0.5 # ⭐
# print("rmse:", rmse)
# print("rmse2:", rmse2)

pred = model.predict(X_test)
result = pd.DataFrame(pred, columns=["pred"])
result.to_csv("result.csv", index=False)

test = pd.read_csv("result.csv")
print(test.head())

# 38점