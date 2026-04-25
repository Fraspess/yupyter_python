from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# 1
data = fetch_california_housing()
X = data.data[:, data.feature_names.index("MedInc")].reshape(-1, 1)
y = data.target

poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_poly, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)

print("R2 (test):", r2)

# 2
degrees = [1, 2, 3]
results = []

for d in degrees:
    poly = PolynomialFeatures(degree=d)
    X_poly = poly.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(
        X_poly, y, test_size=0.2, random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)

    results.append([
        d,
        r2_score(y_train, y_train_pred),
        r2_score(y_test, y_test_pred)
    ])


print("Ступінь | R2 train | R2 test")
for row in results:
    print(f"{row[0]}       | {row[1]:.4f}   | {row[2]:.4f}")


# 3
from sklearn.linear_model import Lasso

features = ["MedInc", "HouseAge", "AveRooms", "AveBedrms"]
indices = [data.feature_names.index(f) for f in features]

X = data.data[:, indices]
y = data.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

lr = LinearRegression()
lr.fit(X_train, y_train)
lr_r2 = r2_score(y_test, lr.predict(X_test))

lasso = Lasso(alpha=0.1)
lasso.fit(X_train, y_train)
lasso_r2 = r2_score(y_test, lasso.predict(X_test))

zero_coeffs = sum(lasso.coef_ == 0)

print("LinearRegression R2:", lr_r2)
print("Lasso R2:", lasso_r2)
print("Кількість нульових коефіцієнтів у Lasso:", zero_coeffs)


# 4
from sklearn.linear_model import Ridge
import numpy as np

lr = LinearRegression()
lr.fit(X_train, y_train)
lr_r2 = r2_score(y_test, lr.predict(X_test))
lr_nonzero = np.sum(lr.coef_ != 0)

ridge = Ridge(alpha=1.0)
ridge.fit(X_train, y_train)
ridge_r2 = r2_score(y_test, ridge.predict(X_test))
ridge_nonzero = np.sum(ridge.coef_ != 0)

print("Модель               | R2 test | Ненульові коеф.")
print(f"LinearRegression     | {lr_r2:.4f} | {lr_nonzero}")
print(f"Ridge (alpha=1.0)   | {ridge_r2:.4f} | {ridge_nonzero}")



