import numpy as np
import random
# 1
# array = np.array([random.randint(0,50) for _ in range(20)])
# print(array)
# num = int(input("Введіть число: "))
# print("Кількість елементів більше за введене число" , len(array[array > num]))
# print("Позиція максимального числа: ", np.argmax(array))
# print("Максимальне число: ", np.max(array))
# print("За спаданням:", np.sort(array)[::-1])

# 2
# start = int(input("Введіть перше число:"))
# end = int(input("Введіть друге число:"))
# matrix = np.random.randint(start,end + 1, size=(5,5))
# print(matrix)
# print("Діагональ:", np.diag(matrix))
# print("Сума діагоналі:", np.sum(np.diag(matrix)))
# for i in range(5):
#     for j in range(5):
#         if j > i:
#             matrix[i][j] = 0
# print("Нулі вище діагоналі:",matrix)


# 3
# start = int(input("Введіть перше число:"))
# end = int(input("Введіть друге число:"))
# sequence = np.arange(start, end+1)
#
# matrix = sequence[:30].reshape(6,5)
# print("Матриця")
# print(matrix)
#
# print("Сума рядків:", np.sum(matrix,axis=1))
# print("Максимальне стовпчиків:", matrix.max(axis=0))


# 4
# start = int(input("Введіть перше число:"))
# end = int(input("Введіть друге число:"))
# array = np.random.randint(start,end+1, size=15)
# print(array)
# print(array[array < 0])
#
# copyArr = np.copy(array)
# copyArr[array < 0] = 0
# print(copyArr)
# print("Нулів:", np.sum(copyArr == 0))


# 5
# length = int(input("Введіть довжину масивів: "))
# arr1 = np.random.randint(1,10+1, size = length)
# arr2 = np.random.randint(10,20+1, size = length)
# print(arr1)
# print(arr2)
# print("Об'єднані масиви", np.concatenate((arr1,arr2)))
#
# print("Додавання :", arr1 + arr2)
# print("Віднімання", arr1 - arr2)



# 6
rows = int(input("Введіть кількість рядків матриці: "))
cols = int(input("Введіть кількість стовпців матриці: "))

size = rows * cols
matrix = np.arange(1, size + 1).reshape(rows, cols)
print(matrix)

new_rows = int(input("Введіть нову кількість рядків: "))
new_cols = int(input("Введіть нову кількість стовпців: "))

new_size = new_rows * new_cols

if new_size != size:
    print("ноу ноу ноу")
else:
    new_matrix = matrix.reshape(new_rows, new_cols)
    print("Нова матриця:")
    print(new_matrix)

    row_mins = new_matrix.min(axis=1)
    row_maxs = new_matrix.max(axis=1)

    print("Мінімальні значення в рядках:")
    print(row_mins)

    print("Максимальні значення в рядках:")
    print(row_maxs)

    print("Сума:", new_matrix.sum())




