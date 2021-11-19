# Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
# определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь
#Again

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
            склад (количество - 1)
    конструктор:
        вывод общего списка оборудования с распределением за отделами
    """
    warehouse_equipment = []
    provided_equipment = []
    def __init__(self, name):
        self.name = name

    def new_supply(self, equipment, qty):
        dict_item = {
            "vendor" : equipment.vendor,
            "model" : equipment.model,
            "year" : equipment.year,
            "printstatus" : equipment.printstatus,
            "scanstatus" : equipment.scanstatus,
            "qty" : qty}

        print(f"Поставлено оборудование {dict_item['vendor']}, {dict_item['model']}, {qty} штук")
        if qty > 0:
            addstatus = False
            if self.warehouse_equipment:
                for item in self.warehouse_equipment:
                    if equipment.vendor == item["vendor"] and equipment.model == item["model"] and equipment.year == item["year"]:
                        item["qty"] += qty
                        addstatus = True
            if not addstatus:
                self.warehouse_equipment.append(dict_item)

    def disposal(self, equipment, qty):
        deleteline = False
        for item in self.warehouse_equipment:
            if equipment.vendor == item["vendor"] and equipment.model == item["model"] and equipment.year == item["year"]:
                if qty<item["qty"]:
                    item["qty"] -= qty
                else:
                    deleteline = item
                    print("Передано все доступное оборудование")
                break
            else: print("Такое оборудование на складе не найдено")
        if deleteline:
            self.warehouse_equipment.remove(deleteline)

    def give(self, department, equipment, qty):
        for item in self.warehouse_equipment:
            if equipment.vendor == item["vendor"] and equipment.model == item["model"] and equipment.year == item["year"]:
                if qty < item["qty"]:
                    dict_item = {
                        "department": department.name,
                        "vendor": equipment.vendor,
                        "model": equipment.model,
                        "year": equipment.year,
                        "qty": qty}
                    self.provided_equipment.append(dict_item)
                    self.disposal(equipment,qty)
                    department.take_equipment(dict_item)
                else:
                    dict_item = {
                        "department": department.name,
                        "vendor": equipment.vendor,
                        "model": equipment.model,
                        "year": equipment.year,
                        "qty": item["qty"]}
                    self.provided_equipment.append(dict_item)
                    self.disposal(equipment, item["qty"])
                break

    def __str__(self):
        text = f"------- На складе {self.name} хранится: ------------\n"
        for item in self.warehouse_equipment:
            text = f"{text}{item}\n"
        text += f"------- Передано: ------------\n"
        for item in self.provided_equipment:
            text = f"{text}{item}"
        return text

class Equipment:
    """
    аттрибуты
        производитель
        модель
        год
    методы:
        генерация инвентарного номера
        общая стоимость оборудования
    """
    def __init__(self, vendor, model, year):
        self.vendor = vendor
        self.model = model
        self.year = year

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
    def __init__(self, vendor, model, year, printmax, scanformat):
        super().__init__(vendor, model, year)
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
    def __init__(self, vendor, model, year, printmax):
        super().__init__(vendor, model, year)
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
    def __init__(self, vendor, model, year, scanformat):
        super().__init__(vendor, model, year)
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
        self.dept_equipment = []

    def take_equipment(self, equipment):
        self.dept_equipment = equipment

    def return_equipment(self):
        pass


print("*"*100)
# Первое задание
main_warehouse = Warehouse(name="Основной")
xerox = Xerox(vendor="Xerox",model="Junior",year=2020, printmax=10000, scanformat="A4")
printer = Printer(vendor="Samsung",model="LP1000",year=2021, printmax=10000)
scaner = Scaner(vendor="HP",model="SJ200",year=2019, scanformat="A4 A3")
department_finance = Department(name="Бухгалтерия", headcount=5)
department_sales = Department(name="Продажи", headcount=20)
print("*"*100)
# Второе задание
# На склад поставляют оборудование:
main_warehouse.new_supply(xerox, 10)
main_warehouse.new_supply(xerox,5)
main_warehouse.new_supply(printer, 20)
main_warehouse.new_supply(scaner, 5)

print(main_warehouse)

main_warehouse.disposal(xerox,5)

print(main_warehouse)

main_warehouse.give(department_finance, xerox, 5)
print(main_warehouse)

print("*"*100)
print("В департаменте зарегистрировано:", department_finance.dept_equipment)