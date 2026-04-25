from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score
from xgboost import XGBRegressor
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
from sklearn.ensemble import RandomForestRegressor

# 1
data = fetch_california_housing()

features = ["MedInc", "HouseAge", "AveRooms", "AveBedrms"]
idx = [data.feature_names.index(f) for f in features]

X = data.data[:, idx]
y = data.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = DecisionTreeRegressor(max_depth=4, random_state=42)
model.fit(X_train, y_train)

r2 = r2_score(y_test, model.predict(X_test))
print("R2:", r2)

# 2
tree = DecisionTreeRegressor(max_depth=4, random_state=42)
tree.fit(X_train, y_train)
tree_r2 = r2_score(y_test, tree.predict(X_test))

forest = RandomForestRegressor(n_estimators=100, random_state=42)
forest.fit(X_train, y_train)
forest_r2 = r2_score(y_test, forest.predict(X_test))

print("Модель              | R2")
print(f"Decision Tree       | {tree_r2:.4f}")
print(f"Random Forest       | {forest_r2:.4f}")


# 3
xgb = XGBRegressor(
    n_estimators=200,
    learning_rate=0.1,
    max_depth=5,
    random_state=42
)

xgb.fit(X_train, y_train)
xgb_r2 = r2_score(y_test, xgb.predict(X_test))

print("XGBoost R2:", xgb_r2)

# 4
median_price = np.median(y)
y_class = (y > median_price).astype(int)

X_train, X_test, y_train, y_test = train_test_split(
    X, y_class, test_size=0.2, random_state=42
)

clf = LogisticRegression(max_iter=1000)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall:", recall_score(y_test, y_pred))
print("F1:", f1_score(y_test, y_pred))


