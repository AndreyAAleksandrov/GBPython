# Task 1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
# Task 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
i = input("Введите число n")
print(i)

i = int(i)+ int(str(i) + str(i)) + int(str(i) + str(i) + str(i))
print("Сумма n + nn + nnn равна",i)

j = input("Введите любое слово")
print(j)

# Task 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
k = input("Введите секунды")
k = int(k)
hours = str(k // 3600)
minutes = str((k % 3600) // 60)
seconds = str(k % 60)
print(hours + ":" + minutes + ":" + seconds)

# Task 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
l = int(input("Введите большое число для определения максимума"))
m = l%10
l = l//10
while l > 0:
    if l%10 > m:
        m = l%10
    l = l//10
print(m)

# Task 5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

revenue = int(input("Введите выручку"))
cost = int(input("Введите издержки"))

if revenue > cost:
    print("Компания работает с прибылью", revenue - cost, "Rub")
    print("Рентабельность", revenue / cost *100, "%")
    employee = int(input("Введите численность персонала"))
    print("Прибыль на одноо сотрудника", (revenue - cost) / employee, "Rub")
elif revenue < cost:
    print("Компания работает с убытками", cost - revenue)
else:
    print("Компания работает в ноль")

# Task 6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров. Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

a = float(input("Введите число а"))
b = float(input("Введите число b"))
i = 1
print(i,"й день: ",a)
while a<= b:
    a = a * 1.1
    i += 1
    print(i,"й день: ",a)