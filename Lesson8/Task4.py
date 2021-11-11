# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В
# базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.


class Warehouse:
    """
    аттрибуты:
        количество оборудования на складе
    методы:
        новая поставка (класс оборудование, аттрибут количество)
            оборудование (производитель, модель)
            склад (количество + аттрибут количество)
        утилизация старого оборудования (класс оборудование, аттрибут количество)
            оборудование (производитель, модель)
            склад (количество - аттрибут количество)
        принять на склад (класс оборудование, класс отдел)
            оборудование (производитель, модель)
            отдел (название отдела)
            склад (количество + 1)
        отдать со склада (класс оборудование, класс отдел)
            оборудование (производитель, модель)
            отдел (название отдела)
            склад (количество -1)
    конструктор:
        вывод общего списка оборудования с распределением за отделами
    """
    equipment_qty = 0
    def __init__(self, name):
        self.name = name

class Equipment:
    """
    аттрибуты
        производитель
        модель
        год
        цена
    методы:
        генерация инвентарного номера
        общая стоимость оборудования
    """
    def __init__(self, vendor, model, year, price):
        self.vendor = vendor
        self.model = model
        self.year = year
        self.price = price

class Xerox(Equipment):
    """
    аттрибуты
        возможность печати - True
        возможность сканирования - True
        ресурс печати страниц
        поддерживаемые форматы сканирования
    """
    printstatus = True
    scanstatus = True
    def __init__(self, vendor, model, year, price, printmax, scanformat):
        super().__init__(vendor, model, year, price)
        self.printmax = printmax
        self.scanformat = scanformat

class Printer(Equipment):
    """
    аттрибуты
        возможность печати - True
        возможность сканирования - False
        ресурс печати страниц
    """
    printstatus = True
    scanstatus = False
    def __init__(self, vendor, model, year, price, printmax):
        super().__init__(vendor, model, year, price)
        self.printmax = printmax

class Scaner(Equipment):
    """
    аттрибуты
        возможность печати - False
        возможность сканирования - True
        поддерживаемые форматы сканирования
    """
    printstatus = False
    scanstatus = True
    def __init__(self, vendor, model, year, price, scanformat):
        super().__init__(vendor, model, year, price)
        self.scanformat = scanformat

class Department:
    """
    аттрибуты:
        название отдела
    методы:
        отдать на склад (класс оборудование)
            оборудование (производитель, модель)
            отдел (количество - 1)
        получить со склада (класс оборудование
            оборудование (производитель, модель)
            отдел (название отдела)
            склад (количество -1)
    конструктор:
        вывод общего списка оборудования в отделе
        вывод количества устройств на человека в отделе
    """
    def __init__(self, name, headcount):
        self.name = name
        self.headcount = headcount

main_warehouse = Warehouse("Основной")
print(main_warehouse.equipment_qty)
print(main_warehouse.name)

xerox = Xerox(vendor="Xerox",model="Junior",year=2020, price=3000, printmax=10000, scanformat="A4")
printer = Printer(vendor="Samsung",model="LP1000",year=2021, price=3000, printmax=10000)
scaner = Scaner(vendor="HP",model="SJ200",year=2019, price=3000, scanformat="A4 A3")

print(xerox.vendor)
print(printer.vendor)
print(scaner.vendor)

department = Department("Бухгалтерия", 10)
print(department.name)




