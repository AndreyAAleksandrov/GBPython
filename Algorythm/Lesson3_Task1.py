# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них
# кратны каждому из чисел в диапазоне от 2 до 9.

for natural in range(2,10):
    result = []
    for digits in range(2,100):
        if digits % natural == 0:
            result.append(digits)
    print(f"Для числа {natural}, количество кратных {len(result)}, сами числа: {result}")
