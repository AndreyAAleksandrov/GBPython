class Auto:
    # Параметр, который используется по всему классу
    auto_count = 0
    # __init__ Запускается при инициализации класса - вводятся скобки.
    def __init__(self, auto_brand, auto_model):
        self.auto_brand = auto_brand
        self.auto_model = auto_model
        # Изменяем внешний параметр иначе будет применимо только в рамках одного объекта.
        Auto.auto_count += 1

# Вызываем класс без параметров ()
object_auto = Auto
print(f"---1---: {object_auto}")
# <class '__main__.Auto'> // только говорит о наличии класса и не более

# Используем переменную из class
print(f"---2---: {object_auto.auto_count}")
# 0 // Уже присутствует переменная в классе

# Вызывая self, параметры становятся обязательными
object_auto = Auto("Lexus","RX300")
print(f"---3---: {object_auto}")
# <__main__.Auto object at 0x7fcf47ccd160> // Объект уже начал храниться в памяти компьютера

# Вызываем внутренние переменные объекта
print(f"---4---: {object_auto.auto_brand} {object_auto.auto_model} {object_auto.auto_count}")
# Lexus RX300 1 // доступны и внутренние и внешние переменны по одному запросу
