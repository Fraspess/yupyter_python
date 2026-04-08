import numpy as np

# myarray = np.array([23,3,45,2,5,6,])
# print(myarray)

# myarray2 = np.array([[1,2,3],[6,9,7]])
# print(myarray2)

# zeros = np.zeros((3,3))
# print(zeros)

# ones = np.ones((3,3))
# print(ones)

# arr = np.arange(0,10,2)
# print(arr)

# arr = np.linspace(0,1,8)
# print(arr)

# myArray = np.array([[2,3,6], [4,6,6]])
# print(myArray)
# print(myArray.shape)
# print(myArray.ndim)
# print(myArray.dtype)
# print(myArray.size)

# myList = np.array([23,46,26,16,29,54,21])
# print(myList[0])
# print(myList[1:4])
# print(myList[:3])

# my2D = np.array([[3,4,6],[1,2,5],[8,8,8]])
# print(my2D[1:,:2])

# a = np.array([2,3,5,7,8])
# b = np.array([2,3,5,7,8])
# print("a:", a)
# print("b:", b)
#
# print("a + b:", a + b)
# print("a - b:", a - b)
# print("a * b:", a * b)
# print("a / b:", a / b)
# print("a // b:", a // b)
# print("a % b:", a % b)
# print("a ** b:", a ** b)
# print("a == b:", a == b)
# print("a != b:", a != b)

# data = np.array([2,3,4,5,6,7,8])
# print(data)


# практична
import random
# 1
#
# arr = np.array([random.randint(1, 100 + 1) for _ in range(10)])
# print(arr)
# print("Max:", np.max(arr))
# print("Min:", np.min(arr))
# sortArr = np.sort(arr)
# print("Original:",arr)
# print("Sorted:",sortArr)

# 2
# arr = np.array([[random.randint(1, 50 + 1) for _ in range(4)],
#                 [random.randint(1, 50 + 1) for _ in range(4)],
#                 [random.randint(1, 50 + 1) for _ in range(4)],
#                 [random.randint(1, 50 + 1) for _ in range(4)]])
# print(arr)
# print("Сума по колонкам:", np.sum(arr, axis = 0))
# print("Сума по рядкам:", np.sum(arr, axis = 1))
# print("Середнє значення:", np.mean(arr))

# 3
# arr = np.arange(15).reshape(3, 5)
# print(arr)
# print(arr.reshape(5,3))

# 4
array = np.random.rand(10, 10)

print(array)


