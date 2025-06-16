import pandas as pd

# Heat_Load
train = pd.read_csv("energy_train.csv")
test = pd.read_csv("energy_test.csv")

# print(train.head())
# print(test.head())
# print(train.shape, test.shape) # (537, 10) (231, 9)
# print(train.info())

X = train.drop(["Heat_Load"], axis=1)
y= train["Heat_Load"]

X_full = pd.concat([X, test], axis=0)

X_full = pd.get_dummies(X_full)
# print(X_full.shape)

X_train = X_full[:train.shape[0]]
X_test = X_full[train.shape[0]:]
# print(X_train.shape, X_test.shape) # (537, 16) (231, 16)

from sklearn.model_selection import train_test_split
X_train, X_val, y_train, y_val = train_test_split(X_train, y, test_size=0.2)
# print(X_train.shape, X_val.shape, y_train.shape, y_val.shape) # (429, 16) (108, 16) (429,) (108,)

from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
model.fit(X_train, y_train)
y_val_pred = model.predict(X_val)

from sklearn.metrics import f1_score
score = f1_score(y_val, y_val_pred, average="macro")

pred = model.predict(X_test)
result = pd.DataFrame(pred, columns=["pred"])
result.to_csv("result.csv", index=False)

test = pd.read_csv("result.csv")
print(test.head())

# model_selection, ensemble, metrics
# train_test_split, RandomForestClassifier, f1_score

# 40점