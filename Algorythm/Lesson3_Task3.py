# 3. В массиве случайных целых чисел поменять местами минимальный и
# максимальный элементы.

import random
size = 10

list = [random.randint(0, 99) for _ in range(size)]
print(f"Before   : {list}")

max = list[0]
min = list[0]
max_index = 0
min_index = 0

for index in range(1,size):
    if list[index] > max:
        max = list[index]
        max_index = index
    elif list[index] < min:
        min = list[index]
        min_index = index

wildcard = ["" for _ in range(size)]
wildcard[min_index] = min
wildcard[max_index] = max
print(f"Wildcard : {wildcard}")

list[min_index], list[max_index] = list[max_index], list[min_index]
print(f"After    : {list}")