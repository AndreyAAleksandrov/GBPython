# 5. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

alphabet = 'abcdefghijklmnopqrstuvwxyz'

position = int(input('Введите порядковый номер буквы : '))-1

letter = alphabet[position]

print(f'Под номеров {position+1} находится буква "{letter}"')