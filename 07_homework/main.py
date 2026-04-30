import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# 1
diabetes = datasets.load_diabetes()

X = diabetes.data[:, np.newaxis, 2]
y = diabetes.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Реальні vs Передбачені:")
for real, pred in list(zip(y_test, y_pred))[:10]:
    print(f"{real:.2f}  |  {pred:.2f}")


# 2
import matplotlib.pyplot as plt

plt.scatter(X_test, y_test, label="Реальні значення")
plt.plot(X_test, y_pred, linewidth=2, label="Лінія регресії")

plt.xlabel("BMI")
plt.ylabel("Ціль (Disease progression)")
plt.title("Лінійна регресія (1 ознака)")
plt.legend()

plt.show()


# 3
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nМетрики якості:")
print(f"{'Метрика':<10} | Значення")
print("-" * 25)
print(f"MAE       | {mae:.4f}")
print(f"MSE       | {mse:.4f}")
print(f"R²        | {r2:.4f}")


# 4
X_train_gd = X_train.flatten()
X_test_gd = X_test.flatten()

w = 0.0
b = 0.0

lr = 0.1
epochs = 1000
n = len(X_train_gd)

for _ in range(epochs):
    y_pred_gd = w * X_train_gd + b

    dw = (-2 / n) * np.sum(X_train_gd * (y_train - y_pred_gd))
    db = (-2 / n) * np.sum(y_train - y_pred_gd)

    w -= lr * dw
    b -= lr * db

y_pred_gd_test = w * X_test_gd + b

mae_gd = mean_absolute_error(y_test, y_pred_gd_test)
mae_sklearn = mean_absolute_error(y_test, y_pred)

print("\nПорівняння MAE:")
print(f"Gradient Descent MAE: {mae_gd:.4f}")
print(f"LinearRegression MAE: {mae_sklearn:.4f}")

print("\nКоефіцієнти GD:")
print(f"w = {w:.4f}, b = {b:.4f}")

print("\nКоефіцієнти sklearn:")
print(f"w = {model.coef_[0]:.4f}, b = {model.intercept_:.4f}")