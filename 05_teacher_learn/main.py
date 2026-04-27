from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn.metrics import mean_absolute_error, r2_score

area = np.array([50, 100, 150, 200, 250]).reshape(-1,1)
price = np.array([100,150,200,300,400])

print("Площі :", area)
print("Ціни :", price)

model = LinearRegression()
model.fit(area, price)

new_area = np.array([[180]])

prediction = model.predict(new_area)

print("Площа : ", new_area[0,0], " м2 -> ", prediction[0])


print("-"*70)
predictions = model.predict(area)
mea = mean_absolute_error(price, predictions)

rmse = np.sqrt(mea)

r2 = r2_score(price, predictions)

print(f"MAE: {mea:.2f} середня помилка")
print(f"RMSE: {rmse:.2f} коренева квадратична помилка")
print(f"r2 score: {r2:.2f} якість моделі")

print("+++"*20)

X = np.array([
    [50,2,30],
    [100,3,20],
    [150,4,10],
    [200,5,5],
    [250,6,0],
])

Y = np.array([100,150,200,300,400])

model_multi = LinearRegression()
model_multi.fit(X,Y)

new_house = np.array([[120,3,15]])
price_pred = model_multi.predict(new_house)

print(price_pred)
