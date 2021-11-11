# https://python-scripts.com/object-oriented-programming-in-python
# Auto params
# Auto constructor __init__
# Auto method engine_start
# Auto method engine_stop
# Auto method get_info

class Auto:
    print(f"Класс Auto:")
    # Аттрибут, который используется по всему класс
    auto_count = 0
    print(f"Аттрибут класса auto_count: {auto_count}")
    # __init__ Запускается при инициализации класса - вводятся скобки.
    def __init__(self, auto_brand, auto_model):
        print(f"Конструктор __init__ с Аттрибутами экземпляра: {auto_brand} {auto_model}")
        self.auto_brand = auto_brand
        self.auto_model = auto_model
        self.engine_status = False
        # Изменяем внешний параметр иначе будет применимо только в рамках одного объекта.
        Auto.auto_count += 1

    def engine_start(self):
        print(f"Метод def engine_start(self):")
        self.engine_status = True
        return print("Двигатель заведен")

    def engine_stop(self):
        print(f"Метод def engine_stop(self):")
        self.engine_status = False
        return print("Двигатель остановлен")

    def get_info(self):
        print(f"Метод get_info(self):")
        print(f"{self.auto_brand} {self.auto_model} {self.engine_status}")

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
# Общий блок класса пропущен так как он уже вызывался для этого класса

# Создадим новый объект
object_auto_1 = Auto("Infinity","FX37")
print(f"---3---: {object_auto_1}")
# Общий блок класса пропущен так как он уже вызывался для этого класса

# Вызываем внутренние переменные объекта
print(f"---4---: {object_auto.auto_brand} {object_auto.auto_model} {object_auto.auto_count}")
print(f"---4---: {object_auto_1.auto_brand} {object_auto_1.auto_model} {object_auto_1.auto_count}")
# Lexus RX300 1 // доступны и внутренние и внешние переменны по одному запросу

object_auto.engine_start()
print(f"---5---: {object_auto.engine_status}")
print(f"---5---: {object_auto_1.engine_status}")
object_auto_1.engine_start()
object_auto.engine_stop()
object_auto.get_info()
object_auto_1.get_info()

