import matplotlib.pyplot as plt
import random
# 1
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
plan = [100, 120, 140, 130, 150, 160]
fact = [90, 110, 135, 120, 145, 170]

plt.plot(months, plan, label="План", marker='o')
plt.plot(months, fact, label="Факт", marker='o')

plt.xlabel("Місяці")
plt.ylabel("Продажі")
plt.title("План vs Факт продажів")
plt.legend()

plt.show()

# 2
ages = [random.randint(18, 60) for _ in range(100)]

plt.hist(ages, bins=10)

avg_age = sum(ages) / len(ages)
plt.axvline(avg_age, linestyle='dashed', linewidth=2)

plt.xlabel("Вік")
plt.ylabel("Кількість людей")
plt.title("Розподіл віку")

plt.show()


# 3
group1 = [random.randint(60, 100) for _ in range(20)]
group2 = [random.randint(50, 95) for _ in range(20)]
group3 = [random.randint(70, 100) for _ in range(20)]

plt.boxplot([group1, group2, group3])
plt.xticks([1, 2, 3], ["Група 1", "Група 2", "Група 3"])

plt.ylabel("Оцінки")
plt.title("Порівняння оцінок студентів")

plt.show()


# 4
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
temp = [20, 22, 19, 23, 25, 24, 21]
humidity = [60, 55, 70, 65, 50, 45, 60]

plt.plot(days, temp, label="Температура")
plt.plot(days, humidity, label="Вологість")

plt.xlabel("Дні")
plt.ylabel("Значення")
plt.title("Температура та вологість за тиждень")
plt.legend()

plt.xticks(rotation=45)

plt.show()


# 5
hours = list(range(24))
load = [30, 20, 15, 10, 10, 15, 25, 50, 70, 80, 90, 85,
        80, 75, 70, 65, 60, 70, 85, 95, 90, 70, 50, 40]

plt.plot(hours, load)
plt.fill_between(hours, load, alpha=0.3)

plt.xlabel("Години")
plt.ylabel("Навантаження (%)")
plt.title("Навантаження сервера за добу")
plt.grid()

plt.show()

# 6
time = list(range(10))

conversion = [2, 3, 4, 3, 5, 6, 5, 6, 7, 8]
retention = [50, 52, 53, 55, 54, 56, 58, 60, 62, 65]
avg_check = [20, 22, 21, 23, 25, 27, 26, 28, 30, 32]
orders = [100, 120, 110, 130, 150, 170, 160, 180, 200, 220]

fig, axs = plt.subplots(2, 2)

axs[0, 0].plot(time, conversion)
axs[0, 0].set_title("Конверсія")

axs[0, 1].plot(time, retention)
axs[0, 1].set_title("Утримання")

axs[1, 0].plot(time, avg_check)
axs[1, 0].set_title("Середній чек")

axs[1, 1].plot(time, orders)
axs[1, 1].set_title("Кількість замовлень")

fig.suptitle("Метрики продукту")

plt.tight_layout()
plt.show()