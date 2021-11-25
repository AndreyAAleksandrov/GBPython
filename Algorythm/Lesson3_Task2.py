# 2. Во втором массиве сохранить индексы чётных элементов первого
# массива. Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то
# во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 -
# если индексация начинается с нуля), т.к. именно в этих позициях первого
# массива стоят чётные числа.

import random

size = 20

list = [random.randint(0, 100) for _ in range(size)]
print(f"Array      : {list}")
wildcard = ["" for _ in range(size)]
even_index = []

for index in range(len(list)):
    if list[index] % 2 == 0:
        even_index.append(index)
        wildcard[index] = list[index]

print(f"Wildcard   : {wildcard}")

print(f"Index even : {even_index}")