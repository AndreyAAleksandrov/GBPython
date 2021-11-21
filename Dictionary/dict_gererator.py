import random

# Генератор списка случайных чисел  в одну строку
array = [random.randint(-100,100) for _ in range(100)]

# Поиск по условию в одну строку

array_lower = [item for item in array if item < 0]

print(array)
print(array_lower)

# Обмен значений переменных не используя дополнительную переменную
a = 10
b = 20

a , b = b, a

print(a, b)

# Генератор матрицы и красивый вывод

matrix = [[random.randint(1,10) for _ in range(5)] for _ in range(7)]
for line in matrix:
    for item in line:
        print(f"{item:>4}", end="")
    print()