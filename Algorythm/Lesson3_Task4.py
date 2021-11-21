# 4. Определить, какое число в массиве встречается чаще всего.

import random
size = 20

list = [random.randint(0, 99) for _ in range(size)]
print(f'Array    : {list}')

max_count = 0
max_item = list[0]

for item in list:
    count = 0
    for compare_item in list:
        if item == compare_item:
            count += 1
    if count > max_count:
        max_count = count
        max_item = item

wildcard = ["" for _ in range(size)]
for i in range(size):
    if max_item == list[i]:
        wildcard[i]=max_item
print(f"Wildcard : {wildcard}")

print(max_item, max_count)