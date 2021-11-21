# 5. В массиве найти максимальный отрицательный элемент. Вывести на
# экран его значение и позицию в массиве.

import random
size = 10

list = [random.randint(-99, 99) for _ in range(size)]
print(f"Array    : {list}")

min_index = 0
min_item = list[0]

for index in range(1,size):
    if list[index] < min_item:
        min_index = index
        min_item = list[index]

if min_item >= 0:
    print(f"В массиве нет отрицательных элементов")
else:
    wildcard = ["" for _ in range(size)]
    for i in range(size):
        if min_item == list[i]:
            wildcard[i] = min_item
    print(f"Wildcard : {wildcard}")

    print(f"Максимальный отрицательный элемент: {min_item} находится на позиции {min_index}")