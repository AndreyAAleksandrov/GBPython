# 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25,
# -0.125,… Количество элементов (n) вводится с клавиатуры.

n = int(input('Введите количество элементов: '))
series_number = 1
sum = 0
for i in range(n):
    sum += series_number
    series_number /= -2

print(f'Сумма {sum}')